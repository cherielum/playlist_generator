from app import app
from app.forms import SongSearchForm
from app.models import AudioFeatures, Playlist, Track
from flask import request, render_template, redirect, url_for, session
from functools import wraps
from redis import Redis
from spotipy import util
from uuid import uuid4
import os
import spotipy
import time


redis = Redis.from_url(os.environ['REDIS_URL'])
oauth = spotipy.oauth2.SpotifyOAuth(
    client_id=os.environ['SPOTIPY_CLIENT_ID'],
    client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
    redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'],
    scope='playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative')


def get_access_token():
    if 'id' in session:
        expires_at = redis.get('user_id.{}.expires_at'.format(session['id']))
        if expires_at is None or float(expires_at) <= time.time():
            refresh_token = redis.get('user_id.{}.refresh_token'.format(session['id']))
            auth = oauth.refresh_access_token(refresh_token)
            store_auth(session['id'], auth)
        access_token = redis.get('user_id.{}.access_token'.format(session['id']))
        if access_token:
            return access_token.decode('utf-8')


def create_spotify():
    access_token = get_access_token()
    if access_token:
        spotify = spotipy.Spotify(access_token)
        return spotify


def requires_spotify(route):
    @wraps(route)
    def decorated_function(*args, **kwargs):
        try:
            spotify = create_spotify()
            if spotify is None:
                return redirect(url_for('login'))
            return route(spotify=spotify, *args, **kwargs)
        except spotipy.client.SpotifyException as error:
            if error.http_status == 401:
                return redirect(url_for('login'))
            raise error

    return decorated_function


def store_auth(session_id, auth):
    access_token = auth['access_token']
    expires_at = auth['expires_at']
    refresh_token = auth['refresh_token']
    redis.set('user_id.{}.access_token'.format(session_id), access_token)
    redis.set('user_id.{}.expires_at'.format(session_id), expires_at)
    redis.set('user_id.{}.refresh_token'.format(session_id), refresh_token)

@app.route('/')
def index():
    form = SongSearchForm()
    return render_template('index.html',
        form=form)


@app.route('/login')
def login():
    return redirect(oauth.get_authorize_url())


@app.route('/authorization')
def authorization():
    session['id'] = str(uuid4())
    auth = oauth.get_access_token(request.args['code'])
    store_auth(session['id'], auth)
    return redirect(url_for('index'))


@app.route('/recommended_track', methods=['POST'])
@requires_spotify
def recommended_track(spotify):
    form = SongSearchForm()
    if form.validate_on_submit():
        track_ids = [form.song1_id.data, form.song2_id.data]
        audio_features = AudioFeatures(spotify.audio_features(tracks=track_ids))
        recommendations = spotify.recommendations(
            limit=1,
            seed_tracks=track_ids,
            target_danceability=audio_features.mean('danceability'),
            target_acousticness=audio_features.mean('acousticness'),
            target_energy=audio_features.mean('energy'),
            target_instrumentalness=audio_features.mean('instrumentalness'),
            target_key=round(audio_features.mean('key')),
            target_liveness=audio_features.mean('liveness'),
            target_loudness=audio_features.mean('loudness'),
            # target_mode=audio_features.mean('mode'),
            # target_popularity=round(audio_features.mean('popularity')),
            target_speechiness=audio_features.mean('speechiness'),
            target_tempo=audio_features.mean('tempo'),
            target_time_signature=round(audio_features.mean('time_signature')),
            target_valence=audio_features.mean('valence')
        )
        track = Track(recommendations['tracks'][0])
        user_id = spotify.current_user()['id']
        spotify.user_playlist_add_tracks(user_id, form.playlist_id.data, [track.id()], form.position.data)
        return redirect(url_for('playlist', playlist_id=form.playlist_id.data))
    else:
        return redirect(request.referrer or url_for('index'))


@app.route('/audio_features')
@requires_spotify
def audio_features(spotify):
    tracks = [request.args['track_id']]
    results = spotify.audio_features(tracks=tracks)
    return str(results)


@app.route('/playlist/<playlist_id>')
@requires_spotify
def playlist(playlist_id, spotify):
    user_id = spotify.current_user()['id']
    api_response = spotify.user_playlist(user_id, playlist_id)
    playlist = Playlist(api_response)
    form = SongSearchForm()
    return render_template('playlist.html',
        playlist=playlist,
        items=playlist.items(),
        form=form)



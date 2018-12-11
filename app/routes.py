from app import app
from flask import request, render_template, redirect, url_for
from spotipy import util
from app.forms import SongSearchForm
from app.models import AudioFeatures, Playlist, Track

import spotipy
token = util.prompt_for_user_token('3artqygk5gf3tyb7vhcz8enal', 'playlist-read-private playlist-modify-private playlist-modify-public')
spotify = spotipy.Spotify(auth=token)


@app.route('/')
@app.route('/index')
def index():
    form = SongSearchForm()
    return render_template('index.html', form=form)


@app.route('/recommended_track', methods=['POST'])
def recommended_track():
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
        return redirect(request.referrer)


@app.route('/audio_features')
def audio_features():
    tracks = [request.args['track_id']]
    results = spotify.audio_features(tracks=tracks)
    return str(results)


@app.route('/playlist/<playlist_id>')
def playlist(playlist_id):
    user_id = spotify.current_user()['id']
    api_response = spotify.user_playlist(user_id, playlist_id)
    playlist = Playlist(api_response)
    form = SongSearchForm()
    return render_template('playlist.html',
        playlist=playlist,
        items=playlist.items(),
        form=form)



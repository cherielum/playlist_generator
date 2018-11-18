from app import app
from flask import request, render_template
from spotipy import util
from app.forms import SongSearchForm

import spotipy
token = util.prompt_for_user_token('3artqygk5gf3tyb7vhcz8enal', 'playlist-read-private')
spotify = spotipy.Spotify(auth=token)


@app.route('/')
@app.route('/index')
def index():
    form = SongSearchForm()
    return render_template('index.html', form=form)


@app.route('/song_search', methods=['POST'])
def song_search():
    form = SongSearchForm()
    if form.validate_on_submit():
        return render_template('song_search.html')
    else:
        return render_template('index.html', form=form)


@app.route('/audio_features')
def audio_features():
    tracks = [request.args['track_id']]
    results = spotify.audio_features(tracks=tracks)
    return str(results)



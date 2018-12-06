from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField

class SongSearchForm(FlaskForm):
    playlist_id = StringField('Playlist ID')
    song1_id = StringField('Song 1 ID')
    song2_id = StringField('Song 2 ID')
    position = StringField('Position')
    submit = SubmitField('Search')

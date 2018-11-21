from statistics import mean

class AudioFeatures(object):
    """Extracts data from Spotify Audio Features objects

    >>> api_response = [{'danceability': 0.694, 'energy': 0.815, 'key': 2, 'loudness': -4.328, 'mode': 1, 'speechiness': 0.12, 'acousticness': 0.229, 'instrumentalness': 0, 'liveness': 0.0924, 'valence': 0.813, 'tempo': 88.931, 'type': 'audio_features', 'id': '5CtI0qwDJkDQGwXD1H1cLb', 'uri': 'spotify:track:5CtI0qwDJkDQGwXD1H1cLb', 'track_href': 'https://api.spotify.com/v1/tracks/5CtI0qwDJkDQGwXD1H1cLb', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/5CtI0qwDJkDQGwXD1H1cLb', 'duration_ms': 228827, 'time_signature': 4}, {'danceability': 0.599, 'energy': 0.667, 'key': 7, 'loudness': -4.267, 'mode': 1, 'speechiness': 0.0367, 'acousticness': 0.0533, 'instrumentalness': 0, 'liveness': 0.134, 'valence': 0.817, 'tempo': 80.984, 'type': 'audio_features', 'id': '72Q0FQQo32KJloivv5xge2', 'uri': 'spotify:track:72Q0FQQo32KJloivv5xge2', 'track_href': 'https://api.spotify.com/v1/tracks/72Q0FQQo32KJloivv5xge2', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/72Q0FQQo32KJloivv5xge2', 'duration_ms': 288877, 'time_signature': 4}]

    >>> af = AudioFeatures(api_response)

    >>> af.min('danceability')
    0.599

    >>> af.max('danceability')
    0.694

    >>> af.mean('danceability')
    0.6465

    >>> af.min('energy')
    0.667

    >>> af.min('liveness')
    0.0924
    """

    def __init__(self, api_response):
        self.api_response = api_response

    def min(self, feature):
        return min(self.api_response[0][feature], self.api_response[1][feature])

    def max(self, feature):
        return max(self.api_response[0][feature], self.api_response[1][feature])

    def mean(self, feature):
        return mean([self.api_response[0][feature], self.api_response[1][feature]])
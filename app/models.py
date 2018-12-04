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


class Playlist(object):
    """

    >>> api_response = {'collaborative': False, 'description': '', 'external_urls': {'spotify': 'https://open.spotify.com/playlist/7qD7y5EnpXWNCMk3RpDFQ2'}, 'followers': {'href': None, 'total': 0}, 'href': 'https://api.spotify.com/v1/playlists/7qD7y5EnpXWNCMk3RpDFQ2', 'id': '7qD7y5EnpXWNCMk3RpDFQ2', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/f181188e81fb8d8a1333afe5d4d37a65cc704e2f', 'width': 640}], 'name': 'Testing Playlist 2018', 'owner': {'display_name': 'Cherie Lum', 'external_urls': {'spotify': 'https://open.spotify.com/user/3artqygk5gf3tyb7vhcz8enal'}, 'href': 'https://api.spotify.com/v1/users/3artqygk5gf3tyb7vhcz8enal', 'id': '3artqygk5gf3tyb7vhcz8enal', 'type': 'user', 'uri': 'spotify:user:3artqygk5gf3tyb7vhcz8enal'}, 'primary_color': None, 'public': True, 'snapshot_id': 'MyxmMzY3MmI3MTBhYzkxN2I3MTA0NTBjZjNjMjk0YjczODRhOGFlMzdi', 'tracks': {'href': 'https://api.spotify.com/v1/playlists/7qD7y5EnpXWNCMk3RpDFQ2/tracks?offset=0&limit=100', 'items': [{'added_at': '2018-12-04T01:28:42Z', 'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/3artqygk5gf3tyb7vhcz8enal'}, 'href': 'https://api.spotify.com/v1/users/3artqygk5gf3tyb7vhcz8enal', 'id': '3artqygk5gf3tyb7vhcz8enal', 'type': 'user', 'uri': 'spotify:user:3artqygk5gf3tyb7vhcz8enal'}, 'is_local': False, 'primary_color': None, 'track': {'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6ppQ1vjjme5Jtz2ceBFcWY'}, 'href': 'https://api.spotify.com/v1/artists/6ppQ1vjjme5Jtz2ceBFcWY', 'id': '6ppQ1vjjme5Jtz2ceBFcWY', 'name': 'Yoga Music', 'type': 'artist', 'uri': 'spotify:artist:6ppQ1vjjme5Jtz2ceBFcWY'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/1508kSLULYbyHDzGbTahVv'}, 'href': 'https://api.spotify.com/v1/albums/1508kSLULYbyHDzGbTahVv', 'id': '1508kSLULYbyHDzGbTahVv', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/f181188e81fb8d8a1333afe5d4d37a65cc704e2f', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/9a01e445ed75fe11d1a473589c92241495d8833b', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ccbbf6d4c758f2f2ef73d44e2903d2da4d25b8cc', 'width': 64}], 'name': 'Instrumental Piano and Relaxing Piano Music for Yoga Spa Meditation Relaxation and Music for Spa', 'release_date': '2014-11-05', 'release_date_precision': 'day', 'total_tracks': 31, 'type': 'album', 'uri': 'spotify:album:1508kSLULYbyHDzGbTahVv'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6ppQ1vjjme5Jtz2ceBFcWY'}, 'href': 'https://api.spotify.com/v1/artists/6ppQ1vjjme5Jtz2ceBFcWY', 'id': '6ppQ1vjjme5Jtz2ceBFcWY', 'name': 'Yoga Music', 'type': 'artist', 'uri': 'spotify:artist:6ppQ1vjjme5Jtz2ceBFcWY'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 144039, 'episode': False, 'explicit': False, 'external_ids': {'isrc': 'USA2P1477986'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/2WwDvI6ZwXRS3VmISOqBkO'}, 'href': 'https://api.spotify.com/v1/tracks/2WwDvI6ZwXRS3VmISOqBkO', 'id': '2WwDvI6ZwXRS3VmISOqBkO', 'is_local': False, 'name': 'Pachelbel Canon in D', 'popularity': 46, 'preview_url': 'https://p.scdn.co/mp3-preview/8c6792a6012e301274d54e10ce6cc01c9b57c5e6?cid=4d1756ce0cde4907923b9b6f79314063', 'track': True, 'track_number': 25, 'type': 'track', 'uri': 'spotify:track:2WwDvI6ZwXRS3VmISOqBkO'}, 'video_thumbnail': {'url': None}}, {'added_at': '2018-12-04T01:29:07Z', 'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/3artqygk5gf3tyb7vhcz8enal'}, 'href': 'https://api.spotify.com/v1/users/3artqygk5gf3tyb7vhcz8enal', 'id': '3artqygk5gf3tyb7vhcz8enal', 'type': 'user', 'uri': 'spotify:user:3artqygk5gf3tyb7vhcz8enal'}, 'is_local': False, 'primary_color': None, 'track': {'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1HxJeLhIuegM3KgvPn8sTa'}, 'href': 'https://api.spotify.com/v1/artists/1HxJeLhIuegM3KgvPn8sTa', 'id': '1HxJeLhIuegM3KgvPn8sTa', 'name': 'Jack Ü', 'type': 'artist', 'uri': 'spotify:artist:1HxJeLhIuegM3KgvPn8sTa'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5he5w2lnU9x7JFhnwcekXX'}, 'href': 'https://api.spotify.com/v1/artists/5he5w2lnU9x7JFhnwcekXX', 'id': '5he5w2lnU9x7JFhnwcekXX', 'name': 'Skrillex', 'type': 'artist', 'uri': 'spotify:artist:5he5w2lnU9x7JFhnwcekXX'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5fMUXHkw8R8eOP2RNVYEZX'}, 'href': 'https://api.spotify.com/v1/artists/5fMUXHkw8R8eOP2RNVYEZX', 'id': '5fMUXHkw8R8eOP2RNVYEZX', 'name': 'Diplo', 'type': 'artist', 'uri': 'spotify:artist:5fMUXHkw8R8eOP2RNVYEZX'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/6bfkwBrGYKJFk6Z4QVyjxd'}, 'href': 'https://api.spotify.com/v1/albums/6bfkwBrGYKJFk6Z4QVyjxd', 'id': '6bfkwBrGYKJFk6Z4QVyjxd', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/b962d9c0353ef080806b5599cd6618ef0b266880', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/e3d922ad543fa3158ae7f4507fb23d0cd2004143', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/97e4a1c40ac374a49dff6480459f23e8cfea2dfe', 'width': 64}], 'name': 'Skrillex and Diplo present Jack Ü', 'release_date': '2015-02-24', 'release_date_precision': 'day', 'total_tracks': 10, 'type': 'album', 'uri': 'spotify:album:6bfkwBrGYKJFk6Z4QVyjxd'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1HxJeLhIuegM3KgvPn8sTa'}, 'href': 'https://api.spotify.com/v1/artists/1HxJeLhIuegM3KgvPn8sTa', 'id': '1HxJeLhIuegM3KgvPn8sTa', 'name': 'Jack Ü', 'type': 'artist', 'uri': 'spotify:artist:1HxJeLhIuegM3KgvPn8sTa'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5he5w2lnU9x7JFhnwcekXX'}, 'href': 'https://api.spotify.com/v1/artists/5he5w2lnU9x7JFhnwcekXX', 'id': '5he5w2lnU9x7JFhnwcekXX', 'name': 'Skrillex', 'type': 'artist', 'uri': 'spotify:artist:5he5w2lnU9x7JFhnwcekXX'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5fMUXHkw8R8eOP2RNVYEZX'}, 'href': 'https://api.spotify.com/v1/artists/5fMUXHkw8R8eOP2RNVYEZX', 'id': '5fMUXHkw8R8eOP2RNVYEZX', 'name': 'Diplo', 'type': 'artist', 'uri': 'spotify:artist:5fMUXHkw8R8eOP2RNVYEZX'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/1uNFoZAHBGtllmzznpCI3s'}, 'href': 'https://api.spotify.com/v1/artists/1uNFoZAHBGtllmzznpCI3s', 'id': '1uNFoZAHBGtllmzznpCI3s', 'name': 'Justin Bieber', 'type': 'artist', 'uri': 'spotify:artist:1uNFoZAHBGtllmzznpCI3s'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 250285, 'episode': False, 'explicit': False, 'external_ids': {'isrc': 'USAT21500555'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/66hayvUbTotekKU3H4ta1f'}, 'href': 'https://api.spotify.com/v1/tracks/66hayvUbTotekKU3H4ta1f', 'id': '66hayvUbTotekKU3H4ta1f', 'is_local': False, 'name': 'Where Are Ü Now (with Justin Bieber)', 'popularity': 76, 'preview_url': 'https://p.scdn.co/mp3-preview/edd7282e93a954b2b48cfc136aa63b0396c16406?cid=4d1756ce0cde4907923b9b6f79314063', 'track': True, 'track_number': 9, 'type': 'track', 'uri': 'spotify:track:66hayvUbTotekKU3H4ta1f'}, 'video_thumbnail': {'url': None}}], 'limit': 100, 'next': None, 'offset': 0, 'previous': None, 'total': 2}, 'type': 'playlist', 'uri': 'spotify:user:3artqygk5gf3tyb7vhcz8enal:playlist:7qD7y5EnpXWNCMk3RpDFQ2'}

    >>> playlist = Playlist(api_response)

    >>> playlist.name()
    'Testing Playlist 2018'

    >>> len(playlist.tracks())
    2

    >>> playlist.tracks()[0].__class__.__name__
    'Track'
    """

    def __init__(self, api_response):
        self.api_response = api_response

    def name(self):
        return self.api_response['name']

    def tracks(self):
        return [Track(data) for data in self.api_response['tracks']['items']]


class Track():
    """
    >>> api_response = {'added_at': '2018-12-04T01:28:42Z', 'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/3artqygk5gf3tyb7vhcz8enal'}, 'href': 'https://api.spotify.com/v1/users/3artqygk5gf3tyb7vhcz8enal', 'id': '3artqygk5gf3tyb7vhcz8enal', 'type': 'user', 'uri': 'spotify:user:3artqygk5gf3tyb7vhcz8enal'}, 'is_local': False, 'primary_color': None, 'track': {'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6ppQ1vjjme5Jtz2ceBFcWY'}, 'href': 'https://api.spotify.com/v1/artists/6ppQ1vjjme5Jtz2ceBFcWY', 'id': '6ppQ1vjjme5Jtz2ceBFcWY', 'name': 'Yoga Music', 'type': 'artist', 'uri': 'spotify:artist:6ppQ1vjjme5Jtz2ceBFcWY'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/1508kSLULYbyHDzGbTahVv'}, 'href': 'https://api.spotify.com/v1/albums/1508kSLULYbyHDzGbTahVv', 'id': '1508kSLULYbyHDzGbTahVv', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/f181188e81fb8d8a1333afe5d4d37a65cc704e2f', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/9a01e445ed75fe11d1a473589c92241495d8833b', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ccbbf6d4c758f2f2ef73d44e2903d2da4d25b8cc', 'width': 64}], 'name': 'Instrumental Piano and Relaxing Piano Music for Yoga Spa Meditation Relaxation and Music for Spa', 'release_date': '2014-11-05', 'release_date_precision': 'day', 'total_tracks': 31, 'type': 'album', 'uri': 'spotify:album:1508kSLULYbyHDzGbTahVv'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6ppQ1vjjme5Jtz2ceBFcWY'}, 'href': 'https://api.spotify.com/v1/artists/6ppQ1vjjme5Jtz2ceBFcWY', 'id': '6ppQ1vjjme5Jtz2ceBFcWY', 'name': 'Yoga Music', 'type': 'artist', 'uri': 'spotify:artist:6ppQ1vjjme5Jtz2ceBFcWY'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 144039, 'episode': False, 'explicit': False, 'external_ids': {'isrc': 'USA2P1477986'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/2WwDvI6ZwXRS3VmISOqBkO'}, 'href': 'https://api.spotify.com/v1/tracks/2WwDvI6ZwXRS3VmISOqBkO', 'id': '2WwDvI6ZwXRS3VmISOqBkO', 'is_local': False, 'name': 'Pachelbel Canon in D', 'popularity': 46, 'preview_url': 'https://p.scdn.co/mp3-preview/8c6792a6012e301274d54e10ce6cc01c9b57c5e6?cid=4d1756ce0cde4907923b9b6f79314063', 'track': True, 'track_number': 25, 'type': 'track', 'uri': 'spotify:track:2WwDvI6ZwXRS3VmISOqBkO'}, 'video_thumbnail': {'url': None}}

    >>> track = Track(api_response)

    >>> track.name()
    'Pachelbel Canon in D'
    """

    def __init__(self, api_response):
        self.api_response = api_response

    def name(self):
        return self.api_response['track']['name']
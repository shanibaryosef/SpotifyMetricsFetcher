# import requests
#
# # A valid OAuth token (Client Credentials Flow or Authorization Code Flow)
# headers = {
#     "Authorization": r"Bearer BQDQusBYODSLYvJjvWSAIUTgtU7XSqkyDjUG9rJVdHjb_sx9E4EqXtLvhDQmjFSmYr75WlJzT5LRJpm83q8Ig_j77xDcHg1dL6Hk_UTMo9HIRsvzRyU",
# }
#
# track_id = "11dFghVXANMlKmJXsNCbNl"  # Example track
#
# url = f"https://api.spotify.com/v1/audio-features/{track_id}"
# response = requests.get(url, headers=headers)
#
# if response.status_code == 200:
#     data = response.json()
#     print("Valence:", data["valence"])
#     print("Energy:", data["energy"])
#     print("Tempo:", data["tempo"])
# else:
#     print("Error:", response.status_code, response.json())
import spotipy
from spotipy import SpotifyClientCredentials
client_id = 'a4d37735508d4cab8c520059ff5ee84e'
client_secret = '11a59739203344e3ad53fc5da0ab7dad'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# results = spotify_client.audio_features(['11dFghVXANMlKmJXsNCbNl'])
# results = spotify_client.audio_analysis('11dFghVXANMlKmJXsNCbNl')
results = spotify_client.recommendations('11dFghVXANMlKmJXsNCbNl')
print(results)

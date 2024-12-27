import requests

headers = {
    "Authorization": f"Bearer BQAL7QsDwUAmF0W-z2fjk57vdUNSGj_9dZatNnsNIYgproboP_CiEGIHnwar0ltTNS6jNarM1ysQeFm8WgsoSfty6u-ac702Qv970XlQr2g5aOCsk5U"
}

search_url = "https://api.spotify.com/v1/search"
params = {
    "q": "Top 50 Israel",
    "type": "playlist",
    "limit": 1
}

response = requests.get(search_url, headers=headers, params=params)
search_results = response.json()
playlist_id = search_results['playlists']['items'][0]['id']

print("Playlist ID for Top 50 Israel:", playlist_id)

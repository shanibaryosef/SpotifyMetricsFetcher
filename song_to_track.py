import requests

headers = {
    "Authorization": f"Bearer BQAL7QsDwUAmF0W-z2fjk57vdUNSGj_9dZatNnsNIYgproboP_CiEGIHnwar0ltTNS6jNarM1ysQeFm8WgsoSfty6u-ac702Qv970XlQr2g5aOCsk5U"
}

def get_track_id(song_name, artist_name=None):
    search_url = "https://api.spotify.com/v1/search"
    params = {
        "q": song_name + (f" artist:{artist_name}" if artist_name else ""),
        "type": "track",
        "limit": 1
    }
    response = requests.get(search_url, headers=headers, params=params)
    results = response.json()
    if results["tracks"]["items"]:
        return results["tracks"]["items"][0]["id"]
    else:
        return None

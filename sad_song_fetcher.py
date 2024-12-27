import requests

# Replace with your access token
headers = {
    "Authorization": f"Bearer BQAL7QsDwUAmF0W-z2fjk57vdUNSGj_9dZatNnsNIYgproboP_CiEGIHnwar0ltTNS6jNarM1ysQeFm8WgsoSfty6u-ac702Qv970XlQr2g5aOCsk5U"
}


# Define a function to check if a song is sad
def is_song_sad(track_id):
    # Fetch audio features for the song
    audio_features_url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    response = requests.get(audio_features_url, headers=headers)
    audio_features = response.json()

    # Extract relevant features
    valence = audio_features.get("valence", 0)
    energy = audio_features.get("energy", 0)
    tempo = audio_features.get("tempo", 120)  # default if tempo missing

    # Define sadness criteria
    is_sad = valence < 0.3 and energy < 0.5
    return {
        "valence": valence,
        "energy": energy,
        "tempo": tempo,
        "is_sad": is_sad
    }


# List of track IDs for the songs you want to analyze
track_ids = ['5nYFRLTLrqiETyy6LUPfhQ']  # replace with actual track IDs

# Analyze each song
for track_id in track_ids:
    result = is_song_sad(track_id)
    print(f"Track ID: {track_id}")
    print(f"Valence: {result['valence']}, Energy: {result['energy']}, Tempo: {result['tempo']}")
    print("Sad" if result["is_sad"] else "Not Sad")
    print("-----")

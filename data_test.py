import requests

# Replace with your valid access token
access_token = "BQDIpI2nhOBRdlB2Xn3nuZr3-tQsbW0YA-9vehYuGSHKyjPFcDFXB8SnTS0a3DpwRjdrSPzD9jHUvOMjarBD_Oeec4S2XxHoKSGgjONaDBSFwuNpz9M"

# Set your authorization token
headers = {
    "Authorization": f'Bearer {access_token}'
}

# Step 1: Get top tracks for a country (e.g., Israel)
top_tracks_url = "https://api.spotify.com/v1/playlists/37i9dQZEVXbJ6IpvItkve3/tracks"
# Replace {playlist_id} with a Spotify playlist ID for top songs in Israel, or build your own logic for fetching relevant tracks.

response = requests.get(top_tracks_url, headers=headers)
tracks = response.json()["items"]

# Step 2: For each track, fetch the artist's genres
genre_count = {}
for item in tracks:
    artist_id = item["track"]["artists"][0]["id"]
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"

    artist_response = requests.get(artist_url, headers=headers)
    artist_data = artist_response.json()

    # Spotify provides a list of genres for the artist
    genres = artist_data.get("genres", [])

    # Count the genres
    for genre in genres:
        genre_count[genre] = genre_count.get(genre, 0) + 1

# Step 3: Display genre counts
print("Genre Popularity in Top Tracks:")
for genre, count in genre_count.items():
    print(f"{genre}: {count}")

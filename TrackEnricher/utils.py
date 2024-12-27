import base64
import csv
import requests

def getAccessToken():
    client_id = '7a6df11239224a849bdb7ab86f38d2e8'
    client_secret = 'f439afdf5779434eb4585aa64d3c84ad'

    auth_string = f"{client_id}:{client_secret}"
    base64_auth_string = base64.b64encode(auth_string.encode()).decode()

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {base64_auth_string}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info['access_token']
        print("Access Token:", access_token)
    else:
        print(f"Error: {response.status_code}")

    return access_token

def getTrackInfo(access_token, track_ids):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    audio_features_url = f"https://api.spotify.com/v1/audio-features/{','.join(track_ids)}"
    print(audio_features_url)
    response = requests.get(audio_features_url, headers=headers)
    audio_features = response.json()
    return audio_features



def getTrackId(track_dict):
    uri = track_dict['uri']
    id = uri.split(':')[-1]
    return id


def csv_to_dict(file_path, row_limit=50):
    rows = []

    # Open the CSV file
    with open(file_path, mode='r', encoding='utf-8', newline='') as csvfile:
        # Use DictReader to get each row as a dictionary
        reader = csv.DictReader(csvfile)

        # Read up to 100 rows
        for index, row in enumerate(reader):
            if index == row_limit:
                break
            rows.append(row)

    return rows

def parseChartCSV(access_token, file_path):
    chart_dict_list = csv_to_dict(file_path, row_limit=1)
    track_ids = []
    for chart_dict in chart_dict_list:
        track_ids.append(getTrackId(chart_dict))
    tracks_info = getTrackInfo(access_token, track_ids)
    print(tracks_info)



parseChartCSV(getAccessToken(), r'E:\Projects\SpotifyMetricsFetcher\downloads\regional-il-weekly-2024-12-26.csv')
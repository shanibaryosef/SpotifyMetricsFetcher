import base64
import csv
import time

import requests


def getAccessToken(client_id, client_secret):
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

def getTrackInfo(access_token, track_id):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    track_url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(track_url, headers=headers)
    if response.status_code == 429:
        print("Throttle reached!")
        retry_after = response.headers.get('Retry-After')
        if retry_after:
            # Convert it to an integer (it should be a string of seconds)
            wait_time = int(retry_after)
            print(f"Retry after {wait_time} seconds.")
            # Optionally sleep for that amount of time before retrying
            time.sleep(wait_time)
            # Then retry your request here if desired
            return getTrackInfo(access_token, track_id)
    else:
        track_info = response.json()
    return track_info

def getArtistInfo(access_token, artist_id):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    artists_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    response = requests.get(artists_url, headers=headers)
    if response.status_code == 429:
        print("Throttle reached!")
        retry_after = response.headers.get('Retry-After')
        if retry_after:
            # Convert it to an integer (it should be a string of seconds)
            wait_time = int(retry_after)
            print(f"Retry after {wait_time} seconds.")
            # Optionally sleep for that amount of time before retrying
            time.sleep(wait_time)
            # Then retry your request here if desired
            return getArtistInfo(access_token, artist_id)
    else:
        artist_info = response.json()
    return artist_info



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
        # Read up to row_limit rows
        for index, row in enumerate(reader):
            if index == row_limit:
                break
            rows.append(row)

    return rows


def dict_to_csv(data, csv_filename):
    """
    Write a list of dictionaries to a CSV file.

    :param data: list of dicts, e.g. [{'Name': 'Alice', 'Age': 30}, ...]
    :param csv_filename: output CSV filename/path
    """
    # Make sure there is at least one dictionary in the list
    if not data:
        print("No data to write.")
        return

    # Extract column names (keys) from the first dictionary
    fieldnames = data[0].keys()

    # Open the CSV file for writing
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header (column names)
        writer.writeheader()

        # Write each dictionary as a row in the CSV
        for row in data:
            writer.writerow(row)

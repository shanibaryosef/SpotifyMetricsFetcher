import csv
import os
import time

from TrackEnricher.utils import getTrackId, getTrackInfo, getArtistInfo, getAccessToken, csv_to_dict, dict_to_csv
from utils.consts import DATA_DIR


def enrichTrackRow(access_token, data_dict):
    track_id = getTrackId(data_dict)
    track_info = getTrackInfo(access_token, track_id)
    artist_id = track_info['artists'][0]['id']
    artist_info = getArtistInfo(access_token, artist_id)
    enrich_dict = {'artist_name': artist_info['name'], 'artist_genres': artist_info['genres'],
                   'album_name': track_info['album']['name']}
    data_dict.update(enrich_dict)
    return data_dict


def enrichData(client_id, client_secret, file_path):
    access_token = getAccessToken(client_id, client_secret)
    data_dict_list = csv_to_dict(file_path) # list of dicts of rows in csv
    file_name = os.path.basename(file_path)
    print(f'Start enriching {file_name}')

    if os.path.exists(os.path.join(DATA_DIR, file_name)): # check if file already exists in data dir
        print("File exists, skipping enrich")
        return

    time.sleep(30)  # rolling windows limitation
    final_dict_list = []
    for data_dict in data_dict_list:
        final_dict_list.append(enrichTrackRow(access_token, data_dict)) # 2 api actions per row

    full_path = os.path.join(DATA_DIR, file_name) # ex. data/file1.csv
    dict_to_csv(final_dict_list, full_path)


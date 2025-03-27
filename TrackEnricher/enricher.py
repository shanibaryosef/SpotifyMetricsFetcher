import csv
import os
import time

from TrackEnricher.utils import getTrackId, getTrackInfo, getArtistInfo, getAccessToken, csv_to_dict, dict_to_csv, isIsraeli
from utils.consts import DATA_DIR, ENRICHED_DATA_DIR, MODIFIED_DATA_DIR

def enrichTrackRow(access_token, data_dict):
    track_id = getTrackId(data_dict)
    track_info = getTrackInfo(access_token, track_id) # api action
    artist_id = track_info['artists'][0]['id']
    artist_info = getArtistInfo(access_token, artist_id) # api action
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

    time.sleep(30)  # rolling windows limitation (sec)
    final_dict_list = []
    for data_dict in data_dict_list: # each track in the chart
        final_dict_list.append(enrichTrackRow(access_token, data_dict)) # 2 api actions per row, final_dict_list gets the updated dict

    full_path = os.path.join(DATA_DIR, file_name) # ex. data/file1.csv
    dict_to_csv(final_dict_list, full_path)

def enrichTrackRowWithArtistType(data_dict):
    artistName = data_dict['artist_name']
    trackName = data_dict['track_name']
    albumName = data_dict['album_name']
    artistTypeIsrael = isIsraeli(trackName, albumName, artistName)
    if artistTypeIsrael == True:
        artistType = 'Israeli'
    else:
        artistType = 'International'
    enrich_dict = {'artist_type': artistType}
    data_dict.update(enrich_dict)
    return data_dict

def enrichDataWithArtistType(file_path):
    data_dict_list = csv_to_dict(file_path) # list of dicts of rows in csv
    file_name = os.path.basename(file_path)
    print(f'Start enriching {file_name} with artist type')

    if os.path.exists(os.path.join(ENRICHED_DATA_DIR, file_name)): # check if file already exists in enrichedData dir
        print("File exists, skipping enrich")
        return

    final_dict_list = []
    for data_dict in data_dict_list: # each track in the chart
        final_dict_list.append(enrichTrackRowWithArtistType(data_dict)) # final_dict_list gets the updated dict with the information about the artist type

    full_path = os.path.join(ENRICHED_DATA_DIR, file_name) # ex. enrichedData/file1.csv
    dict_to_csv(final_dict_list, full_path)

def modifyTrackRowWithArtistType(data_dict):
        artistName = data_dict['artist_name']
        trackName = data_dict['track_name']
        albumName = data_dict['album_name']
        artistGenres = data_dict['artist_genres']
        artistTypeIsrael = isIsraeli(trackName, albumName, artistName, artistGenres)
        if artistTypeIsrael == True:
            artistType = 'Israeli'
        else:
            artistType = 'International'
        enrich_dict = {'artist_type': artistType}
        data_dict.update(enrich_dict)
        return data_dict

def modifyDataWithArtistType(file_path):
        data_dict_list = csv_to_dict(file_path)  # list of dicts of rows in csv
        file_name = os.path.basename(file_path)
        print(f'Start MODIFY {file_name} with artist type')

        if os.path.exists(
                os.path.join(MODIFIED_DATA_DIR, file_name)):  # check if file already exists in modifiedData dir
            print("File exists, skipping enrich")
            return

        final_dict_list = []
        for data_dict in data_dict_list:  # each track in the chart
            final_dict_list.append(modifyTrackRowWithArtistType(
                data_dict))  # final_dict_list gets the updated modified dict with the information about the artist type

        full_path = os.path.join(MODIFIED_DATA_DIR, file_name)  # ex. modifiedData/file1.csv
        dict_to_csv(final_dict_list, full_path)
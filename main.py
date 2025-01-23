import argparse
import os
import time

from ChartsAPI.charts import download_spotify_csv_with_login
from TrackEnricher.enricher import enrichData, enrichDataWithArtistType, modifyDataWithArtistType
from utils.consts import DOWNLOAD_DIR, DATA_DIR, ENRICHED_DATA_DIR
from utils.utils import getCredentials, generate_weekly_dates


def runChartsFetcher():
    # Example usage
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Get Creds
    creds_dict = getCredentials()

    # Get Dates
    start = "2022-01-06"
    end = "2024-12-26"
    weekly_dates = generate_weekly_dates(start, end)
    print(f"Number of weeks to download {len(weekly_dates)}")

    for week in weekly_dates:
        print(f'Start download flow for week {week}')
        if os.path.exists(os.path.join(DOWNLOAD_DIR, f'regional-il-weekly-{week}.csv')):
            print("File exists, skipping download")
            continue

        download_spotify_csv_with_login(
            download_dir=DOWNLOAD_DIR,
            username=creds_dict['username'],
            password=creds_dict['password'],
            region="il",
            date=week
        )

def runEnricher():
    # Get Creds
    creds_dict = getCredentials()

    for entry in os.listdir(DOWNLOAD_DIR): # list of files in downloads dir (each chart)
        full_path = os.path.join(DOWNLOAD_DIR, entry) # ex. downloads/file1.csv
        enrichData(creds_dict['client_id'], creds_dict['client_secret'], full_path)

    print('Finished Enriching all charts')

def runEnrichArtistType():
    for entry in os.listdir(DATA_DIR): # list of files in data dir (each enriched chart)
        full_path = os.path.join(DATA_DIR, entry) # ex. data/file1.csv
        enrichDataWithArtistType(full_path)

    print('Finished Enriching all charts with the artist type')

def runModifyArtistType():
    for entry in os.listdir(ENRICHED_DATA_DIR): # list of files in data dir (each enriched chart with the artist type)
        full_path = os.path.join(ENRICHED_DATA_DIR, entry) # ex. enrichedData/file1.csv
        modifyDataWithArtistType(full_path)

    print('Finished MODIFY all charts with the artist type')

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Run fetcher methods")

    # Add an argument that can be either "start" or "stop"
    parser.add_argument(
        "--action",
        choices=["download", "enrich", "enrichArtistType", "modifyArtistType"],
        help="The action to perform"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Run the corresponding function
    if args.action == "download":
        runChartsFetcher()

    elif args.action == "enrich":
        runEnricher()

    elif args.action == "enrichArtistType":
        runEnrichArtistType()

    elif args.action == "modifyArtistType":
        runModifyArtistType()


if __name__ == "__main__":
    main()
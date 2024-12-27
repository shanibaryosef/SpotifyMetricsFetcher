import argparse
import os

from ChartsAPI.charts import download_spotify_csv_with_login
from utils.consts import DOWNLOAD_DIR
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


def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Run fetcher methods")

    # Add an argument that can be either "start" or "stop"
    parser.add_argument(
        "--action",
        choices=["download_charts"],
        help="The action to perform"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Run the corresponding function
    if args.action == "download_charts":
        runChartsFetcher()


if __name__ == "__main__":
    main()
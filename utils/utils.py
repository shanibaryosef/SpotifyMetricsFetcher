import json
import time
import random
from datetime import datetime, timedelta

from utils.consts import CREDS_FILE


def randomSleep(min=1, max=20):
    sleepTime = random.randint(min, max)
    print(f"Sleeping for {sleepTime}")
    time.sleep(sleepTime)

def getCredentials():
    with open(CREDS_FILE, 'r') as file:
        data_dict = json.load(file)

    return data_dict

def generate_weekly_dates(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

    dates = []
    current_date = start_date

    while current_date <= end_date:
        dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(weeks=1)  # Move forward by one week

    print(dates)
    return dates


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import pickle

from utils.utils import randomSleep


def save_cookies(driver, file_path):
    """Save cookies from the current domain to a file."""
    cookies = driver.get_cookies()
    with open(file_path, "wb") as file:
        pickle.dump(cookies, file)
    print(f"Cookies saved to {file_path}")


def load_cookies(driver, file_path):
    """Load cookies from a file, ensuring they match the current domain."""
    with open(file_path, "rb") as file:
        cookies = pickle.load(file)
    current_domain = driver.current_url.split("//")[1].split("/")[0]  # Extract domain from current URL
    for cookie in cookies:
        # Only add cookies that match the current domain
        if "domain" in cookie and cookie["domain"] in current_domain:
            driver.add_cookie(cookie)
        elif "domain" not in cookie:
            driver.add_cookie(cookie)
    print(f"Cookies loaded from {file_path}")

def login_to_spotify(driver, username, password):
    """
    Automates logging into Spotify.

    Args:
        driver (webdriver): Selenium WebDriver instance.
        username (str): Spotify username or email.
        password (str): Spotify password.
    """
    # Open Spotify Login page
    login_url = "https://accounts.spotify.com/en/login"
    driver.get(login_url)

    # Wait for the login fields to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "login-username")))

    # Enter credentials
    driver.find_element(By.ID, "login-username").send_keys(username)
    driver.find_element(By.ID, "login-password").send_keys(password)

    # Click the login button
    driver.find_element(By.ID, "login-button").click()

    # Wait for the user to be redirected after login
    time.sleep(5)
    print("Logged in to Spotify successfully.")


def download_spotify_csv_with_login(download_dir, username, password, date, region="il"):
    """
    Automates Spotify login and downloads the CSV file from Spotify Charts.

    Args:
        download_dir (str): Path to the directory where the CSV file will be saved.
        username (str): Spotify username or email.
        password (str): Spotify password.
        region (str): Region for the chart (default: 'israel').
        date (str): Date for the chart. Use 'latest' for the most recent data.
    """
    # Spotify Charts URL
    url = f"https://charts.spotify.com/charts/view/regional-{region}-weekly/{date}"
    print(f"Loading URL: {url}")

    # Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    prefs = {
        "download.default_directory": os.path.abspath(download_dir),
        "download.prompt_for_download": False,
        "directory_upgrade": True,
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Start WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Load cookies if available
        cookies_file = "../spotify_cookies.pkl"
        driver.get("https://charts.spotify.com")
        try:
            load_cookies(driver, cookies_file)
            driver.refresh()  # Refresh after loading cookies
        except FileNotFoundError:
            print("Cookies not found. Logging in manually...")

            # Log in manually
            login_to_spotify(driver, username, password)
            save_cookies(driver, cookies_file)

        # Navigate to the Spotify Charts URL
        driver.get(url)
        randomSleep(5, 10)
        # Wait for the "Download data as CSV" button to be clickable
        wait = WebDriverWait(driver, 15)
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-labelledby='csv_download']")))

        # Click the download button
        download_button.click()
        print("Download button clicked. Waiting for file to download...")

        # Wait for download
        randomSleep(10,20)

        # Verify download
        files = os.listdir(download_dir)
        csv_files = [f for f in files if f.endswith(".csv")]
        if csv_files:
            downloaded_file = os.path.join(download_dir, csv_files[0])
            print(f"File downloaded successfully: {downloaded_file}")
            return downloaded_file
        else:
            print("No CSV file found in the download directory.")
            return None

    finally:
        driver.quit()

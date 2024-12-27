import requests
import json

# Replace with your valid access token
access_token = "BQCAAMAXMt0jRm7fSPb-3oP_epoIKj25fUQ_71v43gyIzICOrgzgqQzglmmHh2q6E-UZ1LYKr_f0_luQQuFCgv6oOBigdtrf09x_rPRsZu2lN66ZCmg"
# Use Spotify API's proper endpoint for artist details
url = "https://api.spotify.com/v1/artists/1IAEef07H0fd9aA8aUHUlL"
headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    # Parse the response content as JSON
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Error: {response.status_code}")

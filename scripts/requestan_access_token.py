import requests
import base64

client_id = 'a4d37735508d4cab8c520059ff5ee84e'
client_secret = '11a59739203344e3ad53fc5da0ab7dad'

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
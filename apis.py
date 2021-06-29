import requests
import spotipy

CLIENT_ID = "c4820cbbfb4b4bf68e69962fd1648da4"
CLIENT_SECRET = "968c1ca80cc148e9b29310afab75300e"

AUTH_URL = "https://accounts.spotify.com/api/token"

auth_response = requests.post(AUTH_URL, {
  'grant_type': 'client_credentials',
  'client_id': CLIENT_ID,
  'client_secret': CLIENT_SECRET,
})
print(auth_response.status_code)
auth_response_data = auth_response.json()
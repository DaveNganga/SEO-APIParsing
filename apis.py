import requests
import spotipy
import json 

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
access_token = auth_response_data['access_token']

#Try and get information on a specific song: Sacrifices - dreamville

track_id = '7wTA0NKIm6T7nP2kaymU2a?si=55326fdadbb74623'
track_Id = '844fefa17b9f438a'
BASE_URL = 'https://api.spotify.com/v1/'
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = r.json()
print(r)


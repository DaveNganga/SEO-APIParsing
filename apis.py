import requests
import spotipy
import pandas as pd
import sqlalchemy 
from sqlalchemy import create_engine

CLIENT_ID = "c4820cbbfb4b4bf68e69962fd1648da4"
CLIENT_SECRET = "968c1ca80cc148e9b29310afab75300e"

AUTH_URL = "https://accounts.spotify.com/api/token"

auth_response = requests.post(AUTH_URL, {
  'grant_type': 'client_credentials',
  'client_id': CLIENT_ID,
  'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

#Try and get information on a specific song: Sacrifices - dreamville

track_id = '7wTA0NKIm6T7nP2kaymU2a?si=55326fdadbb74623'
BASE_URL = 'https://api.spotify.com/v1/'
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

data = r.json()

#print(data)
#print(key for key in data)

information_data_frame = pd.DataFrame.from_dict([data], orient = 'columns')

print(information_data_frame)

engine = create_engine('mysql://root:codio@localhost/music')

information_data_frame.to_sql('SongInformation', con=engine, if_exists='replace', index=False)
import requests
import spotipy
import pandas as pd
import sqlalchemy 
from sqlalchemy import create_engine


#Function to initiate communication with the spotify API
def spotipy_client():
    CLIENT_ID = "c4820cbbfb4b4bf68e69962fd1648da4"
    CLIENT_SECRET = "968c1ca80cc148e9b29310afab75300e"

    AUTH_URL = "https://accounts.spotify.com/api/token"

    auth_response = requests.post(AUTH_URL, {
      'grant_type': 'client_credentials',
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET })
    print('The authentication response: ', auth_response)
    return auth_response

#Functino that shifts through the response and findes the access token
def response_to_accesstoken(response):
    auth_response_data = response.json()
    access_token = auth_response_data['access_token']
    print('The access token: ', access_token)
    return access_token

#Function to Try and get information on a specific song: Sacrifices - dreamville
def track_information(access_token):
    track_id = '7wTA0NKIm6T7nP2kaymU2a?si=55326fdadbb74623'
    BASE_URL = 'https://api.spotify.com/v1/'
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    data = r.json()
    print('The raw data: ', data)
    return data
  
#Function to insert this ifomration into a local sql database
def data_to_sql(data):
    information_data_frame = pd.DataFrame.from_dict([data], orient = 'columns')
    print(information_data_frame)
    engine = create_engine('mysql://root:codio@localhost/music')
    information_data_frame.to_sql('SongInformation', con=engine, if_exists='replace', index=False)
    

def main():
    #A main function to call all the units together
    Auth_Response = spotipy_client()
    Access_Token = response_to_accesstoken(Auth_Response)
    Track_Information = track_information(Access_Token)
    data_to_sql(Track_Information)
    
    if __name__ == '__main__':
        main()

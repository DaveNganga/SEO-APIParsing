import random
import requests
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine


# Function to initiate communication with the spotify API
def spotipy_client():
    CLIENT_ID = ""
    CLIENT_SECRET = ""

    AUTH_URL = "https://accounts.spotify.com/api/token"

    auth_response = requests.post(AUTH_URL, {
      'grant_type': 'client_credentials',
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET
    })
    print('The authentication response: ', auth_response)
    return auth_response


# Functino that shifts through the response and findes the access token
def response_to_accesstoken(response):
    auth_response_data = response.json()
    access_token = auth_response_data['access_token']
    print('The access token: ', access_token)
    return access_token


# Function get information on a specific song: Sacrifices - dreamville
def track_information(access_token):
    track_id = '7wTA0NKIm6T7nP2kaymU2a' # Sacrifices - dreamville
    track_id_two = '0u7qg774VdGANjp5f4uRNv' # Niko Sawa - Sauti Sol
    track_id_three = '2Rh2RQOFkjqdyIFVzgdmfH' # Festival minor - Gerry M Sextet
    BASE_URL = 'https://api.spotify.com/v1/'
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    r2 = requests.get(BASE_URL + 'audio-features/' + track_id_two, headers=headers)
    r3 = requests.get(BASE_URL + 'audio-features/' + track_id_three, headers=headers)
    
    data = r.json()
    data2 = r2.json()
    data3 = r3.json()
    for column in ['uri','track_href','analysis_url']:
        data.pop(column)
        data2.pop(column)
        data3.pop(column)

    print('The raw data: ', data, data2, data3)
    return [data, data2, data3]


# Function to insert this ifomration into a local sql database
def data_to_sql(data):
    for data_object in data:
        information_data_frame = pd.DataFrame.from_dict([data_object], orient='columns')
        print(information_data_frame)
        engine = create_engine('mysql://root:codio@localhost/music')
        information_data_frame.to_sql('SongInformation', con=engine,
                                      if_exists='append', index=False)
        
def data_to_visualization(data):
    temp = 0 
    global name_list
    name_list = ['Sacrifices - Dreamville','Niko Sawa - Sauti Sol','Festivel Minor - Gerry M Sextet']
    for data_object in data:
        ypoints = []
        xpoints = []
        for key, value in data_object.items():
            if key in ('danceability','energy','loudness','tempo'):
                ypoints.append(value)
                xpoints.append(key)
                yplotpoints = np.array(ypoints)
                xplotpoints = np.array(xpoints)
            
        #plt.plot(data_object['key'], data_object.items())
        plt.title('comparing songs')
        plt.plot(xplotpoints,yplotpoints,
                 color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)), 
                 label=name_list[temp])
        plt.legend(loc="best")
        temp+=1
        
    plt.show()  


    # Main function to call all the units together
if __name__ == '__main__':
    Auth_Response = spotipy_client()
    Access_Token = response_to_accesstoken(Auth_Response)
    Track_Information = track_information(Access_Token)
    #data_to_sql(Track_Information)
    data_to_visualization(Track_Information)


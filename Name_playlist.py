import requests
import base64
import os

def get_playlist_tracks(playlist_url, access_token):
    # Get the playlist ID from the URL
    playlist_id = playlist_url.split('/')[-1].split('?')[0]

    # Set up the headers for the request
    headers = {'Authorization': f'Bearer {access_token}'}

    # Make the request to the Spotify API
    response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=headers)

    # Parse the response JSON to get the track names
    data = response.json()
    song_names = [f"{track['track']['name']} - {track['track']['artists'][0]['name']}" for track in data['items']]


    return song_names

if __name__ == '__main__':
    # asking the user to enter the playlist URL
    playlist_url = input('Enter the URL of the Spotify playlist: ')

    # Get the access token from the Spotify API
    #your client id and client secret can be found on Spotify
    client_id = 'your_clien_it'
    client_secret = 'your_client_secret'
    base64_auth = base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
    headers = {'Authorization': f'Basic {base64_auth}'}
    payload = {'grant_type': 'client_credentials'}
    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=payload)
    data = response.json()
    access_token = data['access_token']

    # Get the track names from the playlist
    song_names = get_playlist_tracks(playlist_url, access_token)

    # Write the track names to a text file
    with open('playlist.txt', 'w') as file:
        for song_name in song_names:
            file.write(song_name + '\n')

    # Print a message to indicate that the operation is complete
    print(f'The playlist has been saved to {os.getcwd()}/playlist.txt')

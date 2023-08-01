import yt_dlp
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#function to download youtube songs
def download_music(song_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{song_name}", download=True)['entries'][0]
            print(f"Downloaded: {info['title']}")
        except Exception as e:
            print(f"Error: {e}")
#functtion to extract song name from playlist
def get_playlist_tracks(playlist_id):
    client_credentials_manager = SpotifyClientCredentials(client_id='cleint id here', client_secret='client secret here')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    try:
        results = sp.playlist_tracks(playlist_id)
        return [track['track']['name'] for track in results['items']]
    except Exception as e:
        print(f"Error: {e}")
        return []

def main():
    songs = []
    playlist_id = input('Enter playlist ID: ')
    song_names = get_playlist_tracks(playlist_id)

    if song_names:
        print("Songs in the playlist:")
        for index, song_name in enumerate(song_names, start=1):
            songs.append(song_name)
    else:
        print("No songs found in the playlist.")
    
    for i in songs:
        print(i)
        download_music(i)

if __name__ == "__main__":
    main()

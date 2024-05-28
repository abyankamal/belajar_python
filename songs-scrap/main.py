# from bs4 import BeautifulSoup
# import requests

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "ecc3c09ce95a4835a2a2b296f1ca88de"
CLIENT_SECRET = "19f147463496443baf8b1ef606a6a345"
REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        show_dialog=True,
        username="Abyan Kamal",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
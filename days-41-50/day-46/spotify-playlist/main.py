import requests
import logging
import spotipy
import config
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.CRITICAL)

# ------------------- Authentication with Spotify ------------------- #
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=config.client_id,
        client_secret=config.client_secret,
        redirect_uri=config.redirect_uri,
        scope=config.scope,
        show_dialog=True,
        cache_path="token.txt",
        username=config.username
        )
    )

user_id = sp.current_user()["id"]

# ------------------- Scraping the Billboard Hot 100 ------------------- #

date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date_input.split("-")[0]

response = requests.get("https://www.billboard.com/charts/hot-100/" + date_input)

soup = BeautifulSoup(response.text, "html.parser")
song_text = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_text]
artist_text = soup.select("li ul li span")
artist_names = []
for i in range(len(artist_text)):
    if i == 0 or i % 7 == 0:
        artist_names.append(artist_text[i].getText().strip())

logging.debug(song_names)
logging.debug(artist_names)
logging.debug(len(song_names))
logging.debug(len(artist_names))

# ------------------- Searching Spotify for the Songs ------------------- #

song_queries = []
for song in song_names:
    query = sp.search(q=f"track:{song} year:{year}", type="track")
    logging.debug(query)
    try:
        uri = query["tracks"]["items"][0]["uri"]
        song_queries.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
# ------------------- Creating a new private playlist in Spotify ------------------- #

playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
logging.debug(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_queries)



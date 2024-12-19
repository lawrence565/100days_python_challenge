import requests, dotenv, os, spotipy, json
from datetime import datetime
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

dotenv.load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
with open("token.txt") as file:
    content = json.loads(file.read())
TOKEN = content["access_token"]

def get_date():
    date_format = "%Y-%m-%d"

    while True:
        date_string = input("What year you would like to travel to? (YYYY-MM-DD): ")
        if len(date_string.split("-")) == 3:
            try:
                valid_date = datetime.strptime(date_string, date_format)
                start_date = datetime.strptime("1958-08-03", date_format)
                if valid_date > start_date:
                    return date_string
                else:
                    print(f"The date must after 1958-08-04.")
            except ValueError:
                print(f"The date {date} is not valid.")

date = get_date()

# Scrapping data
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
res = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/", headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

# Create list from the result of scrapping
music_list = [music.getText().strip() for music in soup.select("li>#title-of-a-story")]

# Authentication of Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private playlist-modify-public user-library-read",
                                               redirect_uri="https://example.com",
                                               client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               show_dialog=True,
                                               cache_path="token.txt"))

# Get user id
user_id = sp.current_user()["id"]

# Create playlist
data = {
    "name": f"{date} Billboard 100",
    "public": "false",
    "description": f"This a playlist create through billboard 100 website on {date}"
}
headers = {
    "Authorization": f"Bearer {TOKEN}"
}
res = requests.post(f"https://api.spotify.com/v1/users/{user_id}/playlists", json=data, headers=headers)
playlist_id = res.json()["id"]

# Search songs on Spotify
music_uri_list = []
for music in music_list:
    results = sp.search(q=music, limit=1)
    for idx, track in enumerate(results['tracks']['items']):
        music_uri_list.append(track["uri"])

add_result = requests.post(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", json={"uris": music_uri_list}, headers=headers)
add_result.raise_for_status()
print(add_result.json())


# results = sp.search(q="Trash", limit=1)
# print(results)
# for idx, track in enumerate(results['tracks']['items']):
#     print(track["uri"])
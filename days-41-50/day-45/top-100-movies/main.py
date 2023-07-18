import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movie_ranks = soup.find_all(name="span", class_="jsx-1913936986 listicle-item-count")
all_movies = soup.find_all(name="a", rel="noopener")

# Extract rank X from 'X of 100' string 
ranks_text = [rank.getText() for rank in all_movie_ranks]
ranks = [int(rank.split(" ")[0]) for rank in ranks_text]

# Filter list to include only anchor text that start with "Read Empire's review of "
# Then build the movie list by removing the starting anchor text.
string = "Read Empire's review of "
names = []
names_text = [name.getText() for name in all_movies]
for name in names_text:
    if name.startswith(string):
        name = name.replace(string, "")
        names.append(name)
        
# Flip Empire's list order to descending order (1 to 100)
names.reverse()
        
logging.debug(ranks)
logging.debug(names)
assert len(names) == 100

# Print top 100 movies list to text file
with open("movies.txt", mode="w") as file:
    for rank, name in zip(ranks, names):
        file.write(f"{rank}. {name}\n")
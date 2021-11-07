#IMDB Scraper
from requests import get
from bs4 import BeautifulSoup

def imdb(id, seaNum, epsNum):
    # For every season in the series-- range depends on the show
        # Request from the server the content of the web page by using get(), and store the server’s response in the variable response
        response = get('https://www.imdb.com/title/' + id + '/episodes?season=' + seaNum)

        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')
        
        # Select all the episode containers from the season's page
        episode_containers = page_html.find_all('div', class_ = 'info')
        
        # For each episode in each season
        for episodes in episode_containers:
                # Get the info of each episode on the page
                season = seaNum
                episode_number = episodes.meta['content']
                if (episode_number == epsNum):    
                    title = episodes.a['title']
                    airdate = episodes.find('div', class_='airdate').text.strip()
                    rating = episodes.find('span', class_='ipl-rating-star__rating').text
                    desc = episodes.find('div', class_='item_description').text.strip()
                    # Compiling the episode info
                    episode_data = {"season": season, "episodeNumber": episode_number, "title": title, "airdate": airdate, "rating": rating, "desc": desc}
                    #print(episode_data)
                    return episode_data
                else: 
                    continue

if __name__ == "__main__":
    imdb("tt1305826", "5", "10")

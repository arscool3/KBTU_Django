import requests
from bs4 import BeautifulSoup 
from dramatiq.brokers.redis import RedisBroker 
import dramatiq

dramatiq.set_broker(RedisBroker())

@dramatiq.actor
def get_page_title(url):   
    soup = BeautifulSoup(requests.get(url).text, "html.parser")   
    file = open("titles.txt", "a")   
    file.write("\n"+soup.title.text)
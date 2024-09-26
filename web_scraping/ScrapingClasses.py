import requests
import bs4

soup = bs4.BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/Grace_Hopper").text, 'lxml')
print(soup)
print(soup.select('#cite_note-104')[0].text)
print(soup.select('.new')[0])

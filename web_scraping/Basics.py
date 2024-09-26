import requests
import bs4

result = requests.get("https://example.com")
pretty_print = bs4.BeautifulSoup(result.text, 'lxml')
print(pretty_print)
print(pretty_print.select('title')[0].text)
print(pretty_print.select('div > background-color')[0].text)

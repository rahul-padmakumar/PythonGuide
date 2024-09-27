import requests
import bs4

for i in range(1, 51):
    soup = bs4.BeautifulSoup(requests.get('https://books.toscrape.com/catalogue/page-{}.html'.format(i)).text, 'lxml')
    filtered_list = list(filter(lambda value: value.select(".star-rating.Two") != [], soup.select(".product_pod")))


    def mapper(data):
        return data.select('a')[1]['title']


    print(list(map(mapper, filtered_list)))

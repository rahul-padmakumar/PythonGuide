import requests
import bs4

page_no = 1
authors = set()
while True:
    soup = bs4.BeautifulSoup(requests.get("https://quotes.toscrape.com/page/{}/".format(page_no)).text, "lxml")
    authors_om_this_page = set(map(lambda value: value.text, soup.select(".author")))
    authors.update(authors_om_this_page)

    if page_no == 1:
        print(sorted(authors_om_this_page))
        print(list(map(lambda value: value.text, soup.select(".text"))))
        for i in list(map(lambda value: value.text, soup.select(".tag-item"))):
            print(i)

    if not soup.select(".next"):
        break
    else:
        page_no += 1

print(sorted(authors))

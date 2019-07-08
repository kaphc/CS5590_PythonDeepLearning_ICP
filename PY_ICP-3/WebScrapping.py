import urllib.request
from bs4 import BeautifulSoup

# wiki page url
wiki_page_url = 'https://en.wikipedia.org/wiki/Deep_learning'

# open wiki page using urllib library
page = urllib.request.urlopen(wiki_page_url)

# parse the wiki page using beautifulsoup from bs4 library
soup = BeautifulSoup(page, "html.parser")

# print the wiki page's title using soup.title.string
print("TITLE : " + soup.title.string)

# find all the links in the page by finding the anchortag 'a'
atag = soup.findAll('a')

# iterating over each tag and then return their link using its attribute
# "href" using get
for link in atag:
    print(link.get('href'))

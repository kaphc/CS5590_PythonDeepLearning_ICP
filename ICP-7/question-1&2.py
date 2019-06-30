from bs4 import BeautifulSoup
import urllib.request


def create_file():
    file = open('input.txt', 'a+', encoding='utf-8')
    return file


def get_text():
    url = "https://en.wikipedia.org/wiki/Google"
    content = urllib.request.urlopen(url)

    soup = BeautifulSoup(content, "html.parser")

    body = soup.find('div', {'class': 'mw-parser-output'})
    file.write(str(body.text))


if __name__ == '__main__':
    print("Creating text file.....")
    file = create_file()
    get_text()

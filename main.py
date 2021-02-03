from bs4 import BeautifulSoup
import requests


def generate_qas(content):
    
def run():
    url="https://www.binance.com/en/blog"
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    headers = { 'User-Agent' : user_agent, 'Referer' : 'https://structured-data-testing-tool.developers.google.com/sdtt/web?', 'Origin' : 'https://structured-data-testing-tool.developers.google.com' }
    req = requests.get(url, headers=headers)
    req.enconding = 'utf-8'
    data = req.text
    
    blog_urls = list()
    soup = BeautifulSoup(data, "html.parser")
    mydivs = soup.find_all("div", {"class": "title css-4cffwv"})
    for div in mydivs:
        hrefs = div.find_all('a', href=True)
        for a in hrefs:
            blog_urls.append(a['href'])
    
    # iterate through blog posts
    for post in blog_urls:
        #get blog content
        req = requests.get(url, headers=headers)
        req.enconding = 'utf-8'
        data = req.text
        soup = BeautifulSoup(data, "html.parser")
        page = soup.find('p').getText()


if __name__ == '__main__':
    run()
import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                         'AppleWebKit/537.11 (KHTML, like Gecko) '
                         'Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}


class newsscraper():
    def __init__(self, q="coronavirus-covid-19-outbreak"):
        self.q = q
        self.baseurl = "https://www.indiatoday.in"

    def getnews(self):
        results = list()
        finaldict = dict()
        urlm = self.baseurl +"/"+ self.q
        try:
            r = requests.get(urlm, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            newslist = soup.find_all('div', class_='catagory-listing')
            for news in newslist:
                newsl = dict()
                lnk = news.find('a')
                newsl['title'] = lnk.text
                url = lnk['href']
                newsl['news_link'] = self.baseurl + url
                newsl['snippet'] = news.find('p').text
                newsl['image'] = news.find('img')['src']
                results.append(newsl)
        except Exception as e:
            print(str(e))
            return {'error': 'Error :' + str(e)}
        if (len(results) > 1):
            finaldict['results'] = results
            return finaldict
        else:
            return {'error': 'No results'}

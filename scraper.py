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


class covidscraper():
    def __init__(self, state=""):
        self.state = state

    def getdata(self):
        results = list()
        finaldata = dict()
        try:
            req = requests.get("https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India", headers=headers)
            soup = BeautifulSoup(req.content, 'html.parser')
            table_data = soup.find('table', class_='wikitable')
            tblbody = table_data.find('tbody')
            rows = tblbody.find_all('tr')

        except Exception as e:
            print(str(e))
            return {'error': str(e)}
        if self.state.lower().strip() == "":
            all_data = table_data.find('tr', class_='sortbottom').find_all('th')
            infected_all = all_data[1].text.strip()
            deaths_all = all_data[2].text.strip()
            recovered_all = all_data[3].text.strip()
            total_cases = all_data[4].text.strip()
            return {'infected': infected_all, 'deaths': deaths_all, 'recovered': recovered_all,
                    'total_cases': total_cases}
        elif self.state.lower().strip() == "all":

            for element in rows:
                statedict = dict()
                try:
                    statedict['state'] = element.find('th').text.replace("\u2020", '').strip()
                    datas = element.find_all('td')
                    statedict['total'] = datas[3].text.strip()
                    statedict['active'] = datas[0].text.strip()
                    statedict['deaths'] = datas[1].text.strip()
                    statedict['recoveries'] = datas[2].text.strip()
                    results.append(statedict)
                except Exception as e:
                    pass
        elif self.state.lower().strip() != "":
            statedict = dict()
            for element in rows:
                try:
                    if element.find('th').text.replace("\u2020", '').lower().strip() == self.state.lower().strip():
                        statedict['state'] = element.find('th').text.replace("\u2020", '').strip()
                        datas = element.find_all('td')
                        statedict['total'] = datas[3].text.strip()
                        statedict['active'] = datas[0].text.strip()
                        statedict['deaths'] = datas[1].text.strip()
                        statedict['recoveries'] = datas[2].text.strip()
                except Exception as e:
                    pass
            if len(statedict) != 0:
                results.append(statedict)
        if len(results) == 0:
            return {'error': 'No matching results'}
        else:
            finaldata['results'] = results
            return finaldata

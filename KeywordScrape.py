import csv
from bs4 import BeautifulSoup
import requests

urls = ['http://www.hopeindustrial.com/','http://www.makeitdaisy.com', 'https://www.pepperl-fuchs.com/global/en/index.htm', 'http://www.rockwellautomation.com/', 'http://www.swiftprotech.com', '']
cleanurls = []
keywords_dict = []

with open( "--ENTER EMAIL DOMAIN URLS DOC--", 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
for i in your_list:
    urls.append('http://www.'+i[0])

def get_keywords(li):
    for i in li:
        try:
            r = requests.get(i)
            data = r.text.lower()
            soup = BeautifulSoup(data, "lxml")
            try:
                kws = soup.findAll("meta", attrs={"name":"keywords"})
                print(kws[0]['content'])
            except Exception as e:
                print('no kws')
        except Exception as e:
            print("--")
    print()


get_keywords(urls)
print(keywords_dict)

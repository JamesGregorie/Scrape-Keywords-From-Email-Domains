import csv
from bs4 import BeautifulSoup
import requests


urls = ['http://www.hopeindustrial.com','http://www.makeitdaisy.com', 'https://www.pepperl-fuchs.com/global/en/index.htm', 'http://www.rockwellautomation.com/', 'http://www.swiftprotech.com', '']
keywords = []

with open( "emails.csv", 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
for i in your_list:
    urls.append('http://www.'+i[0])

def get_keywords(li):
    for i in li:
        try:
            r = requests.get(i)
            data = r.text.lower()
            soup = BeautifulSoup(data, "html.parser")
            kws = soup.findAll("meta", attrs={"name":"keywords"})
            words = kws[0]['content'].split(", ")
            for i in words:
                keywords.append(i)
        except Exception as e:
            pass
get_keywords(urls)
print(keywords)

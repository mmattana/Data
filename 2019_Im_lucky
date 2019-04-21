import requests
import webbrowser
import re
from bs4 import BeautifulSoup

search = input()
url = "https://www.google.com/search?q=" + search
response = requests.get(url)
if response.status_code == 200:
    print("Success")
else:
    print("Failure")

soup = BeautifulSoup(response.content,'lxml')
responses = soup.select('.r')
for item in responses:
    #print(str(item))
    search = re.search(r"https://.+;sa",str(item))
    try:
        webbrowser.open(search.group()[:-7])
    except Exception:
        pass

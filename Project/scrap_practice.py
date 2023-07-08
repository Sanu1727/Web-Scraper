
import requests as re
from bs4 import BeautifulSoup
URL = "https://www.kaggle.com"
response = re.get(URL)

print("response -->",response, "\ntype -->",type(response))

print("text -->",response.text, "\ncontent -->",response.content, "\nstatus_code -->",response.status_code)

if response.status_code !=200:
    print("HTTP connection is not succesful")
else:
    print("HTTP connection is sucessful")

soup = BeautifulSoup(response.content,"html.parser")

print("Title with tags -->", soup.title,"\ntitle without tags -->",soup.title.text)

for link in soup.find_all("link"):
    print(link.get("href"))

print(soup.get_text())
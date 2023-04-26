import requests as req
import json
from pathlib import Path
from json import JSONEncoder
from bs4 import BeautifulSoup

url = "https://useme.com/pl/roles/contractor/soplica-software-solutions,257025/"
dir_path = Path("C:/Users/rogoz/OneDrive/Pulpit/useme_crawler")
file_name = 'reviews.json'
file_path = dir_path.joinpath(file_name)

class Review:
  def __init__(self, username, text, date, rtype):
    self.username = username
    self.text = text
    self.date = date
    self.rtype = rtype

class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

def getData():
    res = req.get(url)
    soup  = BeautifulSoup(res.text, "html.parser")
    names = soup.find_all(class_ = "portrait__name")
    texts = soup.find_all(class_ = "opinion-content-text")
    dates = soup.find_all(class_ = "portrait__date")
    rtypes = soup.find_all(class_ = "opinion-type-label")

    reviews = [];

    for i in range(len(names)):
        reviews.append(Review(names[i].text, texts[i].text.strip(), dates[i].text, rtypes[i].text.strip())) 

    for x in reviews:
       print(x.rtype)
    return reviews


with open(file_path,'w') as my_file:
    json.dump(MyEncoder().encode(getData()), my_file)



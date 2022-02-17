from array import array
import requests
import csv
from bs4 import BeautifulSoup

# Website to crawl
url = "https://news.ycombinator.com/"

# Execute GET-Request
response = requests.get(url)

# Analyze HTML file syntax using BeautifulSoup 
html = BeautifulSoup(response.text, 'html.parser')

#Get order
orders = html.find_all("span", {"class": "rank"}) #orden

#Get titles
titles = html.find_all("a", {"class": "titlelink"}) #titles

#Get only number of points
points = [0]*30
scores = html.find_all("span", {"class": "score"}) #points
i = 0
for score in scores: 
    text_comm = score.string
    #print(i)
    #print(text_comm)
    numbers = [int(s) for s in text_comm.split() if s.isdigit()]
    if (len(numbers)!=0):
        #print(numbers[0])
        points[i]=numbers[0]
        i+=1

#Get only number of comments
comments = [0]*30
trs = html.find_all(class_="athing") #ids
i=0
for tr in trs :
    n_com1 = html.find_all("a", {"href": "item?id="+tr.get('id')})
    text_comm = n_com1[1].string
    numbers = [int(s) for s in text_comm.split() if s.isdigit()]
    if (len(numbers)!=0):
        comments[i]=numbers[0]
        i+=1

for i in range(30): 
    print(orders[i].string)
    print(titles[i].string)
    print(points[i])
    print(comments[i])


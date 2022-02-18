from array import array
import requests
import csv
from bs4 import BeautifulSoup

def printresults(entries):
    for i in range(len(entries)):
        print(entries[i][0]+" "+entries[i][1]+". Points:"+str(entries[i][2])+ ". Comments: "+str(entries[i][3]))
    print("")
    
def main():
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
        numbers = [int(s) for s in text_comm.split() if s.isdigit()]
        #To check if the string score.string was not empty
        if (len(numbers)!=0):
            points[i]=numbers[0]
            i+=1

    #Get only number of comments
    comments = [0]*30
    trs = html.find_all(class_="athing") #ids
    i=0
    for tr in trs :
        #There are several href labels inside each tr
        n_com = html.find_all("a", {"href": "item?id="+tr.get('id')})
        #To select only the href label with the comments
        for j in range(len(n_com)):
            if ("comment" in n_com[j].string):
                text_comm = n_com[j].string
                break
            else:
                text_comm="0"
        numbers = [int(s) for s in text_comm.split() if s.isdigit()]
        comments[i]=numbers[0]
        i+=1

    #Constructing a list of entries
    entries =[]
    for i in range(30):
        entry = (orders[i].string, titles[i].string, points[i], comments[i])
        entries.append(entry)
        
    #Entries with more than five words in the title ordered by the number of comments first.
    entry_set_A = list(filter(lambda n:len(n[1].split())>5,entries))
    entry_set_A.sort(key=lambda x:x[3])
    print("Entries with more than five words in the title ordered by the number of comments first")
    printresults(entry_set_A)

    #Entries with less than or equal to five words in the title ordered by points.
    entry_set_B = list(filter(lambda n:len(n[1].split())<=5,entries))
    entry_set_B.sort(key=lambda x:x[2])
    print("Entries with less than or equal to five words in the title ordered by points.")
    printresults(entry_set_B)

main()

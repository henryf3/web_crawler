# Importar módulos
import requests
import csv
from bs4 import BeautifulSoup

# Dirección de la página web a scrapear
url = "https://news.ycombinator.com/"
# Ejecutar GET-Request
response = requests.get(url)
# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')
news = html.find_all("score")
scores = html.find_all("span", {"class": "score"})
for score in scores:
    print(score.string)



#print(news)
# i=0
# while(i<30):
#     print(html.title)
#     i+=1



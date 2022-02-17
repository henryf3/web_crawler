# Importar módulos
import requests
import csv
from bs4 import BeautifulSoup

# Dirección de la página web
url = "http://quotes.toscrape.com/"
# Ejecutar GET-Request
response = requests.get(url)
# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')

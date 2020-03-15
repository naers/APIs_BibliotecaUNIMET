import scrapy
from bs4 import BeautifulSoup
import requests


class Spider(scrapy.Spider):
    name = "mapo"
    #allowed_domains = ["example.com"]
    start_urls = (
        'http://andromeda.unimet.edu.ve/catalogo/php1/buscar.php?xx=9999&base=mapo&cipar=mapo.par&Expresion=($)&Opcion=detalle&Formato=a&from=&to=',
   )

    def parse(self, response):
        url = "http://andromeda.unimet.edu.ve/catalogo/php1/buscar.php?xx=9999&base=mapo&cipar=mapo.par&Expresion=($)&Opcion=detalle&Formato=a&from=&to="
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        x = soup.find_all(['b','a'])
        for tag in x:
            var = tag.text.strip()
            yield {
               # "url": response.url,
                 '':var
                }

    
import scrapy
from bs4 import BeautifulSoup
import requests


class Spider(scrapy.Spider):
    name = "bibliografica"
    #allowed_domains = ["example.com"]
    start_urls = (
        'http://andromeda.unimet.edu.ve/catalogo/php1/buscar.php?xx=9999&base=marc&cipar=marc.par&Expresion=(romero/(100)*anibal/(100))&Opcion=detalle&Formato=a&from=&to=',
   )

    def parse(self, response):
        url = "http://andromeda.unimet.edu.ve/catalogo/php1/buscar.php?xx=9999&base=marc&cipar=marc.par&Expresion=(romero/(100)*anibal/(100))&Opcion=detalle&Formato=a&from=&to="
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        x = soup.find_all(['b','a'])
        for tag in x:
            var = tag.text.strip()
            yield {
               # "url": response.url,
                 '':var
                }
               
              

        





# APIs_BibliotecaUNIMET
En esta carpeta se podra encontrar el código para utilizar los APIs del catálogo de la Biblioteca Pedros Grases de la Universidad Metropolitana 

Esta guía pretende ser de uso para aquellas personas que deseen modificar el código fuente del API, para mejoras y ampliaciones.

Cada una de las carpetas representa el API de los catálogos Bibliografica, Trabajos de Grado y Mapoteca, siendo este último un API adiciona creado.

*Dentro de cada una de las carpetas, solo hace falta editar el archivo con extensión .py  que se encuentra dentro de la carpeta SPIDERS, ya que los demás archivos son autogenerados o no hace falta modificación alguna.*

**El archivo _init_.py no se modifica, solo el otro**

##Código

Dentro del codigo podemos ver como se crea una clase Spider, a la cual se le da un nombre. Tambien podemos ver la variable *start_urls*, en la cuál
se ingresa el URL de búsqueda del sitio web Andrómeda.

```
class Spider(scrapy.Spider):
    name = "bibliografica"
    #allowed_domains = ["example.com"]
    start_urls = (
        'http://andromeda.unimet.edu.ve/catalogo/php1/buscar.php?xx=9999&base=marc&cipar=marc.par&Expresion=(romero/(100)*anibal/(100))&Opcion=detalle&Formato=a&from=&to=',
   )
```

Este URL es un poco largo, pero presenta ciertas partes que pueden modificarse para obtener una búsqueda más específica.

**base=marc&cipar=marc**

En esta parte del URL, la palabra MARC significa que se está accediendo al catálogo de Bibliográfica. Si se desea acceder a algún otro,
se cambia por los siguientes:

  - marc:       Bibliográfica
  - CENDI:    CENDIF
  - ARTUS:   Arturo Uslar Pietri
  - ramvel:    Ramón J. Velásquez
  - RAROS:  Raros y curiosos
  - tesis:       Trabajos de Grado
  - tesdoc:    Tesis Doctorales
  - ACUER:  Acuerdos y Tratados Unimet
  - PSER:     Revistas
  - VTECA:   Videoteca
  - MAPO:    Mapoteca
  - PTECA:  PINACOTECA
  - fotog:      Fototeca
  - info:  INFOEM


**Expresion=(romero/(100)*anibal/(100))**

En la siguiente parte del URL, más específicamente la que se encuentra dentro del paréntesis, es donde se escriben las palabras claves
que se desean buscar. El número 100 representa una búsqueda por **Autor**, el 245 por **Título** y 650 por **Materia**. Entonces se
reemplaza ese número por lo que se quiera buscar, y del lado izquiero se coloca la palabra clave. Por ejemplo:

**Expresion=(democracia/(245))**

##Conclusiones

Estas son las únicas partes del código y del URL que hacen falta editar para modificar el API y los catálogos a los que accede.

Espero esta guía sea de ayuda para la modificación, mejoras y ampliación de las APIs. Para un mejor entendimiento del código,
recomendamos revisar la documentación de Python y sus librerías Scrapy, BeautifulSoup4 y Scrapyrt.

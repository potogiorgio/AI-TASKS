# Extracción y Análisis de Texto de Artículos Científicos

# Zenodo
[![DOI](https://zenodo.org/badge/1175971540.svg)](https://doi.org/10.5281/zenodo.18937913)

## Dataset
El dataset está compuesto por 10 artículos científicos de acceso abierto obtenidos de arXiv.

## Herramientas a seguir
El flujo de trabajo del proyecto es el siguiente:

1. Descargar artículos en formato PDF desde arXiv.

2. Procesar los PDFs utilizando Grobid con la opción Process Fulltext Document.

3. Obtener los archivos XML en formato TEI.

4. Analizar los XML mediante scripts en Python.

5. Generar los resultados del análisis.

# Estructura

docs/ -> carpeta con los docs necesarios para conectar Github con ReadtheDocs.

dataset/ -> papers.

extracted_text/ -> xml de los PDFs.

scripts/ -> scripts de python (el archivo runner.py es un script de python para runnear todos desde docker).

results/ -> ficheros de resultados de los scripts de python.

test/ -> test de los scripts que pasan en github al hacer un commit.

# Enviroment set up
En vuestro CMD:

python -m venv venv 

source venv/bin/activate 

# Instalacion de dependencias

 pip install -r requirements.txt

 # Probar los scripts
 Desde la raiz poner los siguientes comandos:

 python scripts/keyword_cloud.py

python scripts/figures.py

python scripts/links.py

 # Test
 Los test del proyecto estan implementados usando pytest

 pytest

 # Ejecución con Docker

docker build -t imagen .

docker run imagen

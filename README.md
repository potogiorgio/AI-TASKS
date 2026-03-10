# Text Extraction and Analysis

# Zenodo conexion
https://doi.org/10.5281/zenodo.18937914

## Dataset
10 datasets de Arxiv

## Herramientas a seguir
1. PDFs de Arxiv
2. Analizarlos con Grobid con TEI y Process Fulltext Document
3. Sacar los xml
4. Analizarlos con Python y obtener los distintos resultados

## Estructura

dataset/ → papers
extracted_text/ → xml de los PDFs  
scripts/ → scripts de python
results/ → ficheros de resultados

# Enviroment set up

python -m venv venv 
source venv/bin/activate 

# Instalacion de dependencias

 pip install -r requirements.txt

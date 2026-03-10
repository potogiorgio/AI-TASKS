import os
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
xml_folder = os.path.join(base_dir, "extracted_text")
abstract_text = ""

for file in os.listdir(xml_folder):
    if file.endswith(".xml"):
        path = os.path.join(xml_folder, file)

        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "xml")

            abstract = soup.find("abstract")
            if abstract:
                abstract_text += abstract.get_text() + " "

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(abstract_text)

plt.figure()
plt.imshow(wordcloud)
plt.axis("off")

os.makedirs("results", exist_ok=True)

plt.savefig("results/keyword_cloud.png")
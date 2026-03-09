import os
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

xml_folder = "../extracted_text"

papers = []
figures_count = []

for file in os.listdir(xml_folder):
    if file.endswith(".xml"):
        path = os.path.join(xml_folder, file)

        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "xml")

            figures = soup.find_all("figure")

            papers.append(file)
            figures_count.append(len(figures))

plt.figure()
plt.bar(papers, figures_count)

plt.xticks(rotation=45)
plt.ylabel("Number of figures")
plt.xlabel("Articles")

plt.tight_layout()

plt.savefig("../results/figures_per_article.png")
plt.show()
import os
from bs4 import BeautifulSoup

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
xml_folder = os.path.join(base_dir, "extracted_text")

os.makedirs("results", exist_ok=True)
output_file = "results/links.txt"

with open(output_file, "w", encoding="utf-8") as out:

    for file in os.listdir(xml_folder):
        if file.endswith(".xml"):
            path = os.path.join(xml_folder, file)

            with open(path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "xml")

                out.write(f"\n{file}\n")

                refs = soup.find_all(["ref", "ptr"])

                for r in refs:
                    link = r.get("target")
                    if link and "http" in link:
                        out.write(link + "\n")

                        
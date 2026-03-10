from bs4 import BeautifulSoup

# Test 1

def extract_abstract(xml):
    soup = BeautifulSoup(xml, "xml")
    abstract = soup.find("abstract")
    if abstract:
        return abstract.get_text().strip()
    return None


def test_extract_abstract():
    xml = """
    <TEI>
        <profileDesc>
            <abstract>
                <p>This is a test abstract.</p>
            </abstract>
        </profileDesc>
    </TEI>
    """

    result = extract_abstract(xml)

    assert result == "This is a test abstract."

# Test 2

def count_figures(xml):
    soup = BeautifulSoup(xml, "xml")
    figures = soup.find_all("figure")
    return len(figures)


def test_count_figures():
    xml = """
    <text>
        <figure></figure>
        <figure></figure>
        <figure></figure>
    </text>
    """

    result = count_figures(xml)

    assert result == 3


# Test 3
def extract_links(xml):
    soup = BeautifulSoup(xml, "xml")

    links = []
    refs = soup.find_all(["ref", "ptr"])

    for r in refs:
        link = r.get("target")
        if link:
            links.append(link)

    return links


def test_extract_links():
    xml = """
    <text>
        <ref target="https://github.com/project"/>
        <ref target="https://dataset.org"/>
    </text>
    """

    result = extract_links(xml)

    assert "https://github.com/project" in result
    assert "https://dataset.org" in result
    assert len(result) == 2
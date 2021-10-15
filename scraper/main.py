from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
import requests
import asyncio
from bs4 import BeautifulSoup
from typing import List


def extract_urls(company: str) -> List[str]:
    doc = Document(f"Sustainability_Reports/{company}/{company}.docx")
    rels = doc.part.rels
    # yes you have to index back into rels, otherwise you only get a string
    # split on "?" to avoid queries so that set can filter out duplicates
    # docx's API is confusing.
    links = set(
        rels[r]._target.split("?")[0] for r in rels if rels[r].reltype == RT.HYPERLINK
    )
    # pdfs are harder to manage...
    return [l for l in links if not l.endswith(".pdf")]


async def fetch_html(links: List[str]):
    # speed optimization
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(None, requests.get, link) for link in links]
    responses = list(await asyncio.gather(*futures))

    return [r.text for r in responses if r.status_code == 200]


async def extract_news_articles(company: str) -> List[str]:
    links = extract_urls(company)
    htmls = await fetch_html(links)
    texts = []
    for html in htmls:
        # credit to https://stackoverflow.com/a/24618186
        soup = BeautifulSoup(html, "html.parser")

        for script in soup(["script", "style", "header", "footer"]):
            script.extract()

        # remove unrelated stuff, maybe
        m = soup.find("main")
        text = m.get_text() if m is not None else soup.get_text()

        if a := soup.find("article"):
            at = a.get_text()
            if len(at) < len(text):
                text = at

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = "\n".join(chunk for chunk in chunks if chunk)

        texts.append(text)

    return texts


async def main():
    t = await extract_news_articles("Apple")
    print(t)


if __name__ == "__main__":
    asyncio.run(main())

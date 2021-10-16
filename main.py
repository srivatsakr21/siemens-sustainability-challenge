from scraper import extract_news_articles
import asyncio
import os

async def main():
    with open("reports.csv", "w") as f:
        f.write("company, news\n")
        for company in os.listdir("Sustainability_Reports"):
            if company == ".DS_Store":
                continue
            print(f"Company: {company}")
            t = await extract_news_articles(company)
            for a in t:
                f.write(f"\"{company}\", \"{a}\"\n")
            print(len(t))
    
        


if __name__ == "__main__":
    asyncio.run(main())

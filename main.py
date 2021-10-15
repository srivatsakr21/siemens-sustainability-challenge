from scraper import extract_news_articles
import asyncio

async def main():
    t = await extract_news_articles("Apple")
    print(t)


if __name__ == "__main__":
    asyncio.run(main())

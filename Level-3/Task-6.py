import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    print("\nFetching data from Quotes Website...")
    url = "http://quotes.toscrape.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")
        print("\n--- Top Quotes ---\n")
        for q in quotes[:5]:
            text = q.find("span", class_="text").text.strip()
            author = q.find("small", class_="author").text.strip()
            print(f"\"{text}\"\n - {author}\n")

    except Exception as e:
        print("Error fetching quotes:", e)


def scrape_hackernews():
    print("\nFetching data from Hacker News...")
    url = "https://news.ycombinator.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        titles = soup.find_all("a", class_="storylink")

        print("\n--- Top Hacker News Articles ---\n")
        for t in titles[:10]:
            print(f"- {t.text}")
            print(f"  Link: {t['href']}\n")

    except Exception as e:
        print("Error fetching articles:", e)


def main():
    while True:
        print("\n===== Interactive Web Scraper =====")
        print("1. Scrape Quotes Website")
        print("2. Scrape Hacker News Articles")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            scrape_quotes()
        elif choice == "2":
            scrape_hackernews()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please enter 1–3.")


if __name__ == "__main__":
    main()

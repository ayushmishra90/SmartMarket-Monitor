import requests
from bs4 import BeautifulSoup

def scrape_moneycontrol():
    url = "https://www.moneycontrol.com/news/business/markets/"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    headlines = []

    # Loop through known newslist ids like newslist-0 to newslist-5
    for i in range(10):  # Adjust range if more available
        li = soup.find("li", id=f"newslist-{i}")
        if not li:
            continue

        h2 = li.find("h2")
        if not h2:
            continue

        a_tag = h2.find("a", href=True)
        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        href = a_tag['href']

        if not title or not href:
            continue
        if not href.startswith("http"):
            href = "https://www.moneycontrol.com" + href

        headlines.append({
            "title": title,
            "link": href,
            "source": "Moneycontrol"
        })
    base_url = "https://www.moneycontrol.com/news/business/markets/page-{}"
    # headers = {"User-Agent": "Mozilla/5.0"}

    for page in range(2, 11):  # pages 1 to 10
        url = base_url.format(page)
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code != 200:
                continue

            soup = BeautifulSoup(res.text, 'html.parser')

            # Loop through known newslist ids like newslist-0 to newslist-9
            for i in range(20):  # often 0–19 per page
                li = soup.find("li", id=f"newslist-{i}")
                if not li:
                    continue

                h2 = li.find("h2")
                if not h2:
                    continue

                a_tag = h2.find("a", href=True)
                if not a_tag:
                    continue

                title = a_tag.get_text(strip=True)
                href = a_tag['href']

                if not title or not href:
                    continue
                if not href.startswith("http"):
                    href = "https://www.moneycontrol.com" + href

                headlines.append({
                    "title": title,
                    "link": href,
                    "source": "Moneycontrol"
                })

        except Exception as e:
            print(f"Error scraping page {page}: {e}")
            continue

    # return headlines[:10]
    return headlines


def scrape_economic_times():
    url = "https://economictimes.indiatimes.com/markets"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    headlines = []

    for item in soup.select("ul.listing > li > a")[:10]:
        title = item.get_text(strip=True)
        href = item.get("href")
        full_url = "https://economictimes.indiatimes.com" + href if href else ""
        if title and href:
            headlines.append({"title": title, "link": full_url, "source": "Economic Times"})
    return headlines


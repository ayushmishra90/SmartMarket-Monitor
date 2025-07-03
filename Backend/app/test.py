import requests
from bs4 import BeautifulSoup

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
print( headlines[:10])
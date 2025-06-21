import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os

def get_thn_news():
    feed_url = "https://feeds.feedburner.com/TheHackersNews"
    feed = feedparser.parse(feed_url)
    articles = []

    if not feed.entries:
        print("[-] No articles found in THN feed.")
        return []

    for entry in feed.entries[:10]:
        title = entry.title
        summary = entry.summary.replace('<br>', '').replace('<p>', '').replace('</p>', '').strip()
        link = entry.link

        articles.append({
            "Source": "The Hacker News",
            "Title": title,
            "Summary": summary,
            "Link": link
        })

    return articles

def get_cyberscoop_news():
    url = "https://cyberscoop.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"[-] Error fetching CyberScoop: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    posts = soup.select("article.tease")
    if not posts:
        print("[-] No articles found.")
        return []

    for post in posts[:6]:
        try:
            title_tag = post.find("h3")
            link_tag = title_tag.find("a")
            title = link_tag.get_text(strip=True)
            link = link_tag["href"]

            summary_tag = post.find("p")
            summary = summary_tag.get_text(strip=True) if summary_tag else "No summary available."

            articles.append({
                "Source": "CyberScoop",
                "Title": title,
                "Summary": summary,
                "Link": link
            })
        except Exception as e:
            print(f"[!] Error parsing post: {e}")
            continue

    return articles

def export_to_excel(articles, output_path="output/cyber_news.xlsx"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.DataFrame(articles)
    df.to_excel(output_path, index=False)
    print(f"[+] Excel file generated at: {output_path}")

if __name__ == "__main__":
    print("[*] Scraping cybersecurity news...")
    thn_articles = get_thn_news()
    cs_articles = get_cyberscoop_news()
    all_articles = thn_articles + cs_articles
    print(f"[+] Total articles fetched: {len(all_articles)}")
    print("[*] Generating Excel file...")
    export_to_excel(all_articles)

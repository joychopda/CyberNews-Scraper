import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os
import feedparser

import feedparser

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
            "title": title,
            "summary": summary,
            "link": link
        })

    return articles
def get_cyberscoop_news():
    feed_url = "https://cyberscoop.com/feed/"
    feed = feedparser.parse(feed_url)
    articles = []

    if not feed.entries:
        print("[-] No articles found in CyberScoop feed.")
        return []

    for entry in feed.entries[:10]:
        title = entry.title
        summary = BeautifulSoup(entry.summary, "html.parser").get_text(strip=True)
        link = entry.link

        articles.append({
            "title": title,
            "summary": summary,
            "link": link
        })

    return articles

def generate_pdf(articles, output_path="output/cyber_news.pdf"):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template.html")
    html_out = template.render(articles=articles)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    HTML(string=html_out).write_pdf(output_path)
    print(f"[+] PDF generated at: {output_path}")


if __name__ == "__main__":
    print("[*] Scraping cybersecurity news from The Hacker News...")
    thn_news = get_thn_news()
    print(f"[+] Found {len(thn_news)} articles from The Hacker News.")

    print("[*] Scraping cybersecurity news from CyberScoop...")
    cs_news = get_cyberscoop_news()
    print(f"[+] Found {len(cs_news)} articles from CyberScoop.")

    all_news = thn_news + cs_news
    print(f"[+] Total articles combined: {len(all_news)}")

    print("[*] Generating PDF...")
    generate_pdf(all_news)

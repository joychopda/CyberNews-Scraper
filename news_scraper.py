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

    # Find main article containers
    posts = soup.select("article.tease")  # "tease" class holds article previews

    if not posts:
        print("[-] No articles found. Dumping HTML snippet:")
        print(response.text[:1000])
        return []

    for post in posts[:6]:  # Limit to top 6
        try:
            title_tag = post.find("h3")
            link_tag = title_tag.find("a")
            title = link_tag.get_text(strip=True)
            link = link_tag["href"]

            summary_tag = post.find("p")
            summary = summary_tag.get_text(strip=True) if summary_tag else "No summary available."

            articles.append({
                "title": title,
                "summary": summary,
                "link": link
            })
        except Exception as e:
            print(f"[!] Error parsing post: {e}")
            continue

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
    news = get_thn_news()
    print(f"[+] Found {len(news)} articles.")
    print("[*] Generating PDF...")
    generate_pdf(news)
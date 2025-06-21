# CyberNews-Scraper

Perfect — thanks for the clarification. Here’s the updated and final README.md, now with accurate dependency breakdowns based on script functionality (CSV vs PDF):

⸻

📰 News Scraper

This tool scrapes headlines from Google News RSS feeds for any search keyword you enter. Outputs can be saved as a CSV or exported as a formatted PDF using Jinja2 and WeasyPrint.

Great for OSINT, threat intel snapshots, or research reporting — all from the command line.

⸻

✅ Features
	•	🔍 Google News keyword search via RSS
	•	🧠 Extracts:
	•	Title
	•	URL
	•	Source
	•	Publish Time
	•	🗃️ Outputs:
	•	Excel format (news_scraper_xl.py)
	•	PDF format (news_scraper.py)
	•	Minimal setup, easy to customize

⸻

📦 Dependencies

Install all dependencies at once:

pip install requests beautifulsoup4 feedparser pandas jinja2 weasyprint

Breakdown by script:

Script	Dependencies
news_scraper_csv.py	requests, beautifulsoup4, feedparser, pandas, os
news_scraper.py	requests, beautifulsoup4, feedparser, jinja2, weasyprint, os

💡 Note: os is part of Python’s standard library.

⸻

🚀 How to Use

Clone the repo

git clone https://github.com/joychopda/news-scraper.git
cd news-scraper

Excel Output

python news_scraper_xl.py

Creates cyber_news.xlsx in your current directory.

PDF Output

python news_scraper_pdf.py

Creates a styled cyber_news.pdf.

Both scripts will prompt you for a search keyword.

⸻

📄 Sample Output

Excel (cyber_news.xlsx):

Title	Link	Source	Published
Major Cyberattack Hits	https://news.example.com	Wired	2025-06-20T08:00:00Z

PDF (cyber_news.pdf):
Clean, readable format with articles sorted and styled via HTML/CSS (Jinja2 + WeasyPrint).

⸻

🔍 Use Cases
	•	Threat intel snapshotting
	•	Daily news digests for cybersecurity teams
	•	OSINT enrichment
	•	Competitive monitoring
	•	Report-ready PDF exports

⸻

⚠️ Disclaimer
	•	Google News RSS is unofficial and may rate-limit or block aggressive scraping.
	•	For educational and non-commercial use. Always respect robots.txt and ToS.



# Web Scraping Project

This project demonstrates web scraping using Python, Selenium, and BeautifulSoup. It retrieves HTML content from YouTube, parses commenter names, and optionally uses text-to-speech to read them aloud.

## Features
- Retrieve dynamic HTML from YouTube using Selenium
- Parse commenter/channel names with BeautifulSoup
- Speak names using pyttsx3 (text-to-speech)
- Organized with Object-Oriented Programming (OOP)

## Prerequisites
- Python 3.8+
- Google Chrome browser
- ChromeDriver (managed automatically)

## Setup
1. Clone the repository:
   ```
   git clone https://github.com/M-Nadeem-B/Web-Scraping.git
   cd Web-Scraping
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
- **Selenium_with_BS4.py**: Retrieves YouTube HTML and parses commenter names, speaking them aloud.
- **3.simplebs4.py**: Parses a saved HTML file and speaks commenter names.
- **2.selenium.py**: Scrapes YouTube commenter names using Selenium only.
- **1.retrieving_html.py**: Retrieves and saves HTML from YouTube.

Run a script:
```bash
python Selenium_with_BS4.py
```

## File Structure
- `Selenium_with_BS4.py` — Combined Selenium and BeautifulSoup script
- `2.simplebs4.py` — BeautifulSoup parser with TTS
- `selenium.py` — Selenium-only scraper
- `1.retrieving_html.py` — HTML retriever
- `requirements.txt` — Python dependencies
- `.gitignore` — Files/folders to ignore in git

## Notes
- Do not upload sensitive info (API keys, passwords).
- For YouTube scraping, selectors may change if YouTube updates its layout.

## License
MIT

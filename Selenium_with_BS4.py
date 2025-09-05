from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pyttsx3
import time


class YouTubeCommentScraper:
    def __init__(self, url):
        '''Initialize the scraper with the YouTube video URL.'''
        self.url = url
        options = webdriver.ChromeOptions() # Configure Chrome options
        options.add_argument("--headless") # Run in headless mode
        # Initialize WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 

    def get_html(self, scroll_count=5):
        '''Retrieve HTML content after scrolling 5 times to load comments.'''
        self.driver.get(self.url) # Open the YouTube video URL
        for _ in range(scroll_count):
            # Scroll down to load more comments
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);") 
            time.sleep(3) # Wait for comments to load
        html_content = self.driver.page_source # Get the page source
        self.driver.quit() # Close the WebDriver
        return html_content

    def parse_and_speak(self):
        '''Parse the HTML to extract commenter names and use text-to-speech to read them out.'''
        html_content = self.get_html()
        soup = BeautifulSoup(html_content, "html.parser")
        commenters = soup.find_all(id="author-text", class_="yt-simple-endpoint style-scope ytd-comment-view-model")
        names = [commenter.get_text().replace("\n", " ").replace("@", " ").strip() for commenter in commenters[:10]]
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.8)
        for name in names:
            print(name)
            engine.say(name)
            engine.runAndWait() # Make sure that it is inside the loop

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=uUbvJ7ZEhPE'
    scraper = YouTubeCommentScraper(video_url)
    scraper.parse_and_speak()

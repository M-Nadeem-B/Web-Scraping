from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YouTubeCommentScraper:
    def __init__(self, video_url, scroll_count=5):
        self.video_url = video_url 
        self.scroll_count = scroll_count
        options = webdriver.ChromeOptions()
        options.add_argument("--headless") 
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    def open_video(self):
        self.driver.get(self.video_url)

    def scroll_comments(self):
        for _ in range(self.scroll_count):
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(3)
    def get_commenters(self, max_results=10):
        # Wait for comments to load
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#author-text span"))
            ) # Wait until at least one commenter's name is present
        except:
            print("Comments did not load in time.")
            return []
        commenters = self.driver.find_elements(By.CSS_SELECTOR, "#author-text span")
        return [user.text.lstrip('@') for user in commenters[:max_results]]

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=uUbvJ7ZEhPE'
    scraper = YouTubeCommentScraper(video_url)
    scraper.open_video()
    scraper.scroll_comments()
    names = scraper.get_commenters()
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")
    scraper.quit()


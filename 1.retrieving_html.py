from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open YouTube Video
video_url = 'https://www.youtube.com/watch?v=uUbvJ7ZEhPE'  # Replace VIDEO_ID
driver.get(video_url)

# Scroll down to load comments
for _ in range(5):  # Adjust scroll count if needed
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3)

# Get full page source
html_content = driver.page_source

# Save it to an HTML file
with open("webpage_dynamic.html", "w", encoding="utf-8") as file:
    file.write(html_content)

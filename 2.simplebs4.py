from bs4 import BeautifulSoup
import pyttsx3

class YouTubeCommentParser:
    def __init__(self, html_file):
        '''Initialize the parser with the HTML file.'''
        self.html_file = html_file # Store the HTML file path
        self.engine = pyttsx3.init() # Initialize text-to-speech engine
        self.engine.setProperty('rate', 150) # Set speech rate
        self.engine.setProperty('volume', 0.8) # Set volume

    def prettify_html(self, output_file="prettified.html"):
        '''Prettify and save the HTML content to a new file.'''
        with open(self.html_file, "r", encoding="utf-8") as file: # Open the HTML file
            soup = BeautifulSoup(file, "html.parser")
        with open(output_file, "w", encoding="utf-8") as file: # Write prettified HTML to new file
            file.write(soup.prettify())

    def parse_and_speak(self, max_names=10):
        '''Parse the HTML to extract commenter names and use text-to-speech to read them out.'''
        with open(self.html_file, "r", encoding="utf-8") as file: 
            soup = BeautifulSoup(file, "html.parser")
        commenters = soup.find_all(id="author-text", class_="yt-simple-endpoint style-scope ytd-comment-view-model")
        for commenter in commenters[:max_names]: # Limit to max_names which is 10 by default
            name = commenter.get_text().replace("\n", " ").replace("@", " ").strip()
            self.engine.say(name)
            print(name)
            self.engine.runAndWait() # Ensure speech is processed otherwise speak 1st name only

if __name__ == "__main__":
    parser = YouTubeCommentParser("webpage_dynamic.html")
    parser.prettify_html() 
    parser.parse_and_speak()
   


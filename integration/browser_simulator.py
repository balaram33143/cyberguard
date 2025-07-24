import random
import time

class BrowserSimulator:
    def __init__(self, phishing_urls):
        self.phishing_urls = phishing_urls
        self.normal_urls = [
            "https://www.google.com",
            "https://www.wikipedia.org",
            "https://www.reddit.com",
            "https://www.openai.com",
            "https://www.github.com"
        ]

    def simulate_click(self):
        # Randomly decide phishing or normal (70% normal, 30% phishing)
        if random.random() < 0.3:
            url = random.choice(self.phishing_urls)
            label = "phishing"
        else:
            url = random.choice(self.normal_urls)
            label = "normal"
        
        timestamp = time.time()
        return {
            "url": url,
            "label": label,
            "timestamp": timestamp
        }

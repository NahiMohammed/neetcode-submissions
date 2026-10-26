class Solution:

    def __init__(self):
        self.urls = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        shortUrl = str(self.counter)
        self.urls[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl]
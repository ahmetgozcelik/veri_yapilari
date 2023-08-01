class Codec:
    def __init__(self):
        self.encodingMap = {}
        self.decodingMap = {}
        self.baseUrl = "https://tinyurl.com/"


    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodingMap:
            shortUrl = self.baseUrl + str(len(self.encodingMap) + 1)
            self.encodingMap[longUrl]  = shortUrl
            self.decodingMap[shortUrl] = longUrl
        return self.encodingMap[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.decodingMap[shortUrl]
    
codec = Codec()

print(codec.encode("https://ahmedgurkanozcelik.com/test/test/test"))
print(codec.decode("https://tinyurl.com/1"))
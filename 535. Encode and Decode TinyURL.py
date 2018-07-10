# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. 
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Solution:
# 1. ramdon generate 6 digit string/number mix
# 2. use two dictionary to keep the relation between code -> url and url -> code. before return value, check if it's already exist. 
# 3. remember to use self when writing the fucntions names and global variables in Python
class Codec:
    dic = string.ascii_letters + string.digits

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.Url2Code = {}
        self.Code2Url = {}
        if longUrl in self.Url2Code:
            return 'http://tinyurl.com/' + Url2Code[longUrl]
        else:
            code = ''.join(random.choice(Codec.dic) for i in range(6))
            if code not in Code2Url:
                self.Url2Code[longUrl] = code
                self.Code2Url[code] = longUrl
            return 'http://tinyurl.com/' + self.Url2Code[longUrl]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.Code2Url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


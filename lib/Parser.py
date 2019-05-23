import bs4 from BeautifulSoup;
import urllib.request;

class Parser:
    bs = "";

    def __init__(self, url):
        fp = urllib.request.urlopen(url).read();
        self.bs = BeautifulSoup(fp.decode("utf8"));
        fp.close();

    def Parse(self, elements):
        
        pass;
    

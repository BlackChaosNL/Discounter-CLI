class Product:
    tag = '';
    title = '';
    description = '';
    price = '';
    url = '';

    def __to_str(self):
        return self.getTag() + " - " + self.getTitle() + " - " + self.getPrice();

    def setTag(self, tag):
        self.tag = tag;

    def getTag(self):
        return "[ " + self.tag + " ]";

    def setTitle(self, title):
        self.title = title;
    
    def getTitle(self):
        return self.title;

    def setDescription(self, description):
        self.description = description;

    def getDescription(self):
        return self.description;

    def setPrice(self, price):
        self.price = price;

    def getPrice(self):
        return self.price;

    def setUrl(self, url):
        self.url = url;

    def getUrl(self):
        return self.url;
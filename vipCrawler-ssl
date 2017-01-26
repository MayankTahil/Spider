### Pre-req is to pip install requests. If you do not have pip and requests module installed do the following: 
### $ sudo apt-get install python-pip python-dev build-essential 
### $ sudo pip install --upgrade pip 
### $ sudo pip install requests 


# This code takes in a single CLI input where the only parameter is the file name/path of a csv list of all VIP websites to cawl.
# For example in the format:  http://<vip>:port/
#
#     http://172.16.0.11:8080,
#     http://172.16.0.11:8081,
#     http://172.16.0.11:8082,
#     http://172.16.0.11:8083,
#     http://172.16.0.11:8084,
#     http://172.16.0.11:8085,
#     http://172.16.0.11:8086,
#     http://172.16.0.11:8087,
#     http://172.16.0.11:8088,
#     http://172.16.0.11:8089,
#     http://172.16.0.11:8090,
#     http://172.16.0.11:8091,

# Here is our spider. It takes in an URL,
# and the number of pages to search through before giving up
def spider(url, maxPages):
    pagesToVisit = [url]
    numberVisited = 0
    foundWord = False
    # The main loop. Create a LinkParser and get all the links on the page.
    # Also search the page for the word or string
    # In our getLinks function we return the web page
    # (this is useful for searching for the word)
    # and we return a set of links from that web page
    # (this is useful for where to go next)
    while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
        numberVisited = numberVisited + 1
        # Start from the beginning of our collection of pages to visit
        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        print(numberVisited, "Visiting:", url)
        parser = LinkParser()
        data, links = parser.getLinks(url)
        pagesToVisit = pagesToVisit + links
        sleep(random())
        # if data.find(word)>-1:
        #     foundWord = True
        #     # Add the pages that we visited to the end of our collection
        #     # of pages to visit:
        #     pagesToVisit = pagesToVisit + links
        #     print(" **Success!**")

    # if foundWord:
    #     print("The word", word, "was found at", url)
    # else:
    #     print("Word never found")
	
# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class LinkParser(HTMLParser):
    # This is a function that HTMLParser normally has
    # but we are adding some functionality to it
    def handle_starttag(self, tag, attrs):
        # We are looking for the begining of a link. Links normally look
        # like <a href="www.someurl.com"></a>
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # We are grabbing the new URL. We are also adding the
                    # base URL to it. For example:
                    # www.netinstructions.com is the base and
                    # somepage.html is the new URL (a relative URL)
                    #
                    # We combine a relative URL with the base URL to create
                    # an absolute URL like:
                    # www.netinstructions.com/somepage.html
                    newUrl = parse.urljoin(self.baseUrl, value)
                    # And add it to our colection of links:
                    self.links = self.links + [newUrl]
					
    # This is a new function that we are creating to get links
    # that our spider() function will call
    def getLinks(self, url):
        self.links = []
        # Remember the base URL which will be important when creating
        # absolute URLs
        self.baseUrl = url
        # Use the urlopen function from the standard Python 3 library
        print(url)  
        response = requests.get(url, verify=False)
        self.feed(response.text)
        return response.text, self.links


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
      vipList = list(csv.reader(f))
    numOfVips = len(vipList)
    completedVips = 0
    print(vipList)
    while completedVips > -1:
        urls2seekDeep = randint(3, 20)
        vip = vipList[randint(1, numOfVips)-1][0]
        spider(vip, urls2seekDeep)

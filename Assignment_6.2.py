#DSC 430: Python Programming - Assignment 0602: Surf CDM
#Student Name: Serena Yang
#Date: Oct, 25, 2020
#Video Link: https://youtu.be/vBwojzsDndw
#I have not given or received any unauthorized assistance on this assignment.

from urllib.request import urlopen
from html.parser import HTMLParser

#get text from the url
class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.text = [] 
    
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            return attr

    def handle_endtag(self, tag):
        return tag

    def handle_data(self, data):
        self.text.append(data)
        return self.text

#get link from user and call 
def read():
    url = input("link: ")
    content = urlopen(url).read().decode()
    #print(content)
    myparser = MyHTMLParser()
    doc = myparser.feed(content)

    print("doc" + str(doc))
    return (doc, url)


#anaylze the url
def analyze(url):
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()

    return urls

#restricted search to
def crawls2(url):
    global visited
    visited.add(url)

    links = analyze(url)

    for link in links:
        if link not in visited:
            try:
                crawls2(link)
            except:
                pass

#collect hyperlinks
class Collector(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':
                        self.links.append(absolute)

    def getLinks(self):
        return self.links


def findwords(content):
    count = {}
    words = content.strip().split()
    
    #for each word, if the word is already in the count list, freq +1; otherwise, add the word into the list and its freq =1
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    

    freqslist = []
    for word, freq in count.items():
        freqslist.append((word, freq))
    

    freqslist.sort(reverse = True)

    print("Output: ")
    for word, freq in freqslist[:25]:
        if word not in ['“','”','’','–','~','}','|','{','.','–','<','>','#','/']:
            print(word, freq)


def main():
    content, url = read()
    urls = analyze(url)
    crawls2(url)
    findwords(content)

main()
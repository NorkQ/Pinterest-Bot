import requests, os
from xml.dom import minidom
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts
from wordpress_xmlrpc import WordPressTerm
from wordpress_xmlrpc.methods import posts
import re
from bs4 import BeautifulSoup
from wordpress_xmlrpc.methods import taxonomies

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

file_name = "posts.xml"
def download(url):
    get_response = requests.get(url,stream=True)
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

url = 'https://evcilhayvanbakimi.com/post-sitemap.xml'
download(url)

# parse an xml file by name
print(file_name)
mydoc = minidom.parse(file_name)

items = mydoc.getElementsByTagName('loc')

for i in range(len(items)):
  items[i] = items[i].firstChild.data


"""post_titles = list()
post_contents = list()

for post in all_posts:
    title = cleanhtml(post.title)
    content = cleanhtml(post.content)
    post_titles.append(title)
    post_contents.append(content)"""


client = Client("https://www.evcilhayvanbakimi.com/xmlrpc.php", 'NorkQ', 'emsile2158')
all_posts = client.call(GetPosts())
tags = client.call(taxonomies.GetTerms('post_tag'))

for i in range(len(tags)):
  tags[i] = tags[i].name


tags = tags
titles = items
titles.pop(0)

print(tags)
print(titles)


class Post():
    def __init__(self, title, descr, image, category, addres):
        self.title = title
        self.descr = descr
        self.image = image
        self.category = category
        self.address = addres





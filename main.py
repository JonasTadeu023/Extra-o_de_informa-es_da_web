import requests
import json
from bs4 import BeautifulSoup

res = requests.get("https://diolinux.com.br/")
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all(class_ = "post")

all_posts = []

for post in posts:
    info = post.find(class_ = "post-outer")
    title = info.h2.text
    preview = post.find(class_ = "entry-excerpt").text
    info2 = post.find(class_ = "meta-author")
    author = info2.a.text
    date = post.find(class_ = "meta-date").text

    all_posts.append({
        'titulo' : title, 
        'previo' : preview, 
        'autor' : author,
        'data' : date 
    })

with open('posts.json', 'w') as json_file:
    json.dump(all_posts, json_file, indent = 3, ensure_ascii = False)
with open('randompost.txt', 'r+', encoding='utf-8') as clear:
    clear.truncate(0)

import json
import praw
import random
from PIL import Image, ImageFont, ImageDraw
import textwrap 
import imgrounder


with open("Reddit API/redditapiclient.json") as json_data:
    redditkeys = json.load(json_data)

reddit = praw.Reddit(
    client_id = redditkeys["client_id"],
    client_secret = redditkeys["client_secret"],
    user_agent = redditkeys["user_agent"]
)


post_list = []
title_list = []

def replace_abbreviations(text):
    replacements = {
        "AITA": "Am I the asshole",
        "TIFU": "Today I fucked up",
        "TL;DR": "Too long didn't read",
        "Tl;dr": "Too long didn't read",
        "tl;dr": "Too long didn't read",
        "FU": 'fucked up'
    }

    for abbreviation, replacement in replacements.items():
        text = text.replace(abbreviation, replacement)
    return text

subreddit_list = ["AmITheAsshole", "tifu"]

subreddit = reddit.subreddit(random.choice(subreddit_list))

for submissions in subreddit.hot(limit=20):
    post_list.append(submissions.selftext)
    title_list.append(submissions.title)

random_post = random.choice(post_list)
random_title = title_list[post_list.index(random_post)]
print(random_title)
print(random_post)

if subreddit == "AmITheAsshole":
    im = Image.open('images/posttemplate1.png')
    im.show()
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("fonts/Poppins-Bold.ttf", 50)
    height = 160
    wrappedtext = textwrap.wrap(random_title,35)
    if len(wrappedtext) > 3:
        print(len(wrappedtext))
        wrappedtext = textwrap.wrap(random_title,20)
    for phrase in wrappedtext:    
        draw.text((50,height),phrase, (0,0,0), font=font)
        height += 60
    imgrounder.imagerounder(im=im)
elif subreddit == "tifu":
    im = Image.open('images/posttemplate2.png')
    im.show()
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("fonts/Poppins-Bold.ttf", 50)
    height = 160
    wrappedtext = textwrap.wrap(random_title,35)
    if len(wrappedtext) > 3:
        print(len(wrappedtext))
        wrappedtext = textwrap.wrap(random_title,20)
    for phrase in wrappedtext:    
        draw.text((50,height),phrase, (0,0,0), font=font)
        height += 60
    imgrounder.imagerounder(im=im)

with open('randompost.txt', 'r+', encoding='utf-8') as post:
    post.write(random_title)
    post.write('\n')
    post.write(random_post)
    post.seek(0)
    new_text = replace_abbreviations(post.read())
    post.seek(0)
    post.truncate(0)
    post.write(new_text)
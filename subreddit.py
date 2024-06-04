with open('randompost.txt', 'r+', encoding='utf-8') as clear:
    clear.truncate(0)

import json
import praw
import random


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
        "TIFU": "Today I fucked up"
    }

    for abbreviation, replacement in replacements.items():
        text = text.replace(abbreviation, replacement)
    return text

subreddit_list = ["AmITheAsshole", "tifu", "oddlysatisfying"]

subreddit = reddit.subreddit(random.choice(subreddit_list))

for submissions in subreddit.hot(limit=20):
    post_list.append(submissions.selftext)
    title_list.append(submissions.title)

random_post = random.choice(post_list)
random_title = title_list[post_list.index(random_post)]
print(random_title)
print(random_post)

with open('randompost.txt', 'r+', encoding='utf-8') as post:
    post.write(random_title)
    post.write('\n')
    post.write(random_post)
    post.seek(0)
    new_text = replace_abbreviations(post.read())
    post.seek(0)
    post.truncate(0)
    post.write(new_text)

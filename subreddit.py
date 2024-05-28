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

subreddit_list = ["AmITheAsshole", "tifu"]

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
    post.seek(0)  # Reset file pointer to the beginning of the file
    lines = post.readlines()
    word = "AITA"
    for line in lines:
        if line.find("AITA") != -1:
            print(word, 'string exists in file')
            new_line = line.replace("AITA", "Am I the asshole")
            
    post.write(new_line)

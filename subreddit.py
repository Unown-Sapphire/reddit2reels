import json
import praw
import itertools
import random

with open("Reddit API/redditapiclient.json") as json_data:
    redditkeys = json.load(json_data)

reddit = praw.Reddit(
    client_id = "-4WA2RrwmCqDytJam4HnzA",
    client_secret = "oVVMVjxSiUr0iGF6NVYF2zQawk13Jw",
    user_agent = "subfetcherv1"
)

post_list = []

subreddit = reddit.subreddit("AmITheAsshole")

for submissions in subreddit.top(limit=20):
    post_list.append(submissions.selftext)

random_post = random.choice(post_list)
print(random_post)

with open('randompost.txt', 'w', encoding='utf-8') as post:
    post.write(random_post)
import json
import praw
import itertools
import random

with open("Reddit API/redditapiclient.json") as json_data:
    redditkeys = json.load(json_data)

reddit = praw.Reddit(
    client_id = redditkeys["client_id"],
    client_secret = redditkeys["client_secret"],
    user_agent = redditkeys["user_agent"]
)

post_list = []

subreddit = reddit.subreddit("AmITheAsshole")

for submissions in subreddit.top(limit=20):
    post_list.append(submissions.selftext)

random_post = random.choice(post_list)
print(random_post)

with open('randompost.txt', 'w', encoding='utf-8') as post:
    post.write(random_post)

update_variable = 0
import json
import praw

with open("Reddit API/redditapiclient.json") as json_data:
    redditkeys = json.load(json_data)

reddit = praw.Reddit(
    client_id = "-4WA2RrwmCqDytJam4HnzA",
    client_secret = "oVVMVjxSiUr0iGF6NVYF2zQawk13Jw",
    user_agent = "subfetcherv1"
)

subreddit = reddit.subreddit("test")

for submission in subreddit.top(limit=2):
    print(submission.selftext)
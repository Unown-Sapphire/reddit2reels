import json
import praw

with open("Reddit API/redditapiclient.json") as json_data:
    redditkeys = json.load(json_data)

reddit = praw.Reddit(
    client_id = redditkeys["client_id"],
    client_secret = redditkeys["client_secret"],
    user_agent = redditkeys["user_agent"]
)

subreddit = reddit.subreddit("test")

for submission in subreddit.top(limit=2):
    print(submission.selftext)
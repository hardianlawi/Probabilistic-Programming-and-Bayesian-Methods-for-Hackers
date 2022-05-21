import sys

import numpy as np

import praw


reddit = praw.Reddit(
    client_id="dewRhkO5GKI2Z_SJXPh9Aw",
    client_secret="v5_YYOr4T1D9MolaUo9UeJhtOGT-bA",
    user_agent="jupyter:1.0:1.0 by (u/hardinalawi)",
)
subreddit = reddit.subreddit("showerthoughts")

# go by timespan - 'hour', 'day', 'week', 'month', 'year', 'all'
# might need to go longer than an hour to get entries...
top_submissions = subreddit.top(time_filter='week', limit=100)

n_sub = int( sys.argv[1] ) if sys.argv[1] else 1

i = 0
while i < n_sub:
    top_submission = next(top_submissions)
    i += 1

top_post = top_submission.title

upvotes = []
downvotes = []
contents = []

for sub in top_submissions:
    try:
        ratio = sub.upvote_ratio
        ups = int(
            round((ratio * sub.score) / (2 * ratio - 1))
            if ratio != 0.5
            else round(sub.score / 2)
        )
        upvotes.append(ups)
        downvotes.append(ups - sub.score)
        contents.append(sub.title)
    except Exception as e:
        continue


votes = np.array( [ upvotes, downvotes] ).T
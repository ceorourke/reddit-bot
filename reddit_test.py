import praw
import os

reddit_client_id = os.environ.get("client_id")
reddit_client_secret = os.environ.get("client_secret")
reddit_user_agent = os.environ.get("user_agent")
reddit_username = os.environ.get("username")
reddit_password = os.environ.get("password")

reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent,
                     username=reddit_username,
                     password=reddit_password)

subreddit = reddit.subreddit('CatsStandingUp')

# print(subreddit.display_name)  # Output: redditdev
# print(subreddit.title)         # Output: reddit Development
# print(subreddit.description)   # Output: A subreddit for discussion of ...

# controversial, gilded, hot, new, rising, top
for submission in subreddit.new(limit=20):
#     print(submission.title)  # Output: the submission's title
#     print(submission.score)  # Output: the submission's score
#     print(submission.id)     # Output: the submission's ID
#     print(submission.url) 
#     print(submission.author)
#     print(submission.author.link_karma)

    top_level_comments = list(submission.comments)
    all_comments = submission.comments.list()
    for comment in all_comments:
        if 'Cat.' in comment.body:
            reply_text = "Cat."
            comment.reply(reply_text)
            print comment.body
            print submission
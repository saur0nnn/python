import praw

reddit = praw.Reddit(
    client_id="EPQ8kri-0sdvfb0hyO4Bww",
    client_secret="3eEKj0HPtxjw92VA6-8h7iQqY3LmNw",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0",
    username = "saur0nnn",
    password = "gmertisauroni123"
)

subreddit = reddit.subreddit("test")


print(f"Subreddit Title - {subreddit.title}")

print("\n-- Submission --")
for submission in subreddit.stream.submissions("143iv8m"):
    print(f"Submission title - {submission.title}")
    
    redditor1 = submission.author
    print(f"Avtoris saxeli - {redditor1.name}\n")
    
print ("-- Comment -- ")
for comment in subreddit.comments(limit = 2):
    comment1 = comment.author
    print(f"komentaris avtori - {comment1}")
    
    comment.reply("realuri informacia romelic ar arsebobs")
    print(f"replied to comment: {comment.id}")
    print("comment link")
    print(f"https://www.reddit.com/api/info?id=t1_{comment.id}")

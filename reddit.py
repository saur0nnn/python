import praw

reddit = praw.Reddit(
    client_id="EPQ8kri-0sdvfb0hyO4Bww",
    client_secret="3eEKj0HPtxjw92VA6-8h7iQqY3LmNw",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0",
)

subreddit = reddit.subreddit("test")


print(f"\nSubreddit display name - {subreddit.display_name}")
print(f"Subreddit Title - {subreddit.title}")
print(f"Subreddit Description - {subreddit.description}")

print("\nLast 3 submissions")
for submission in subreddit.hot(limit=3):
    print(f"Submission title - {submission.title}")
    
    redditor1 = submission.author
    print(f"Avtoris saxeli - {redditor1.name}\n")
import praw
import threading

def monitor_comments(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    for comment in subreddit.stream.comments():
        # Process the comment and craft a reply
        reply = "Hello! This is a bot reply."

        # Reply to the comment
        comment.reply(reply)

# Create threads to handle multiple tasks concurrently
threads = []

# Create a thread to monitor comments in a specific subreddit
comment_thread = threading.Thread(target=monitor_comments, args=("AskReddit",))
threads.append(comment_thread)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

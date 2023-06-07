import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="YOUR_USER_AGENT",
    username="YOUR_BOT_USERNAME",
    password="YOUR_BOT_PASSWORD",
)

def interact_with_comments(submission_id):
    submission = reddit.submission(id=submission_id)

    # Access the comments of the submission
    submission.comments.replace_more(limit=None)  # Retrieve all comments including nested ones

    for comment in submission.comments.list():
        # Process each comment and perform actions
        print(f"Comment ID: {comment.id}")
        print(f"Comment Body: {comment.body}")
        # Add your custom logic here

# Specify the submission ID or URL of the submission
submission_id = "SUBMISSION_ID_OR_URL"

interact_with_comments(submission_id)

import praw
import threading

reddit = praw.Reddit(
    client_id="not fake",
    client_secret="martlac rom",
    user_agent="realuri",
    username = "feiki? ara",
    password = "githubzeDasadebiParoli"
)
# 143iv8m - chemi submissionis ID "test" subredditshi
        
def get_subreddit_comments(subreddit_name, count):
    subreddit = reddit.subreddit(subreddit_name)
    print ("\n-- Getting Subreddit Comments --\n")
    
    for comment in subreddit.comments(limit = count):
        comment_author = comment.author
    
        print(f"komentaris ID: {comment.id}")
        print(f"komentari: {comment.body}")
        print(f"komentaris avtori - {comment_author}")
        print(f"komentaris linki: https://www.reddit.com/api/info?id=t1_{comment.id}\n")

def get_submission_comments(submission_id, count):
    submission = reddit.submission(id=submission_id)
    print ("\n-- Getting Submission Comments --\n")
    
    submission.comments.replace_more(limit = count)

    for comment in submission.comments.list():
        comment_author = comment.author
        
        print(f"komentaris ID: {comment.id}")
        print(f"komentari: {comment.body}")
        print(f"komentaris avtori - {comment_author}")
        print(f"komentaris linki: https://www.reddit.com/api/info?id=t1_{comment.id}\n")

# !!!! DID SUBMISSIONZE MAGARI ISPAMEBA DA YLEOBAA !!!!
#
# def reply_submission_comments(submission_id):
#     submission = reddit.submission(id = submission_id)
#     print("\n-- Replying To All Submission Comments --\n")
    
#     for comment in submission.comments.list():
#         comment_author = comment.author
        
#         comment.reply("test for submission")
        
#         print(f"komentaris ID: {comment.id}")
#         print(f"komentari: {comment.body}")
#         print(f"komentaris avtori: {comment_author}")
#         print(f"komentaris linki: https://www.reddit.com/api/info?id=t1_{comment.id}\n")



# !!!! DID SUBMISSIONZE MAGARI ISPAMEBA DA YLEOBAA !!!!
#
# def reply_all_comments(subreddit_name, submission_id):
#     subreddit = reddit.subreddit(subreddit_name)
#     submission = reddit.submission(id=submission_id)
#     comment_stream = subreddit.stream.comments()
    
#     for comment in comment_stream:
#         if comment.submission.id == submission_id:
#             reply = "zd shechema (boti)"
#             comment.reply(reply)
    
#     print("davwere!")



# !!!! DID SUBMISSIONZE MAGARI ISPAMEBA DA YLEOBAA !!!!
#
# def reply_subreddit_comments(subreddit_name, count):
#     subreddit = reddit.subreddit(subreddit_name)
#     print ("\n-- Replying To Subreddit Comments --\n")
    
#     for comment in subreddit.comments(limit = count):
#         comment_author = comment.author
    
#         comment.reply("realuri informacia romelic ar arsebobs")
        
#         print(f"komentaris ID: {comment.id}")
#         print(f"komentari: {comment.body}")
#         print(f"komentaris avtori - {comment_author}")
#         print(f"komentaris linki: https://www.reddit.com/api/info?id=t1_{comment.id}\n")
        
threads = []

# submission_thread = threading.Thread(target=get_submission_comments, args=("143iv8m", 100))

subreddit_thread = threading.Thread(target=get_subreddit_comments, args=("ascii", 1000000))


# threads.append(submission_thread)
threads.append(subreddit_thread)


for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()

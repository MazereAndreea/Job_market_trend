import os
import praw
import csv
from pymongo import MongoClient
from dotenv import load_dotenv
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "app", ".env")
load_dotenv(dotenv_path)

# Initialize Reddit client
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT"),
)

# Initialize MongoDB client
client = MongoClient(os.getenv("MONGO_DB_URL"))
db = client["reddit_salary_data"]
collection1 = db["posts"]
collection2 = db["comments"]

# Define subreddits and keywords
subreddits = ["programare","romania"]
keywords = ["salary", "job", "income", "freelancer", "contract", "B2B", "remote", "salariu", "experiență","companie","titlu","compensatie","tara","cost"]

for sub in subreddits:
    print(f"Searching in r/{sub}...")
    for submission in reddit.subreddit(sub).search(" OR ".join(keywords), limit=5):
        submission.comments.replace_more(limit=0)
        comments = [comment.body for comment in submission.comments]
        post_data = {
            "title": submission.title,
            "selftext": submission.selftext,
            "subreddit": sub,
            "comments": comments,
            "url": submission.url,
            "created_utc": submission.created_utc
        }

        collection1.insert_one(post_data)

#Searching for a specific post and inserting its comments into MongoDB
post_id = "1lqjtjd"
submission = reddit.submission(id=post_id)

for comment in submission.comments.list():
    comment_data = {
        "post_id": post_id,
        "comment_id": comment.id,
        "body": comment.body,
        "author": str(comment.author),
        "created_utc": comment.created_utc
    }
    collection2.insert_one(comment_data)
    print(f"Inserted comment {comment.id} from post {post_id} into MongoDB.")

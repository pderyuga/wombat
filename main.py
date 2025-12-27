import os
from dotenv import load_dotenv
import praw


load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
user_agent = os.environ.get("USER_AGENT")


def main():
    print(f"Hello from {user_agent}!")

    # Initialize Reddit instance
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )

    print(reddit.auth.scopes())

    # Enable read-only mode
    reddit.read_only = True

    # Subreddit to scrape
    subreddit = reddit.subreddit("ExperiencedDevs")

    # Display the name of the Subreddit
    print("Display Name:", subreddit.display_name)

    # Display the title of the Subreddit
    print("Title:", subreddit.title)

    # Display the description of the Subreddit
    print("Description:", subreddit.description)


if __name__ == "__main__":
    main()

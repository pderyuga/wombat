from wombat.reddit import initialize_reddit


def scrape_subreddit(subreddit_name: str):
    # Initialize reddit instance
    reddit = initialize_reddit()

    # Subreddit to scrape
    subreddit = reddit.subreddit("ExperiencedDevs")

    # Display the name of the Subreddit
    print("Display Name:", subreddit.display_name)

    # Display the title of the Subreddit
    print("Title:", subreddit.title)

    # Display the description of the Subreddit
    print("Description:", subreddit.description)

from cli.reddit import initialize_reddit
from prawcore import NotFound, Forbidden, RequestException


def scrape_subreddit(subreddit_name: str):
    """Scrape and display information from a subreddit."""
    # Initialize reddit instance
    reddit = initialize_reddit()

    try:
        # Subreddit to scrape (using the parameter, not hardcoded)
        subreddit = reddit.subreddit(subreddit_name)

        # Access a property to trigger API call and validate existence
        # This will raise NotFound if subreddit doesn't exist
        _ = subreddit.id

        # Display the name of the Subreddit
        print("Display Name:", subreddit.display_name)

        # Display the title of the Subreddit
        print("Title:", subreddit.title)

        # Display the description of the Subreddit
        print("Description:", subreddit.description)

    except NotFound:
        print(f"Error: Subreddit '{subreddit_name}' does not exist")
    except Forbidden:
        print(f"Error: Subreddit '{subreddit_name}' is private or restricted")
    except RequestException as e:
        print(f"Error: Network request failed - {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

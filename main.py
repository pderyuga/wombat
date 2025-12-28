import sys
from wombat.commands import scrape_subreddit


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        subreddit_name = sys.argv[2]

        if command == "scrape":
            scrape_subreddit(subreddit_name)
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)


if __name__ == "__main__":
    main()

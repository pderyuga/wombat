import argparse
from wombat.commands import scrape_subreddit


def main():
    # Create the main parser
    parser = argparse.ArgumentParser(
        prog="wombat",
        description="Wombat - Reddit scraping CLI tool",
        epilog="Examples:\n  uv run main.py scrape python\n  uv run main.py scrape ExperiencedDevs",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Create subparsers for commands
    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
        required=True
    )
    
    # Add 'scrape' command
    scrape_parser = subparsers.add_parser(
        "scrape",
        help="Scrape information from a given subreddit"
    )
    scrape_parser.add_argument(
        "subreddit",
        help="Name of the subreddit to scrape"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Route to appropriate command
    match args.command:
        case "scrape":
            scrape_subreddit(args.subreddit)
            
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()

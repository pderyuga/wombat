# Wombat 🦫

A command-line tool for scraping Reddit subreddit information.

## Prerequisites

- Python 3.13+ (or adjust to your version)
- [uv](https://github.com/astral-sh/uv) package manager

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd wombat
```

### 2. Install dependencies

```
uv sync
```

### 3. Get Reddit API credentials

> **Note:** Reddit's old self-service API tool (reddit.com/prefs/apps) was deprecated in 2023. New users must apply through Reddit's formal approval process. This project was created using credentials from the legacy system.

**If you have existing credentials:**

- You can continue using your CLIENT_ID, CLIENT_SECRET, and USER_AGENT

**If you need new credentials:**

- Apply through Reddit's official API access request process: https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164&tf_14867328473236
- Approval is at Reddit's discretion and may take time

Once you have credentials, you'll use them in the `.env` file in the next step.

### 4. Configure environment variables

```
# Copy the template
cp .env.template .env

# Edit .env with your credentials
# Use your favorite editor (nano, vim, VSCode, etc.)
nano .env
```

## Usage

### Scrape a Subreddit

Scrape and display information about a subreddit:

```
uv run main.py scrape <subreddit_name>
```

Examples:

```
# Scrape the Python subreddit
uv run main.py scrape python

# Scrape the ExperiencedDevs subreddit
uv run main.py scrape ExperiencedDevs

# Scrape the learnprogramming subreddit
uv run main.py scrape learnprogramming
```

Output:

```
Display Name: python
Title: Python
Description: News about the programming language Python...
```

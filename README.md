# TryHackMe Profile Stats Scraper
![Output](https://github.com/user-attachments/assets/e24f68b1-5ae4-48f9-ba7a-dcd4a6d0ba3c)

A Python program that scrapes and displays detailed user information from TryHackMe. It fetches and displays important stats such as rank, level, badges, and rooms completed.

## Features

- Retrieves user profile information from TryHackMe based on the username.
- Display key stats such as:
  - Rank Number
  - Rank Percentage
  - Completed rooms
  - Badges earned
  - Subscription status (Premium or Free)
  - User's Country


## Requirements

Before running the project, ensure you have the following dependencies installed:

- Python 3.x
- `requests` library (for the HTTP request to the API)
- `colorama` library (for the coloring the output in the console)

You can install the required libraries by running the following command:

```bash
pip install requests colorama

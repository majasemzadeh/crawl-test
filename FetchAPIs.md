
# README for Web Scraper using Playwright

## Description

This script uses Playwright to navigate to the "https://maktabkhooneh.org/learn/management-business/" URL. 
It listens to network requests and prints out the URLs of the requests that start with "https://maktabkhooneh.org/api/".

## Requirements

1. Python 3.x
2. Playwright Python library

## Installation & Setup

1. Install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).
   
2. Install the required Python packages:
    ```bash
    pip install playwright
    ```

3. Once installed, run the following command to download the necessary browsers:
    ```bash
    playwright install
    ```

## Usage

1. Save the provided code into a file, e.g., `scraper.py`.
   
2. Navigate to the directory containing the script using a terminal or command prompt.

3. Run the script:
    ```bash
    python scraper.py
    ```

4. The script will open the specified webpage in a headless browser, wait for 5 seconds, 
and then print the URLs of the requests that match the specified criteria.

## Note

Always ensure that you have permission to scrape or access the resources on the websites you are targeting. 
Respect `robots.txt` and terms of service agreements. 
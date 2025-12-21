README – Task 6: Interactive Web Scraping Program (Python)
Cognifyz Technologies – Software Development Internship
 Task Objective:

The objective of Task 6 is to develop an interactive web scraping program that allows users to fetch and display real-time data from websites using a simple web scraping library.
This task demonstrates concepts like:

1.Fetching webpage content

2.Parsing HTML

3.Extracting specific information

4.Presenting data in a user-friendly format

5.Handling user choices

Features Implemented:
✔ 1. Interactive Menu System

Users can choose between:

Scraping quotes from a quotes website

Fetching latest articles from Hacker News

Exiting the program

✔ 2. Web Scraping Using:

requests → to send HTTP requests

BeautifulSoup (bs4) → to parse and extract HTML data

✔ 3. User-Friendly Output

The program clearly displays:

Quotes with authors

Hacker News article titles + links

Clean formatting for readability

✔ 4. Error Handling Implemented

Handles internet errors

Handles parsing issues

Prevents program crash on invalid input

 Technologies Used:

a.Python 3.x

b.requests library

c.bs4 (BeautifulSoup)

d.HTML parsing

e.Menu-driven programming

How to Run the Program:
Step 1: Install Required Libraries
pip install requests
pip install beautifulsoup4

Step 2: Run the script
Task-6.py

Example Output:
===== Interactive Web Scraper =====
1. Scrape Quotes Website
2. Scrape Hacker News Articles
3. Exit
Enter your choice: 1

--- Top Quotes ---

"Life is what happens when you're busy making other plans."
 - John Lennon

Test Cases:

Test the program with different scraping options:

✔ Test 1: Quotes Website

Expected: Display 5 quotes + authors

✔ Test 2: Hacker News Website

Expected: Show 10 article titles + links

✔ Test 3: Invalid Input

Expected:

Invalid choice, please enter 1–3.

✔ Test 4: No Internet

Expected:

Error fetching quotes: <error message>

Output Demonstration Video:

The included Task-6outputvideo.mp4 demonstrates:

✔ Running the web scraper
✔ Scraping quotes
✔ Scraping news articles
✔ Handling menu options
✔ Exiting the program

This satisfies Cognifyz’s requirement for Task 6.

Conclusion:

The project successfully fulfills the requirements of Task 6 by implementing an interactive, user-friendly web scraper that:

a.Fetches data from real websites

b.Uses standard scraping libraries

c.Displays information cleanly

d.Handles errors gracefully

e.This task demonstrates practical applications of Python’s HTTP and HTML parsing capabilities.


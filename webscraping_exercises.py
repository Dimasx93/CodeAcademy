# Lesson Webscraping    10/02/2025

# Exercise n1 Your Chosen Data

# import requests
# from bs4 import BeautifulSoup

# source = requests.get("https://autoplius.lt/").text
# soup = BeautifulSoup(source, "html.parser")
# name_site = soup.find(class_="nav-leader-benefits lang-lt")
# if name_site:
#     # Find the <a> tag within the found block
#     link_tag = name_site.find("a")
#     print(link_tag)
#
#     if link_tag and link_tag.get("href"):
#         # Extract the 'href' attribute (URL)
#         ref_site = link_tag["href"]
#         print(ref_site)
#     else:
#         print("No anchor tag or href attribute found.")
# else:
#     print("Couldn't find the specified block. The class or tag might have changed.")

###########################################################################################

# Exercise n2 Extract Data From a Table

# from bs4 import BeautifulSoup
#
# data ="""
# <html>
# <body>
#   <table>
#     <tr>
#       <th>Name</th>
#       <th>Age</th>
#     </tr>
#     <tr>
#       <td>Alice</td>
#       <td>24</td>
#     </tr>
#     <tr>
#       <td>Bob</td>
#       <td>30</td>
#     </tr>
#     <tr>
#       <td>Monica</td>
#       <td>35</td>
#     </tr>
#   </table>
# </body>
# </html>
# """
#
# soup =  BeautifulSoup(data, "html.parser")
# info = soup.select("table")
# for element in info:
#     print(element.get_text().strip())

###########################################################################################

# Exercise n3 BBC News Headlines

import requests
from bs4 import BeautifulSoup
import csv

# source = requests.get("https://www.bbc.com/news").text
# soup = BeautifulSoup(source, "html.parser")
# news_links = soup.select("a[href^='/news']")
# news_headlines = soup.select("h2", id="card-headline")
# list_of_links = []
# list_of_headers = []
# for link in news_links:
#     list_of_links.append(f"https://www.bbc.com/{link.get('href')}")
# for headline in news_headlines:
#     list_of_headers.append(headline.get_text())
#
# data = zip(list_of_headers, list_of_links)
#
# with open("bbc_news.csv", "w", newline='', encoding="utf-8-sig") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Headline", "Link"])
#     writer.writerows(data)

# Site solution
# Send a request to the BBC News homepage
url = "https://www.bbc.com/news"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all elements that look like news headlines
    headlines = soup.select("a[href^='/news']")

    # Create a list to store headlines and URLs
    results = []

    # Loop through the headlines to extract text and URL
    for headline in headlines:
        headline_text = headline.get_text(strip=True)
        link = headline["href"]

        # Ensure the link is absolute
        if not link.startswith("http"):
            link = "https://www.bbc.com" + link

        # Add to the list if the headline text is not empty
        if headline_text:
            results.append((headline_text, link))
            print(f"Headline: {headline_text}, URL: {link}")

    # Write the results to a CSV file
    with open("bbc_news.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Source", "Headline", "URL"])  # Column headers
        for result in results:
            writer.writerow(["BBC"] + list(result))
        print("Results successfully written to headlines.csv.")
else:
    print("Failed to retrieve the BBC News homepage.")

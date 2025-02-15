# Task: Get/Display cat facts

import requests
import json
from http.client import responses
from bs4 import BeautifulSoup
import csv

CAT_API = "https://catfact.ninja/"


def get_cats_facts(number):
    for i in range(number):
        response = requests.get(f"{CAT_API}fact")
        if not response.ok:
            print("Bad request.")
            print(responses[response.status_code], response.status_code)
            break
        new_response = json.loads(response.text)
        print(f"{i + 1}.\t{new_response["fact"]}")


num_facts = 3
get_cats_facts(num_facts)


source = requests.get("https://books.toscrape.com/catalogue/page-1.html").text
soup = BeautifulSoup(source, "html.parser")
block = soup.select(".product_pod")

data_list = []

for book in block:
    new_list = []
    new_list.append(book.h3.a.attrs["title"])
    new_list.append(book.select_one(".price_color").text)
    new_list.append(book.p.attrs["class"][1])
    new_list.append(book.select_one(".instock").text.strip())
    data_list.append(new_list)

with open("books_scraping.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Rating", "Availability"])
    writer.writerows(data_list)

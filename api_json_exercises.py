# Lesson Web Requests & APIs  11/02/2025

# Exercise n1 Website Servers

# import requests


# def sites_headers_data(*args):
#     print("URL\t\t\t\t\t\tServer")
#     print("----------------------------------------")
#     for site in args:
#         r = requests.get(site)
#         result = r.headers
#         print(f"{r.url}\t{result['Server']}")
#
#
# sites_headers_data(
#     "https://www.google.com",
#     "https://www.microsoft.com",
#     "https://www.wikipedia.org",
#     "https://www.mozilla.org",
#     "https://www.github.com",
#     "https://www.gitlab.com",
# )

#############################################################################

# Exercise n2 Cat Photos

# import json
# import requests
#
# CAT_API = "https://api.thecatapi.com/v1"
#
#
# def get_cats_pics(number):
#     for i in range(number):
#         response = requests.get(f"{CAT_API}/images/search")
#         url = json.loads(response.content)[0]["url"]
#         response_photo = requests.get(url)
#         with open(f"cat_{i + 1}.png", "wb") as f:
#             f.write(response_photo.content)
#
#
# num_photos = int(input("Enter the number of cat photos: "))
# get_cats_pics(num_photos)
# print("Photos downloaded.")

#############################################################################

# Exercise n3 Working with JSON

# import json
#
# with open("api_json_exercise.json", "r") as file:
#     data = json.load(file)
#
# colors_list=[]
# for color in data["colors"]:
#     color_item = {
#         "color": color["color"],
#         "rgb": ",".join(map(str,color["code"]["rgba"][:-1])),
#         "hex": color["code"]["hex"],
#     }
#     colors_list.append(color_item)
#
# colors = {"colors": colors_list}
#
# with open("colors_v2.json", "w") as file:
#     json.dump(colors, file, indent=2)

#############################################################################

# Exercise n4 Currency Exchange Rates

# import requests
#
# RATE_API = "https://api.frankfurter.app/"
#
#
# def get_rate(value_1: str, value_2: str):
#     payload = {
#         "from": value_1,
#         "to": value_2,
#     }
#     r = requests.get(f"{RATE_API}/latest", params=payload)
#     result_dict = r.json()
#     try:
#         print(f"{value_1}-{value_2}:\t{result_dict['rates'][value_2]}")
#     except:
#         r = requests.get(f"{RATE_API}/currencies")
#         currencies_dict = r.json()
#         currencies = list(currencies_dict.keys())
#         print(f"Invalid currency entered. Available currencies:")
#         for i in range(0, len(currencies), 10):
#             print(*currencies[i:i + 10])
#
#
# get_rate("EUR", "GBP")
#
# get_rate("ZZZ", "GBP")

#############################################################################

# Exercise n5 Currency Exchange Rate History


# import requests
#
# API = "https://api.frankfurter.app"
#
#
# def dict_converter(dict_to_convert, to):
#     original = dict_to_convert["rates"]
#     converted = {original[date][to]: date for date in original}
#     return converted
#
#
# def get_high_low_rates(base, to, start_date, end_date):
#     payload = {
#         "from": base,
#         "to": to,
#     }
#     r = requests.get(f"{API}/{start_date}..{end_date}", params=payload)
#     result_dict = r.json()
#     try:
#         converted = dict_converter(result_dict, to)
#         max_rate = max(converted)
#         min_rate = min(converted)
#         print(
#             f"In the currency pair {base}-{to}, during the period from {start_date} to {end_date}:\n"
#             f"The lowest rate was on {converted[min_rate]} - {min_rate}\n"
#             f"The highest rate was on {converted[max_rate]} - {max_rate}"
#         )
#     except:
#         r = requests.get(f"{API}/currencies")
#         currencies_dict = r.json()
#         currencies = list(currencies_dict.keys())
#         print(f"Invalid currency entered. Available currencies:")
#         for i in range(0, len(currencies), 10):
#             print(*currencies[i: i + 10])
#
#
# get_high_low_rates("EUR", "GBP", "2024-01-01", "2024-02-01")
#
# get_high_low_rates("ZZZ", "GBP", "2024-01-01", "2024-02-01")



import requests as r
import pandas


# ---------------------------- DISCOGRAPHY MANAGER ------------------------------- #

page_number = 0
page_has_content = True

try:
    data = pandas.read_csv("discography.csv")
except FileNotFoundError:
    while page_has_content:
        page_number += 1
        response = r.get(f"https://vinniecolaiuta.com/Home/GetPageOfRecordings?page={page_number}")
        response.raise_for_status()
        data = response.json()
        if len(data) != 0:
            page = pandas.DataFrame(data).drop(columns=["$id", "id", "year", "url"]).to_csv(index=False)
            with open("discography.csv", mode="a", encoding="utf-8") as file:
                file.write(page)
        else:
            page_has_content = False
else:
    random_album = data.sample()
    print(random_album)

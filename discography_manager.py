import requests as r
import pandas as pd
import os

DISCOGRAPHY_URL = "https://vinniecolaiuta.com/Home/GetPageOfRecordings?page="


def download_page_of_discography(page_number):
    """Downloads given page of the whole discography as json data."""

    response = r.get(f"{DISCOGRAPHY_URL}{page_number}")
    response.raise_for_status()
    return response.json()


def save_json_to_csv(json_data, filename='discography.csv'):
    """Saves json_data to a CSV file called 'discography.csv'."""

    if not os.path.exists(filename):
        pd.DataFrame(json_data).drop(columns=["$id", "id", "year", "url"]).to_csv(filename, index=False)

    page = pd.DataFrame(json_data).drop(columns=["$id", "id", "year", "url"])
    page.to_csv(filename, mode="a", index=False, header=False)


def download_and_save_whole_discography():
    """Downloads all pages of the discography and saves it to a CSV file."""

    page_number = 0
    page_has_content = True

    while page_has_content:
        page_number += 1
        data = download_page_of_discography(page_number)

        if len(data) != 0:
            save_json_to_csv(json_data=data)
        else:
            page_has_content = False


def pick_random_album():
    """Picks random album from the discography inside discography.csv"""

    if not os.path.exists("discography.csv"):
        download_and_save_whole_discography()

    data = pd.read_csv("discography.csv")
    random_album = data.sample()
    print(random_album)

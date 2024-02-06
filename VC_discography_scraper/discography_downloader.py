import requests
import pandas as pd
import os


class DiscographyDownloader:
    def __init__(self, base_url):
        self.base_url = base_url
        self.page_number = 0
        self.page_has_content = True
        self.filename = '../discography.csv'

    def download_page(self, page_number):
        """Downloads given page of the whole discography as json data."""
        response = requests.get(f"{self.base_url}{page_number}")
        response.raise_for_status()
        return response.json()

    def save_to_csv(self, json_data):
        """Saves json_data to a CSV file called 'discography.csv'."""
        if not os.path.exists(self.filename):
            pd.DataFrame(json_data).to_csv(self.filename, index=False)
        else:
            page = pd.DataFrame(json_data)
            page.to_csv(self.filename, mode="a", index=False, header=False)

    def download_and_save_whole_discography(self):
        """Downloads all pages of the discography and saves it to a CSV file."""
        while self.page_has_content:
            self.page_number += 1
            data = self.download_page(self.page_number)

            if len(data) != 0:
                self.save_to_csv(data)
            else:
                self.page_has_content = False

    def pick_random_album(self):
        """Picks random album from the discography inside discography.csv"""
        if not os.path.exists(self.filename):
            self.download_and_save_whole_discography()

        data = pd.read_csv(self.filename)
        random_album = data.sample()
        return random_album

import requests
import pandas as pd
import os


class DiscographyDownloader:
    def __init__(self, base_url):
        self.base_url = base_url
        self.page_number = 0
        self.page_has_content = True
        self.filename = os.path.join(os.getcwd(), 'discography.csv')

    def download_page(self, page_number):
        """Downloads given page of the whole discography as json data."""
        print(f"Downloading page {page_number}...")
        response = requests.get(f"{self.base_url}{page_number}")
        response.raise_for_status()
        return response.json()

    def save_to_csv(self, json_data):
        """Saves json_data to a CSV file called 'discography.csv'."""
        print("Saving data to CSV...")
        if not os.path.exists(self.filename):
            print(os.getcwd())
            pd.DataFrame(json_data).to_csv(self.filename, index=False)
        else:
            page = pd.DataFrame(json_data)
            page.to_csv(self.filename, mode="a", index=False, header=False)

    def download_and_save_whole_discography(self):
        """Downloads all pages of the discography and saves it to a CSV file."""
        print("Downloading and saving whole discography...")
        while self.page_has_content:
            self.page_number += 1
            data = self.download_page(self.page_number)

            if len(data) != 0:
                self.save_to_csv(data)
                print(f"Page {self.page_number} saved to discography.csv")
            else:
                self.page_has_content = False
        print("Whole discography downloaded and saved.")

    def pick_random_album(self):
        print("Picking random album...")
        if not os.path.exists(self.filename):
            print("Downloading and saving whole discography because file doesn't exist...")
            self.download_and_save_whole_discography()

        data = pd.read_csv(
            self.filename,
            dtype=str,
            low_memory=False
        )

        data = data.dropna(subset=['artist', 'title'])  # 🔥 Odfiltruj NaNy
        data = data[data['artist'].str.strip() != '']
        data = data[data['title'].str.strip() != '']

        if data.empty:
            raise ValueError("No valid albums found in discography.")

        random_album = data.sample()

        return {
            "artist": random_album['artist'].iloc[0],
            "album_title": random_album['title'].iloc[0],
            "year": random_album['year'].iloc[0],
        }



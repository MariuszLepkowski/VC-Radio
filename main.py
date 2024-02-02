from VC_discography_scraper.discography_downloader import DiscographyDownloader

DISCOGRAPHY_URL = "https://vinniecolaiuta.com/Home/GetPageOfRecordings?page="


def main():
    discography_downloader = DiscographyDownloader(DISCOGRAPHY_URL)

    discography_downloader.pick_random_album()


if __name__ == "__main__":
    main()

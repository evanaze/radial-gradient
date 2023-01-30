"""Downloads the training data from the API."""
import csv
import logging
import requests

import click

logging.basicConfig(level=logging.DEBUG)


@click.command()
@click.option(
    "-i", "--ip-address", help="The IP address to send posts to.", default="localhost"
)
def download_data(ip_address: str):
    """Download the training data and save as a CSV."""
    logging.info("Downloading like data.")
    response = requests.get(f"http://{ip_address}:80/like")
    logging.info("First row: %s", response.json()[0])
    rows = [(row["id"], row["user_id"], row["post_id"], row["like"]) for row in response.json()]
    # Save the data to CSV
    with open("like_data.csv", "w") as outfile:
        csvwriter = csv.writer(outfile)
        csvwriter.writerow(["id", "user_id", "post_id", "like"])
        csvwriter.writerows(rows)


if __name__ == "__main__":
    download_data()

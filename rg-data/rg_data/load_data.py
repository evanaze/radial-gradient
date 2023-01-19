"""Load data into the database."""
import csv
import random
from logging import getLogger

import click
import requests

LOGGER = getLogger(__name__)
LOGGER.setLevel("INFO")


def read_csv():
    """Read the data.csv file."""
    with open("data.csv", "r") as infile:
        csvreader = csv.reader(infile)

        csvdata = []
        for line in csvreader:
            csvdata.append(line)
    return csvdata


def assign_likes(posts: list[dict]):
    """Randomly assign likes to 80% of posts."""
    random.shuffle(posts)
    for choice in range(int(len(posts) * 0.8)):
        if random.random() > 0.5:
            posts[choice]["like"] = True
        else:
            posts[choice]["like"] = False
    return posts


@click.command()
@click.option("-i", "--ip-address", help="The IP address to send posts to.", required=True)
def load_data_db(ip_address: str):
    """Load the data into the database."""
    data = read_csv()
    posts = [{"username": post[-1], "content": post[2]} for post in data]

    posts = assign_likes(posts)

    for post in posts:
        LOGGER.info("Writing post %s", post)
        requests.post(f"http://{ip_address}:80/create_post", json=post)


if __name__ == "__main__":
    load_data_db()

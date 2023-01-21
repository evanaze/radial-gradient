"""Load data into the database."""
import csv
import random
import logging

import click
import requests

logging.basicConfig(level=logging.DEBUG)


def read_csv():
    """Read the data.csv file."""
    with open("data.csv", "r") as infile:
        csvreader = csv.reader(infile)

        csvdata = []
        for line in csvreader:
            csvdata.append(line)
    return csvdata


def write_posts_to_db(posts: list[dict], ip_address: str) -> list[int]:
    """Write the posts to the database.

    :param post_ids: A list of posts to generate likes for.
    :param ip_address: The IP address of the database API.
    """
    ids = []
    for post in posts:
        logging.info("Writing post %s", post)
        response = requests.post(f"http://{ip_address}:80/create_post", json=post)
        id = response.json()["id"]
        ids.append(id)
    return ids


def generate_like_data(post_ids: list[int], ip_address: str) -> None:
    """Randomly generate like data for the content.

    :param post_ids: A list of post IDs to generate likes for.
    :param ip_address: The IP address of the database API.
    """
    n_users = 1000
    n_posts = len(post_ids)
    for user in range(n_users):
        n_likes = random.randint(1, n_posts)
        for post_id in random.sample(post_ids, n_likes):
            like_data = {
                "user_id": user,
                "post_id": post_id,
                "like": random.choice([1, -1]),
            }
            requests.post(f"http://{ip_address}:80/like", json=like_data)


@click.command()
@click.option(
    "-i", "--ip-address", help="The IP address to send posts to.", required=True
)
def load_data_db(ip_address: str):
    """Load the data into the database."""
    data = read_csv()
    posts = [{"username": post[-1], "content": post[2]} for post in data]

    post_ids = write_posts_to_db(posts, ip_address)
    generate_like_data(post_ids, ip_address)


if __name__ == "__main__":
    load_data_db()

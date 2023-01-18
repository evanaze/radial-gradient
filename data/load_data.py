"""Load data into the database."""
import csv

import click
import requests


def read_csv():
    """Read the data.csv file."""
    with open("data.csv", "r") as infile:
        csvreader = csv.reader(infile)

        csvdata = []
        for line in csvreader:
            csvdata.append(line)
    return csvdata


@click.command()
@click.option(
    "-i",
    "--ip-address",
)
def load_data_db(ip_address: str):
    """Load the data into the database."""
    data = read_csv()
    posts = [{"username": post[-1], "content": post[2]} for post in data]
    for post in posts:
        requests.post(f"http://{ip_address}/create_post", data=post)


if __name__ == "__main__":
    load_data_db()

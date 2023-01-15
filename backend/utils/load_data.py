"""Load data into the database."""
import csv

from sqlalchemy.orm import Session


def read_csv():
    """Read the data.csv file."""
    with open("data/data.csv", "r") as infile:
        csvreader = csv.reader(infile)

        csvdata = []
        for line in csvreader:
            csvdata.append(line)
    return csvdata


def load_data(db: Session):
    """Load the data."""
    data = read_csv()
    for tweet in data:
        user = tweet[-1]
        content = tweet[2]

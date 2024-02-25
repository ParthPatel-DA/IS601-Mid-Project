# Parth Patel
# Mid Term Project
# IS601 - 1J2

import json
import argparse

def read_json_file(filename):
    """Utility Function - Reads a JSON file and returns the data as a dictionary"""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')

    args = parser.parse_args()
    filename = args.filename

    data = read_json_file(filename)

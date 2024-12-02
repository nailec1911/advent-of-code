#!/usr/bin/env python3

import os
import sys
import requests

def get_session_token():
    """
    Reads the session token from a file named '.SESSION_TOKEN'.
    """
    token_file = ".SESSION_TOKEN"
    if not os.path.exists(token_file):
        print(f"Error: The file '{token_file}' was not found. Please create it and add your session token.")
        sys.exit(1)

    with open(token_file, "r", encoding="utf-8") as file:
        token = file.read().strip()

    if not token:
        print(f"Error: The file '{token_file}' is empty. Please add your session token to it.")
        sys.exit(1)

    return token


def download_input(year: int, day: int):
    """download the input from the day

    Args:
        year int: year you want to download
        day int: day you want to download
    """

    if not 1 <= day <= 25:
        print("Day number must be between 1 and 25.")
        sys.exit(1)

    # URL for the input file
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    # Headers for the request
    headers = {
        "Cookie": f"session={get_session_token()}",
        "User-Agent": "AdventOfCodeInputDownloader"
    }

    # Request the input file
    response = requests.get(url, headers=headers, timeout=3)

    if response.status_code != 200:
        print(f"Failed to download input. Status code: {response.status_code}")
        if response.status_code == 404:
            print("The puzzle might not be released yet.")
        else:
            print("Check your session token or internet connection.")
        sys.exit(1)

    print(f"Input for Day {day} downloaded successfully")

    # Create the directory for the day
    directory = f"day_{day:02}"
    os.makedirs(directory, exist_ok=True)

    # Save the input to input.txt
    inputspath = os.path.join(directory, "input.txt")
    with open(inputspath, "w", encoding="utf-8") as file:
        file.write(response.text)

    daypath = os.path.join(directory, f"day_{day:02}.py")
    with open(inputspath, "w", encoding="utf-8") as file:
        file.write("""f = [e[:-1] for e in list(open("input.txt"))]""")

    print(f"Files {inputspath} and {daypath} properly created")



if __name__ == "__main__":
    # Ensure the script is called with a day number
    if len(sys.argv) != 2 or sys.argv[1] in ["-h", "--help"]:
        print("Usage: ./download_input <dayNb>")
        sys.exit(1)

    try:
        # Parse the day number from the arguments
        dayNb = int(sys.argv[1])
        download_input(2024, dayNb)
    except ValueError:
        print("Day number must be an integer.")
        sys.exit(1)

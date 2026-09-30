from bs4 import BeautifulSoup
import csv


def extract_usernames(html_file, csv_file):
    with open(html_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    usernames = []

    for link in soup.find_all("a"):
        href = link.get("href", "")

        if "instagram.com/" in href:
            username = href.split("instagram.com/")[1]
            username = username.replace("_u/", "")
            username = username.rstrip("/")

            usernames.append(username)

    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["username"])

        for username in usernames:
            writer.writerow([username])

    print(f"Created {csv_file} with {len(usernames)} usernames.")


extract_usernames("followers.html", "followers.csv")
extract_usernames("following.html", "following.csv")


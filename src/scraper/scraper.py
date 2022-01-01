from os import sep, write
import re
import requests
import csv

from pathlib import Path

lang_re = re.compile(
    r"<a href=\"(http[s]?:\/\/(?:www.)?1000mostcommonwords.com\/"
    r"(?:words\/)?1000-most-common-\w+?-words)\">(\w+)<\/a>"
)

words_re = re.compile(r"<tr>\n<td>[0-9]+<\/td>\n<td>(.+?)<\/td>\n<td>.+?<\/td>\n<\/tr>")


def generate_csv(url_dict: dict[str]) -> None:
    csv_list = list()
    for language, url in url_dict.items():
        page = requests.get(url).text
        words = words_re.findall(page)
        if len(words) == 1000:
            words = [language,] + words
            csv_list.append(words)
    csv_list = list(map(list, zip(*csv_list)))
    with open("langs.csv", "w") as f:
        writer = csv.writer(f, delimiter=",")
        [writer.writerow(el) for el in csv_list]


def generate_url_dict(page: str) -> dict:
    return {k.lower(): v for v, k in lang_re.findall(page)}


def main():
    page = requests.get("https://1000mostcommonwords.com/").text
    url_dict = generate_url_dict(page)
    generate_csv(url_dict)


if __name__ == "__main__":
    main()

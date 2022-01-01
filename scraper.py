import re
import requests

pair_re = re.compile(
    r"<tr>\n<td>[0-9]+<\/td>\n<td>([’\s\w]+)" r"<\/td>\n<td>([’\s\w]+)<\/td>\n<\/tr>"
)


def generate_lang_dict(page):
    lang_dict = dict()
    matches = pair_re.findall(page)
    print(len(matches))
    return lang_dict


def main():
    url = "https://1000mostcommonwords.com/1000-most-common-finnish-words/"
    page = requests.get(url)
    lang_dict = generate_lang_dict(page.text)


if __name__ == "__main__":
    main()

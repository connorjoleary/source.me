import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv("./keys.env")
CUSTOM_SEARCH = os.getenv("CUSTOM_SEARCH")
SEARCH_ENGINE = os.getenv("SEARCH_ENGINE")


def run_search(query: str):
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build("customsearch", "v1", developerKey=CUSTOM_SEARCH)

    # https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
    res = service.cse().list(q=query, cx=SEARCH_ENGINE, num=3).execute()
    filtered_res = [
        {"title": i["title"], "link": i["displayLink"], "snippet": i["snippet"]}
        for i in res["items"]
    ]
    return filtered_res

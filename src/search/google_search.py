from dotenv import load_dotenv
from googleapiclient.discovery import build

from common.utils import get_env_var

load_dotenv("./keys.env")
CUSTOM_SEARCH = get_env_var("CUSTOM_SEARCH", required=True)
SEARCH_ENGINE = get_env_var("SEARCH_ENGINE", required=True)


def run_search(query: str) -> list[dict[str, str]]:
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

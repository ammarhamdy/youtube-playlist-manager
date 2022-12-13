from re import match, compile
from googleapiclient.discovery import build
from os import environ
from model.netwok_connection import check_connection


TIME_EXPRESSION = compile(r"(\d*H)?(\d*M)?(\d*S)?")
STANDER_PLAYLIST_URL = "https://www.youtube.com/playlist?list="
VALID_URL_EXPRESSION = r"https://www.youtube.com/watch\?v=[\w-]+&list=([\w-]+)(&\w+=\d+)?"


def extract_target_info(video_item):
    # (title, url, date, view, like, comment, duration)
    like_count = video_item["statistics"].get("likeCount")
    comment_count = video_item["statistics"].get("commentCount")
    return (
        video_item["id"],
        video_item["snippet"].get("title"),
        video_item["snippet"]["publishedAt"].replace("T", " ")[:-1],
        video_item["statistics"].get("viewCount"),
        "unknown" if like_count is None else like_count,
        0 if comment_count is None else comment_count,
        formate_duration(
                    video_item["contentDetails"].get("duration")
                )
    )


def formate_duration(duration):
    global TIME_EXPRESSION
    if duration is None:
        return ""
    # hours, minutes, seconds
    h, m, s = TIME_EXPRESSION.search(duration[2:]).groups()
    return f"{h[:-1] if h else 0}:{m[:-1] if m else 0}:{s[:-1] if s else 0}"


def get_playlist_id(url: str):
    # examples for url:
    # https://www.youtube.com/playlist?list=124578963
    # https://www.youtube.com/watch?v=f00Y1qqswgg&list=PLiKvEJyD4yoKIABMX4t91HOPGHbyinlwy
    # https://www.youtube.com/watch?v=f00Y1qqswgg&list=PLiKvEJyD4yoKIABMX4t91HOPGHbyinlwy&index=1
    # https://www.youtube.com/watch?v=Hlbv3lStpuc
    if url.startswith(STANDER_PLAYLIST_URL):
        return True, url[len(STANDER_PLAYLIST_URL):]
    if valid_url := match(VALID_URL_EXPRESSION, url):
        return True, valid_url.group(1)
    else:
        return False, "invalid url !"


def get_service():
    """  return the YouTube api service that used to make requests """
    # check network connection.
    if not check_connection():
        return False, "no network connection !"
    # get api key from environment variables.
    try:
        api_key = environ.get('YOUTUBE_API_KEY')
    except Exception as ex:
        print(ex)
        return False, "error while getting 'api key' !"
    # build and return the api service.
    try:
        return True, build("youtube", "v3", developerKey=api_key)
    except Exception as ex:
        print(ex)
        return False, "error while getting service !"

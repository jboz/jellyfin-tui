
import requests

api = "https://bollywood.banan4.com"
user_id = "2c7de5c00eca4ac2bc70b4e0ff55d657"
api_key = "ce6d86b7be8e42e1988a3149fafa5d82"

user_latest = api + f"/Users/{user_id}/Items/Latest"
item_primary = api + "/Item/{}/Primary"
video_streaming = "{}/Videos/{}/stream.mkv?api_key={}"

api_dict = dict(
    api_key=api_key
)
item_primary_dict = dict(
    api_key=api_key,
    fillHeight=496,
    fillWidth=331,
    quality=96
)


def getVideoStreamUrl(video_id: str):
    return video_streaming.format(api, video_id, api_key)


def getLatestVideos():
    resp = requests.get(url=user_latest, params=api_dict)
    items = resp.json()
    return map(lambda item: dict(
        id=item['Id'],
        title=item['Name'],
        year=item['ProductionYear'] if 'ProductionYear' in item else None,
        containers=item['Container']
    ), items)


if __name__ == "__main__":
    print(list(getLatestVideos()))

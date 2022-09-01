
import requests

api = "https://bollywood.banan4.com"
user_id = "2c7de5c00eca4ac2bc70b4e0ff55d657"
user_latest = api + f"/Users/{user_id}/Items/Latest"
item_primary = api + "/Item/{}/Primary"
api_dict = dict(
    api_key='ce6d86b7be8e42e1988a3149fafa5d82'
)
item_primary_dict = dict(
    api_key='ce6d86b7be8e42e1988a3149fafa5d82',
    fillHeight=496,
    fillWidth=331,
    quality=96
)


def getLatestVideos():
    resp = requests.get(url=user_latest, params=api_dict)
    items = resp.json()
    return map(lambda item: dict(
        id=item['Id'],
        name=item['Name'],
        year=item['ProductionYear'] if 'ProductionYear' in item else None,
        containers=item['Container']
    ), items)


if __name__ == "__main__":
    print(list(getLatestVideos()))

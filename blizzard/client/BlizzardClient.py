import os

import requests

from blizzard.client.TokenClient import get_oauth_token


def query_realm(namespace, name):
    return query(namespace, "/data/wow/search/connected-realm", {
        "realms.name.en_GB": name,
    })


def query(namespace, path, params=None):
    url = f"{os.getenv("BASE_URL")}{path}"

    headers = {
        "Authorization": f"Bearer {get_oauth_token()}",
        "Content-Type": "application/json",  # Adjust content type as needed
        "Battlenet-Namespace": namespace
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

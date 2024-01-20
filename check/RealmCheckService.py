import os

from blizzard.client.BlizzardClient import query_realm
from system.OSMessagingService import display_system_message


def check_realm_status():
    realm_name = os.getenv("REALM_NAME")
    realms_list = query_realm("dynamic-classic1x-eu", realm_name)["results"]
    realms = [obj for obj in realms_list if obj["data"]["realms"][0]["name"]["en_GB"] == realm_name]
    if len(realms) == 1:
        realm = realms[0]

        realm_type = realm["data"]["population"]["type"]
        print(f"Realm Type: {realm_type}")
        enemy_status = os.getenv("ENEMY_STATUS")

        if realm_type != enemy_status:
            display_system_message(f"{realm_name} has type: {realm_type}, it is not {enemy_status}!")

    else:
        print(f"Unable to find single realm with name:{realm_name}")

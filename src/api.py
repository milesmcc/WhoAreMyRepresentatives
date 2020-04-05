import requests
import random
import os

API_KEYS = os.getenv("GOOGLE_CIVICS_API_KEYS").split(",")

def get_representatives(zipcode, address):
    data = requests.get("https://www.googleapis.com/civicinfo/v2/representatives",
                     params={"address": f"{address} {zipcode}",
                             "key": random.choice(API_KEYS)}).json()

    for office in data["offices"]:
        for officialIndex in office["officialIndices"]:
            data["officials"][officialIndex]["office"] = office

    return {
        "representatives": data["officials"],
        "input": data["normalizedInput"],
    }

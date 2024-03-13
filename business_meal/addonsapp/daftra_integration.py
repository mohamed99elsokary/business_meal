import json

import requests

base_url = "https://z11z1.daftra.com/api2"
api_key = "70bbf579c3eaefee4034739df881c4d07d24369d"


def create_client(name, email):
    url = f"{base_url}/clients"

    payload = json.dumps(
        {
            "Client": {
                "business_name": name,
                "first_name": name,
                "email": email,
            }
        }
    )
    headers = {
        "APIKEY": api_key,
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    return response.get("id")

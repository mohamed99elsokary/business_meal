import requests
from decouple import config


def confirm_payment(id):
    production_status = config("PRODUCTION", default=False, cast=str)
    if production_status == "True":
        SECRET_KEY = config("LIVE_SECRET_KEY")
    else:
        SECRET_KEY = config("STAGING_SECRET_KEY")
    headers = {"Authorization": SECRET_KEY}

    response = requests.request(
        "GET", f"https://api.moyasar.com/v1/payments/{id}", headers=headers, data={}
    ).json()

    return response.get("status") == "paid"

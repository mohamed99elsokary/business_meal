import requests
from decouple import config


def confirm_payment(id):
    headers = {"Authorization": config("SECRET_KEY")}
    response = requests.request(
        "GET", f"https://api.moyasar.com/v1/payments/{id}", headers=headers, data={}
    ).json()

    return response.get("status") == "paid"

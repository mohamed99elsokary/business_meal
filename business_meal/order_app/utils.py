import requests
from decouple import config


def confirm_payment(id):
    headers = {"Authorization": config("PAYMENT_SECRET_KEY")}
    response = requests.request(
        "GET", f"https://api.moyasar.com/v1/payments/{id}", headers=headers, data={}
    ).json()

    return response.get("status") == "paid"


def payment_refund(id, amount):
    headers = {"Authorization": config("PAYMENT_SECRET_KEY")}
    requests.request(
        "POST",
        f"https://api.moyasar.com/v1/payments/{id}/refund",
        headers=headers,
        data={"amount": amount * 100},
    )

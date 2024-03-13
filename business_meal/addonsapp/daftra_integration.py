import json

import requests
from django.db.models import Case, CharField, F, When

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


def get_invoice_pdf(id):

    url = f"{base_url}/invoices/{id}"
    payload = {}
    headers = {"APIKEY": "70bbf579c3eaefee4034739df881c4d07d24369d"}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    return response["data"]["Invoice"]["invoice_pdf_url"]


def create_invoice(client_id, order_id):
    from ..order_app.models import OrderItem

    url = f"{base_url}/invoices"
    order_items = OrderItem.objects.filter(order_id=order_id).annotate(
        name=Case(
            When(meal__isnull=False, then=F("meal__name")),
            When(package__isnull=False, then=F("package__name")),
            When(hall__isnull=False, then=F("hall__name")),
            output_field=CharField(),
        ),
        price=Case(
            When(meal__isnull=False, then=F("meal__price")),
            When(package__isnull=False, then=F("package__price")),
            When(hall__isnull=False, then=F("hall__price")),
            output_field=CharField(),
        ),
    )
    items_array = [
        {"quantity": item.quantity, "item": item.name, "unit_price": item.price}
        for item in order_items
    ]
    payload = json.dumps(
        {
            "Invoice": {"client_id": client_id},
            "InvoiceItem": items_array,
        }
    )
    headers = {
        "APIKEY": api_key,
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    return get_invoice_pdf(response.get("id"))

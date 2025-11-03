import requests

# === Global Variables ===
USERNAME = "seller1"
PASSWORD = "password3"
BASE_URL = "https://rest.e-hacking.de:443/rest-api-sec/vuln_shop"
PRODUCT_ID = "1"

data = {
    "product_id": PRODUCT_ID,
    "name": "Demo Product",
    "description": "Testing safe behavior",
    "shop_id": "1",
    "price": 10.0,
    "amount": 1,
    "sold": 0,
    "picture": "https://informatik.rub.de/wp-content/uploads/2025/07/gruppenfoto_lowres-1024x663.jpg",
}

response = requests.post(
    f"{BASE_URL}/authenticate", data={"username": USERNAME, "password": PASSWORD}
)
token = response.json().get("access_token")

headers = {"Authorization": f"Bearer {token}"}
response = requests.patch(
    f"{BASE_URL}/products/{PRODUCT_ID}", headers=headers, data=data
)
print(response.json())

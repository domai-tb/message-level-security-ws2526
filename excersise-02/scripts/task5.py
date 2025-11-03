import requests
from requests.auth import HTTPBasicAuth

# === Global Variables ===
USERNAME = "natasha_romanoff"
PASSWORD = "blackwidow456"

# === API Base URL ===
BASE_URL = "https://rest.e-hacking.de/rest-api-sec/vuln_users"


def post_authenticate(username: str, password: str) -> str:
    """
    Authenticate with Basic Auth to fetch a Bearer token.
    """
    url = f"{BASE_URL}/authenticate?verifier=auth-2"
    response = requests.post(url, data={"username": username, "password": password})
    response.raise_for_status()
    print(response.json())
    token = response.json().get("access_token")
    if not token:
        raise ValueError("Authentication failed or no access token received.")
    return token


def get_authenticate(username: str, password: str) -> str:
    """
    Authenticate using HTTP Basic auth via GET /authenticate?verifier=auth-2
    and return the bearer/access token from the JSON response.
    """
    url = f"{BASE_URL}/authenticate"
    params = {"verifier": "auth-2"}
    resp = requests.get(
        url, params=params, auth=HTTPBasicAuth(username, password), timeout=15
    )
    print(resp.json())
    token = resp.json().get("access_token")
    if not token:
        raise ValueError("Authentication failed or no access token received.")
    return token


def get_user_info(token: str):
    """
    Get the authenticated user's information using /users/user.
    """
    url = f"{BASE_URL}/users/user?verifier=auth-2"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(response.json())
    response.raise_for_status()
    return response.json()


def main():
    print("[*] Authenticating...")
    token = get_authenticate(USERNAME, PASSWORD)
    print(f"[+] Access Token: {token}")


if __name__ == "__main__":
    main()

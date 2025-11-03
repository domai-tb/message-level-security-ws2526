import requests
from typing import Optional, List, Dict

# === Global credentials ===
USERNAME = "bgreen"
PASSWORD = "password5"

# === API base from the OpenAPI JSON provided ===
BASE_URL = "https://rest.e-hacking.de:443/rest-api-sec/vuln_reports"

# Defaults used by the OpenAPI spec (verifier can usually be empty/1/secure)
VERIFIER = "1"  # the spec allows allowEmptyValue; change if needed


def authenticate(username: str, password: str, verifier: str = VERIFIER) -> str:
    """
    Authenticate using POST /authenticate (form data username/password).
    Returns the Bearer token (accessToken) on success.
    Raises requests.HTTPError on failure.
    """
    url = f"{BASE_URL}/authenticate"
    params = {"verifier": verifier}
    data = {"username": username, "password": password}
    resp = requests.post(url, params=params, data=data, timeout=15)
    print(resp.json())
    resp.raise_for_status()
    token = resp.json().get("access_token")
    if not token:
        # if server returns full user info with accessToken field nested, try common keys
        # otherwise return empty and let caller decide
        raise ValueError("No access token found in authentication response: %s" % j)
    return token


def get_user_info(token: str, verifier: str = VERIFIER) -> Dict:
    """
    GET /user - returns authenticated user's info (id, role, ...)
    """
    url = f"{BASE_URL}/user"
    params = {"verifier": verifier}
    headers = {"authorization": f"Bearer {token}"}
    resp = requests.get(url, params=params, headers=headers, timeout=15)
    print(resp.json())
    resp.raise_for_status()
    return resp.json()


def get_my_reports(token: str, verifier: str = VERIFIER) -> List[Dict]:
    """
    GET /reports - returns reports created by the user according to the spec.
    """
    url = f"{BASE_URL}/reports"
    params = {"verifier": verifier}
    headers = {"authorization": f"Bearer {token}"}
    resp = requests.get(url, params=params, headers=headers, timeout=15)
    resp.raise_for_status()
    j = resp.json()
    # The response format is not strictly defined in the snippet; try common possibilities:
    # - a list of report objects
    # - an object with "reports" key, or "data" key
    if isinstance(j, list):
        return j
    if isinstance(j, dict):
        for k in ("reports", "data", "items"):
            if k in j and isinstance(j[k], list):
                return j[k]
        # If it's a single object for one report, wrap it
        if "id" in j and "content" in j:
            return [j]
    return []


def update_report_name(
    token: str, report_id: str, new_name: str, verifier: str = VERIFIER
) -> Dict:
    """
    PATCH /reports
    Request body (form-encoded) expects at least reportId. To change name, include 'name'.
    Returns the parsed JSON response.
    """
    url = f"{BASE_URL}/reports"
    params = {"verifier": verifier}
    headers = {"authorization": f"Bearer {token}"}
    data = {"reportId": str(report_id), "name": new_name}
    resp = requests.patch(url, params=params, headers=headers, data=data, timeout=15)
    resp.raise_for_status()
    # may or may not return JSON, try to parse:
    if resp.content:
        try:
            return resp.json()
        except ValueError:
            return {"raw": resp.text}
    return {}


def main():
    print("[*] Authenticating...")
    try:
        token = authenticate(USERNAME, PASSWORD)
    except Exception as e:
        print("[!] Authentication failed:", e)
        return

    print(
        "[+] Obtained access token:",
        token[:40] + "..." if len(token) > 40 else token,
    )

    # 1) What is your user's ID and role?
    try:
        user_info = get_user_info(token)
    except Exception as e:
        print("[!] Failed to fetch user info (/user):", e)
        user_info = {}

    user_id = (
        user_info.get("id")
        or user_info.get("userId")
        or user_info.get("accessToken")
        and None
    )
    role = user_info.get("role")
    print("\n=== Authenticated user info ===")
    if user_info:
        print("Full user info (raw):", user_info)
    if user_id:
        print("User ID:", user_id)
    else:
        print("User ID: (not present in response)")

    if role:
        print("Role:", role)
    else:
        print("Role: (not present in response)")

    # 2) Name the ids of your own reports.
    print("\n[*] Querying your reports (/reports)...")
    try:
        reports = get_my_reports(token)
    except Exception as e:
        print("[!] Failed to fetch reports:", e)
        reports = []

    report_ids = []
    for r in reports:
        if isinstance(r, dict):
            rid = (
                r.get("id")
                or r.get("reportId")
                or r.get("reportID")
                or r.get("creatorId")
                and None
            )
            report_ids.append(rid)
    print("Your reports (raw objects):", reports)
    print("Report IDs found:", [r for r in report_ids if r is not None])

    print("\nDone.")


if __name__ == "__main__":
    main()

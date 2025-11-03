# Excersise 1

## Task 1

a) 2

b) `api_key: apiKey`

c) `api_key`

d) Neah, API-keys are still common practice but "dynamic" authentication token like JWTs / SSO-based authentication would be more secure (if correctly configured).

e)

```
Paths that support XML input data:
- /routing/{versionNumber}/calculateReachableRange/{origin}/{contentType}
- /routing/{versionNumber}/calculateRoute/{locations}/{contentType}
```

f) Number of endpoints with variables in the path: 2

## Task 2

a) 12

b)

```
Supported API version(s):
- 1.1
```

c)

```
Paths requiring Bearer authentication:
- /users/userinfo
- /users/{id}
- /users/change_password/{id}
- /users/update_userinfo
- /admins/users
- /admins/update_userinfo/{id}
- /admins/create_user
- /tokens/list
- /tokens/revoke
```

d)

```
Paths allowing Basic authentication:
- /authenticate
```

e)

```
Paths without any defined authentication mechanism:
- /companies/{id}
- /reset
```

## Task 3

a)

The endpoints gives for some reason always `invalid access_token` as response.
Multiple resets couldn't help. The script to implement this is [task3_users.py](./task3_users.py).

```
❯ python task3.py
[*] Authenticating...
{'id': '2', 'name': 'natasha_romanoff', 'access_token': 'bafcd0d2-42bd-4e16-88cc-e6416eef3d11'}
[+] Access Token: bafcd0d2-42bd-4e16-88cc-e6416eef3d11
[*] Fetching user info...
{'error': 'Invalid Access Token'}
Traceback (most recent call last):
  File "/home/domai/Coding/message-level-security-ws2526/excersise-02/task3.py", line 53, in <module>
    main()
    ~~~~^^
  File "/home/domai/Coding/message-level-security-ws2526/excersise-02/task3.py", line 47, in main
    user_info = get_user_info(token)
  File "/home/domai/Coding/message-level-security-ws2526/excersise-02/task3.py", line 37, in get_user_info
    response.raise_for_status()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3.13/site-packages/requests/models.py", line 1026, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 400 Client Error: Bad Request for url: https://rest.e-hacking.de:443/rest-api-sec/vuln_users/users/user?verifier=secure
```

b)

The endpoints gives for some reason always `invalid access_token` as response.
Multiple resets couldn't help. The script to implement this is [task3_reports.py](./task3_reports.py).

```
❯ python task3_reports.py
[*] Authenticating...
{'id': '5', 'name': 'bgreen', 'access_token': '52d44381-5022-4e9d-885b-79c2756b8da3'}
[+] Obtained access token: 52d44381-5022-4e9d-885b-79c2756b8da3
{'error': 'Invalid Access Token'}
[!] Failed to fetch user info (/user): 401 Client Error: Unauthorized for url: https://rest.e-hacking.de:443/rest-api-sec/vuln_reports/user?verifier=1

=== Authenticated user info ===
User ID: (not present in response)
Role: (not present in response)

[*] Querying your reports (/reports)...
[!] Failed to fetch reports: 400 Client Error: Bad Request for url: https://rest.e-hacking.de:443/rest-api-sec/vuln_reports/reports?verifier=1
Your reports (raw objects): []
Report IDs found: []

Done.
```

iii)

- Yes. The endpoint to update an existing report's properties (including the `name`) is:
  HTTP method: PATCH
  Path: /reports (server base) -> full path: https://rest.e-hacking.de:443/rest-api-sec/vuln_reports/reports
- You must supply an Authorization header with `Bearer <access_token>` and include form data with at least `reportId`.
- To change the name include the `name` field in the form body.

## Task 4

a) See [task4_bola1.py](../task4_bola1.py)

```
❯ python task4_bola1.py
[*] Authenticating...
{'id': '2', 'name': 'natasha_romanoff', 'access_token': 'aa570f7e-be8e-4c3e-9225-ee627a2e4d69'}
[+] Access Token: aa570f7e-be8e-4c3e-9225-ee627a2e4d69
[*] Fetching user info...
{'id': '4', 'username': 'bruce_wayne', 'company_id': 'meta', 'role': 'admin', 'address': 'Gotham'}
User ID: 4
Role: admin
```

b) See [task4_bola2.py](../task4_bola2.py)

The endpoints gives for some reason always `invalid access_token` as response.
Multiple resets couldn't help. The script to implement this is [task4_bola2.py](./task4_bola2.py).

```
❯ python task4_bola2.py
[*] Authenticating...
{'id': '2', 'name': 'natasha_romanoff', 'access_token': '2b73d2a8-3c44-4a96-86aa-23d4ddf41f4a'}
[+] Access Token: 2b73d2a8-3c44-4a96-86aa-23d4ddf41f4a
[*] Get user info...
{'error': 'Invalid Access Token'}
Traceback (most recent call last):
  File "/home/domai/Coding/message-level-security-ws2526/excersise-02/scripts/task4_bola2.py", line 79, in <module>
    main()
    ~~~~^^
  File "/home/domai/Coding/message-level-security-ws2526/excersise-02/scripts/task4_bola2.py", line 72, in main
    get_user_info(token)
    ~~~~~~~~~~~~~^^^^^^^
  File "/home/domai/Coding/message-level-security-ws2526/excersise-02/scripts/task4_bola2.py", line 36, in get_user_info
    response.raise_for_status()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3.13/site-packages/requests/models.py", line 1026, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 400 Client Error: Bad Request for url: https://rest.e-hacking.de/rest-api-sec/vuln_users/users/user?verifier=bola-2
```

## Task 5

See [task5.py](../scripts/task5.py)

```
❯ python task5.py
[*] Authenticating...
{'id': '2', 'name': 'natasha_romanoff', 'access_token': 'eyJ0eXAiOiJKV1QiLCJnaWQiOiI3MDE3MmU0NS0wODNkLTQ2YmItYjU2Mi0yNTc2ZjhjMzkxYjQiLCJhbGciOiJSUzI1NiIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6InNpZyIsImtpZCI6IjU1ODc3YWZhLTM0ZjUtNDRkZS1hNmQyLTdlYjcxZDUyNzdiYyIsIm4iOiJ1cnUyeTc3RXRWdWJBUUhBaU9yR1hWNWlwNDY0eTRGRzFvLWoxVmdsLWZzZUhidEZxY3B3RnpfZ2NMUTJjaEVPeFF0N1E2VHA3WG1qTGowc1dCeWptQ2ZQWUNrWVpPSnBtb2lDaEhHY3hqYU1XaWhUamdyejRuWC1qWU5oUzZTLUlpSHBCRDFzalRveVc2OHJtTzJSQ0pqZUw0QnpKRlctTVY2TlVCcEFta244M0VYYzM1QlBiWEtWT2MzaThQUDVVYkstV0RwWE11U3l0eXFhUHlDeklOT3cyUXVxaTdMY2dveFdZaG1Cakd0RHRGYUoyX28yZEVIcHFTNUp4bG01aVV5RGdocEdJMk1jb0w4bXVwOXNlQ21ITTBRc2xBMndnNlotNlRaUVRNU3NLd0dXQy1RWVdZclRoM0x5TFpUS2JRLXYtRDdoTEtHaTUteExveWN3SFEifSwia2lkIjoiNTU4NzdhZmEtMzRmNS00NGRlLWE2ZDItN2ViNzFkNTI3N2JjIn0.ewogICJpZCI6ICIyIiwKICAidXNlcm5hbWUiOiAibmF0YXNoYV9yb21hbm9mZiIsCiAgImNvbXBhbnlfaWQiOiAiYXBwbGUiLAogICJyb2xlIjogIm5vcm1hbCIsCiAgImFkZHJlc3MiOiAiTW9zY293Igp9.I-F-HY1lTRnjtPiroAIowL0NlCNs5_NKavmq7cLTxpDmFsMcoGcX040mQsqShLhqxDgrfbWwn_QtU5FXZGP8AOmxsGOnzRg23PQUbKiJWb_qjmUUhdmx94x_yHJD8N_BQUZScGz5DETMEMK31JAThgXaaUUtik6z0LuWbGygUGBnZ6CnpKl45VXmXpeE1kTyVSss_wqwy2YME1q7A0S_qaHQlXeXiru8Xf9kexESIyt_DETyt6OH2i8p-vqUmoFqcsLFOvA0KhSlxpNY-3J_AGixxNxTYJZduHSg-8BFbfvwGJveMaloNSPvR9fjNe41Y9TAFQJku-7OjU7fSn0yqw'}
[+] Access Token: eyJ0eXAiOiJKV1QiLCJnaWQiOiI3MDE3MmU0NS0wODNkLTQ2YmItYjU2Mi0yNTc2ZjhjMzkxYjQiLCJhbGciOiJSUzI1NiIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6InNpZyIsImtpZCI6IjU1ODc3YWZhLTM0ZjUtNDRkZS1hNmQyLTdlYjcxZDUyNzdiYyIsIm4iOiJ1cnUyeTc3RXRWdWJBUUhBaU9yR1hWNWlwNDY0eTRGRzFvLWoxVmdsLWZzZUhidEZxY3B3RnpfZ2NMUTJjaEVPeFF0N1E2VHA3WG1qTGowc1dCeWptQ2ZQWUNrWVpPSnBtb2lDaEhHY3hqYU1XaWhUamdyejRuWC1qWU5oUzZTLUlpSHBCRDFzalRveVc2OHJtTzJSQ0pqZUw0QnpKRlctTVY2TlVCcEFta244M0VYYzM1QlBiWEtWT2MzaThQUDVVYkstV0RwWE11U3l0eXFhUHlDeklOT3cyUXVxaTdMY2dveFdZaG1Cakd0RHRGYUoyX28yZEVIcHFTNUp4bG01aVV5RGdocEdJMk1jb0w4bXVwOXNlQ21ITTBRc2xBMndnNlotNlRaUVRNU3NLd0dXQy1RWVdZclRoM0x5TFpUS2JRLXYtRDdoTEtHaTUteExveWN3SFEifSwia2lkIjoiNTU4NzdhZmEtMzRmNS00NGRlLWE2ZDItN2ViNzFkNTI3N2JjIn0.ewogICJpZCI6ICIyIiwKICAidXNlcm5hbWUiOiAibmF0YXNoYV9yb21hbm9mZiIsCiAgImNvbXBhbnlfaWQiOiAiYXBwbGUiLAogICJyb2xlIjogIm5vcm1hbCIsCiAgImFkZHJlc3MiOiAiTW9zY293Igp9.I-F-HY1lTRnjtPiroAIowL0NlCNs5_NKavmq7cLTxpDmFsMcoGcX040mQsqShLhqxDgrfbWwn_QtU5FXZGP8AOmxsGOnzRg23PQUbKiJWb_qjmUUhdmx94x_yHJD8N_BQUZScGz5DETMEMK31JAThgXaaUUtik6z0LuWbGygUGBnZ6CnpKl45VXmXpeE1kTyVSss_wqwy2YME1q7A0S_qaHQlXeXiru8Xf9kexESIyt_DETyt6OH2i8p-vqUmoFqcsLFOvA0KhSlxpNY-3J_AGixxNxTYJZduHSg-8BFbfvwGJveMaloNSPvR9fjNe41Y9TAFQJku-7OjU7fSn0yqw
```

JWT decoded:

```
{
    "typ": "JWT",
    "gid": "70172e45-083d-46bb-b562-2576f8c391b4",
    "alg": "RS256",
    "jwk": {
        "kty": "RSA",
        "e": "AQAB",
        "use": "sig",
        "kid": "55877afa-34f5-44de-a6d2-7eb71d5277bc",
        "n": "uru2y77EtVubAQHAiOrGXV5ip464y4FG1o-j1Vgl-fseHbtFqcpwFz_gcLQ2chEOxQt7Q6Tp7XmjLj0sWByjmCfPYCkYZOJpmoiChHGcxjaMWihTjgrz4nX-jYNhS6S-IiHpBD1sjToyW68rmO2RCJjeL4BzJFW-MV6NUBpAmkn83EXc35BPbXKVOc3i8PP5UbK-WDpXMuSytyqaPyCzINOw2Quqi7LcgoxWYhmBjGtDtFaJ2_o2dEHpqS5Jxlm5iUyDghpGI2McoL8mup9seCmHM0QslA2wg6Z-6TZQTMSsKwGWC-QYWYrTh3LyLZTKbQ-v-D7hLKGi5-xLoycwHQ"
    },
    "kid": "55877afa-34f5-44de-a6d2-7eb71d5277bc"
}
{
    "id": "2",
    "username": "natasha_romanoff",
    "company_id": "apple",
    "role": "normal",
    "address": "Moscow"
}
```

=> Most likely a key confusion attack: Replace public key of JWT header with own public key and sign with own private key. The payload can than be whatever we want, e.g. admin role

## Task 6

No time

## Task 7

No time

## Task 8

Patching product allow to insert own URLs. See [task8.py](../scripts/task8.py).

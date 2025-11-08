# Excersise 1

## Task 1

a) 2

b) `api_key: apiKey`

c) `api_key`

d) Neah, API-keys are still common practice but "dynamic" authentication token like JWTs / SSO-based authentication would be more secure (if correctly configured).
The tomtom API uses HTTPS, the sending the API key via query itself would be fine. One issue would be, for example, logging via the browser history. 
This makes the aforementioned authentication methods preferable.

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
- v1.0
- v1.1
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
- /authenticate (POST) (no 'security:' attribute)
- /companies/{id}
- /reset
```

## Task 3
a)
The "Vulnerable Users API" Postman collection was used via Bruno.
i)

- Using the credentials for the `natasha_romanoff` user, `/authenticate` returns `"id": "2"` and an `access_token`.
- Using the `access_token`, `/users/user` returns `"role": "normal"`

ii)
The "Vulnerable Users API" Postman collection was used via Bruno.

```
- Given a valid `access_token`, /users/user provides both id and role.
- Given a valid id and `access_token`, /users/user/{id} provides both id and role for the authenticated user.
- Given valid credentials, /authenticate only provides the id.
```

b)
The "Vulnerable Reports API" Postman collection was used via Bruno.
i)
- Using the credentials for the `bgreen` user, `/authenticate` returns `"id": "5"` and an `access_token`.
- Using the `access_token`, `/user` returns `"role": "employee"`

ii)
- Using the `access_token`, `/reports` (GET) returns reports with `"id": 4` and `"id": 9`
- 
iii)
- Yes. The endpoint to update an existing report's properties (including the `name`) is:
  HTTP method: PATCH
  Path: /reports (server base) -> full path: https://rest.e-hacking.de:443/rest-api-sec/vuln_reports/reports
- You must supply an Authorization header with `Bearer <access_token>` and include form data with at least `reportId`.
- To change the name include the `name` field in the form body.

c)
The "Vulnerable Reports API" Postman collection was used via Bruno.
i)
- Using the credentials for the `user1` user, `/authenticate` returns `"id": "12345678"` and an `access_token`.
- Using the `access_token`, `/users` returns `"role": "customer"`

ii)
- Using the `access_token`, `/users/shops` returns `[]`. The user does not own any shops.

iii)
- Using the `/shops` Endpoint, one can see that the shop `Adventure Goods` has the id `87654325`
- Using the `/shops/{shop_id}` Endpoint using the `access_token`, looking up the id `87654325` returns the user id `45678901` as owner

iv)
- Using the `/shops` Endpoint, one can see that the shop `Bike World` has the id `87654322`
- Using the `/shops/{shop_id}/products` Endpoint using the `access_token` and looking up the id `87654322`, one can see that the BMX costs 300 (Dollars? Euros?)

## Task 4

The "Vulnerable Reports API" Postman collection was used via Bruno.
i)
- Using the credentials for the `bgreen` user, `/authenticate` returns an `access_token` and `"id": "5"`.

ii)
- Using the credentials for the `bgreen` user, `/authenticate` returns an `access_token` and `"id": "5"`.
  - Using the `access_token`, the `/user` Endpoint returns that `bgreen` has the `role` "employee", thus is only able to see his own reports.
- Using the `access_token`, the `/reports` Endpoint returns, that the user created the reports with the ids `4` and `9`.
- However, using the `/reports/{reportId}` endpoint, using `reportId` 1, a report from the user with `"creator_id": 2` gets returned. The user with that `id` is the user `asmith` with the `role` "manager".
   - All other reports (except 4 and 9) return `"error": "Not allowed to see report from a different department!"`

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

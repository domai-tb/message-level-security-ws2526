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

- Set `alg` to `none` and remove signature: `FLAG{json_signature_verifier_2_RWHiX1ifds0GqpKl}`
- Set `alg` to `NoNe` (and let signature attached): `FLAG{json_signature_verifier_3_4dwCLnHa81FguV49}`
- 

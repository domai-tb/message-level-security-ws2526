#!/usr/bin/env bash
# Extract x5c from a JWT file and print it using OpenSSL.
# Handles both X.509 certificates and plain public keys.

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <jwt_file>"
  exit 1
fi

JWT_FILE="$1"
if [[ ! -f "$JWT_FILE" ]]; then
  echo "Error: File not found: $JWT_FILE"
  exit 1
fi

# Read and normalize JWT
JWT=$(tr -d '\n\r ' < "$JWT_FILE")

# Extract header (first part of JWT)
HEADER_B64=$(echo "$JWT" | cut -d '.' -f1)

# Decode base64url → base64 → JSON
HEADER_JSON=$(echo "$HEADER_B64" | tr '_-' '/+' | base64 -d 2>/dev/null)

echo "----- JWT Header -----"
echo "$HEADER_JSON" | jq . 2>/dev/null || echo "$HEADER_JSON"
echo

# Extract x5c values (string or array)
X5C_ENTRIES=$(echo "$HEADER_JSON" | jq -r '
  if .x5c | type == "array" then .x5c[]
  elif .x5c | type == "string" then .x5c
  else empty end
' 2>/dev/null)

if [[ -z "$X5C_ENTRIES" ]]; then
  echo "No x5c value found in JWT header."
  exit 0
fi

count=1
while IFS= read -r der_b64; do
  echo -e "----- Entry $count -----\n"
  TMP_DER=$(mktemp)

  echo "$der_b64" | base64 --decode > "$TMP_DER" || {
    echo "Error: Failed to decode base64 data"
    rm -f "$TMP_DER"
    exit 1
  }

  # Try to interpret as a certificate first
  if openssl x509 -in "$TMP_DER" -inform DER -noout -text 2>/dev/null; then
    echo "(interpreted as X.509 certificate)"
  else
    # Try as a public key
    if openssl pkey -in "$TMP_DER" -inform DER -pubin -text_pub 2>/dev/null; then
      echo "(interpreted as DER-encoded public key)"
    else
      echo "Error: Could not interpret x5c entry $count (not a valid cert or key)"
    fi
  fi

  rm -f "$TMP_DER"
  echo
  ((count++))
done <<< "$X5C_ENTRIES"

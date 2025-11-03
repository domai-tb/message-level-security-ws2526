import json
import sys


def parse_openapi(filepath):
    """Load the OpenAPI JSON file."""
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file at {filepath} is not a valid JSON.")
        return None


def count_paths(openapi_data):
    """Count the number of paths in the OpenAPI specification."""
    paths = openapi_data.get("paths", {})
    return len(paths)


def get_api_versions(openapi_data):
    """Return the version(s) of the API if defined."""
    versions = set()
    if "info" in openapi_data:
        version = openapi_data["info"].get("version")
        if version:
            versions.add(version)
    return list(versions)


def get_authentication_methods_for_paths(openapi_data):
    """Check authentication methods used for each path."""
    paths_auth = {"bearer": [], "basic": [], "no_auth": []}

    # Check the paths for security requirements
    for path, methods in openapi_data.get("paths", {}).items():
        requires_bearer = False
        requires_basic = False
        has_auth = False

        for method, details in methods.items():
            security = details.get("security", [])
            if security:
                has_auth = True
                for sec_scheme in security:
                    if "bearerAuth" in sec_scheme:
                        requires_bearer = True
                    if "basicAuth" in sec_scheme:
                        requires_basic = True

        if requires_bearer:
            paths_auth["bearer"].append(path)
        elif requires_basic:
            paths_auth["basic"].append(path)
        elif not has_auth:
            paths_auth["no_auth"].append(path)

    return paths_auth


def main(filepath):
    openapi_data = parse_openapi(filepath)
    if openapi_data is None:
        return

    # 1. How many API paths are defined?
    num_paths = count_paths(openapi_data)
    print(f"Number of API paths: {num_paths}")

    # 2. Does the API support different versions? If yes, name all of them.
    versions = get_api_versions(openapi_data)
    if versions:
        print("Supported API version(s):")
        for version in versions:
            print(f"- {version}")
    else:
        print("No version information found in the API specification.")

    # 3. Which API path(s) require HTTP Bearer authentication?
    auth_paths = get_authentication_methods_for_paths(openapi_data)
    if auth_paths["bearer"]:
        print("Paths requiring Bearer authentication:")
        for path in auth_paths["bearer"]:
            print(f"- {path}")
    else:
        print("No paths require Bearer authentication.")

    # 4. Which API path(s) allow Basic authentication?
    if auth_paths["basic"]:
        print("Paths allowing Basic authentication:")
        for path in auth_paths["basic"]:
            print(f"- {path}")
    else:
        print("No paths allow Basic authentication.")

    # 5. Which API path(s) do not require any authentication mechanism defined in the OpenAPI specification?
    if auth_paths["no_auth"]:
        print("Paths without any defined authentication mechanism:")
        for path in auth_paths["no_auth"]:
            print(f"- {path}")
    else:
        print("All paths require authentication.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_openapi_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    main(filepath)

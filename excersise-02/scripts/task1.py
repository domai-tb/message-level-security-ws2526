import json
import sys


def parse_openapi(filepath):
    # Open and load the JSON file
    try:
        with open(filepath, "r") as file:
            openapi_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file at {filepath} is not a valid JSON.")
        return None

    return openapi_data


def count_paths(openapi_data):
    paths = openapi_data.get("paths", {})
    return len(paths)


def get_authentication_methods(openapi_data):
    # Check if security definitions exist in the OpenAPI spec
    security_schemes = openapi_data.get("components", {}).get("securitySchemes", {})
    auth_methods = []

    for scheme_name, scheme_details in security_schemes.items():
        auth_methods.append((scheme_name, scheme_details.get("type", "unknown")))

    return auth_methods


def get_default_security(openapi_data):
    # Check if security definitions are applied globally
    default_security = openapi_data.get("security", [])
    return default_security


def get_paths_that_support_xml(openapi_data):
    # Find paths that support XML input (application/xml in requestBody content type)
    paths_with_xml = []

    for path, methods in openapi_data.get("paths", {}).items():
        for method, details in methods.items():
            request_body = details.get("requestBody", {})
            content = request_body.get("content", {})
            if "application/xml" in content:
                paths_with_xml.append(path)
                break  # No need to check other methods for this path

    return paths_with_xml


def count_path_variables(openapi_data):
    # Count how many paths have variables in the path (e.g., /users/{userId})
    variable_count = 0
    for path in openapi_data.get("paths", {}):
        if "{" in path and "}" in path:
            variable_count += 1
    return variable_count


def main(filepath):
    openapi_data = parse_openapi(filepath)
    if openapi_data is None:
        return

    # 1. How many API paths are defined?
    num_paths = count_paths(openapi_data)
    print(f"Number of API paths: {num_paths}")

    # 2. Which authentication mechanisms are specified?
    auth_methods = get_authentication_methods(openapi_data)
    print("Authentication mechanisms:")
    for name, auth_type in auth_methods:
        print(f"- {name}: {auth_type}")

    # 3. Which authentication methods are applied by default on all paths?
    default_security = get_default_security(openapi_data)
    if default_security:
        print("Default authentication mechanisms applied to all paths:")
        for security in default_security:
            print(security)
    else:
        print("No default authentication mechanisms applied.")

    # 4. Which paths support XML input data?
    xml_paths = get_paths_that_support_xml(openapi_data)
    if xml_paths:
        print("Paths that support XML input data:")
        for path in xml_paths:
            print(f"- {path}")
    else:
        print("No paths support XML input data.")

    # 5. How many endpoints allow variables in the path?
    num_variables = count_path_variables(openapi_data)
    print(f"Number of endpoints with variables in the path: {num_variables}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_openapi_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    main(filepath)

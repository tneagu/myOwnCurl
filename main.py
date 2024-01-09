import argparse
from urllib.parse import urlparse

import requests

parser = argparse.ArgumentParser(description="My own curl implemenation")
parser.add_argument("url", help="Name of the url")

args = parser.parse_args()
fullUrl = args.url

# Parse the URL
parsed_url = urlparse(fullUrl)

# Extract components
schema = parsed_url.scheme
url = parsed_url.netloc
port = parsed_url.port

# Log to the console schema, url, port
print("Schema:", schema)
print("URL:", url)
print("Port:", port)

# validate schema to be supported one
if (schema != "http" and schema != "https"):
    raise ValueError("Incorrect url schema. This script supports only http and https")

# make network call
response = requests.get(fullUrl)
if response.status_code == 200:
    content = response.text
    print(content)
else:
    print(f"Error: {response.status_code}")

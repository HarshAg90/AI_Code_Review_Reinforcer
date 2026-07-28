# import requests

# url = "https://64cc-2401-4900-1c55-4adc-212b-db4b-e4f2-36e0.ngrok-free.app/data?key1=value1&key2=value2"

# response = requests.get(url)
import json
import os
import requests

# -------------------------------------------------------
# Read GitHub Event Payload
# -------------------------------------------------------

event_path = os.environ["GITHUB_EVENT_PATH"]

with open(event_path, "r") as f:
    event = json.load(f)

print(event)
pull_number = event["pull_request"]["number"]

repository = os.environ["GITHUB_REPOSITORY"]

token = os.environ["GITHUB_TOKEN"]

owner, repo = repository.split("/")

print(f"Repository : {repository}")
print(f"PR Number  : {pull_number}")

# -------------------------------------------------------
# Request Changed Files
# -------------------------------------------------------

url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

response = requests.get(url, headers=headers)

response.raise_for_status()

files = response.json()

print(f"\nFound {len(files)} changed files\n")

# -------------------------------------------------------
# Print Information
# -------------------------------------------------------

for file in files:

    print("=" * 60)

    print("Filename :", file["filename"])
    print("Status   :", file["status"])
    print("Additions:", file["additions"])
    print("Deletions:", file["deletions"])
    print("Changes  :", file["changes"])

    print("\nPatch:\n")

    print(file.get("patch", "<No patch available>"))

    print()
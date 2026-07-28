# import requests

# url = "https://64cc-2401-4900-1c55-4adc-212b-db4b-e4f2-36e0.ngrok-free.app/data?key1=value1&key2=value2"

# response = requests.get(url)
import json
import os
import requests

# -------------------------------------------------------
# Read GitHub Event Payload
# -------------------------------------------------------
import json
import os
import requests

# -------------------------------------------------------
# Read GitHub Event
# -------------------------------------------------------

with open(os.environ["GITHUB_EVENT_PATH"], "r") as f:
    event = json.load(f)

event_name = os.environ["GITHUB_EVENT_NAME"]

repository = os.environ["GITHUB_REPOSITORY"]
token = os.environ["GITHUB_TOKEN"]

owner, repo = repository.split("/")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

print(f"Event      : {event_name}")
print(f"Repository : {repository}")

# =======================================================
# PULL REQUEST
# =======================================================

if event_name == "pull_request":

    pull_number = event["pull_request"]["number"]

    print(f"PR Number  : {pull_number}")

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    files = response.json()

# =======================================================
# PUSH
# =======================================================

elif event_name == "push":

    before = event["before"]
    after = event["after"]

    print(f"Commit Before : {before}")
    print(f"Commit After  : {after}")

    url = (
        f"https://api.github.com/repos/{owner}/{repo}"
        f"/compare/{before}...{after}"
    )

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    comparison = response.json()

    files = comparison["files"]

# =======================================================
# UNKNOWN
# =======================================================

else:
    raise Exception(f"Unsupported event: {event_name}")

# -------------------------------------------------------
# Print Changed Files
# -------------------------------------------------------

print(f"\nFound {len(files)} changed files\n")

for file in files:

    print("=" * 60)
    print("Filename :", file["filename"])
    print("Status   :", file["status"])

    if "patch" in file:
        print("\nPatch:\n")
        print(file["patch"])
import sys
import json
import urllib.request
import urllib.error
import os

def fetch_orcid_data(orcid):
    url = f"https://pub.orcid.org/v3.0/{orcid}"
    req = urllib.request.Request(url, headers={'Accept': 'application/json'})

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))

        os.makedirs('data', exist_ok=True)
        filepath = f"data/orcid_{orcid}.json"

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Successfully fetched ORCID data for {orcid} and saved to {filepath}")

    except urllib.error.URLError as e:
        print(f"Error fetching ORCID data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        orcid = sys.argv[1]
    else:
        orcid = "0000-0003-2645-2585"

    fetch_orcid_data(orcid)

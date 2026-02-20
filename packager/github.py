import json

import requests


def get_release_urls_github(owner: str, repo: str) -> list[dict[str, str]]:
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    # print(f"Fetching release information from {url}...")
    response = requests.get(url, timeout=10)
    data = response.json()

    return [
        {
            "browser_download_url": asset["browser_download_url"],
            "name": asset["name"],
            "tag_name": release.get("tag_name", "")
        }
        for release in data
        for asset in release.get("assets", [])
    ]

def get_owner_repo(metadata) -> tuple[str, str]:

    with open(metadata, "r") as f:
        data = json.load(f)

        data = data.get("Repository", "")
        owner = data.get("owner", "")
        repo = data.get("name", "")
    

    return owner, repo


if __name__ == "__main__":
    owner = "sagarHackeD"
    repo = "Snap_To_Grid_KiCAD"
    urls = get_release_urls_github(owner, repo)
    for url in urls:
        print(url)

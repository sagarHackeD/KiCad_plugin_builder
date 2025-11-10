import requests



def get_release_urls(owner: str, repo: str) -> list[str]:
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    response = requests.get(url,timeout=10)
    assets = response.json()

    return [
        asset["browser_download_url"]
        for release in assets
        for asset in release.get("assets", [])
    ]


if __name__ == "__main__":
    owner = "sagarHackeD"
    repo = "Snap_To_Grid_KiCAD"
    urls = get_release_urls(owner, repo)
    for url in urls:
        print(url)
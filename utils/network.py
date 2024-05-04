import requests


def download_file(url: str, path: str):
    """Downloads a file, and places it in the specified path"""

    response = requests.get(url, stream=True)
    with open(path, "wb") as f:
        f.write(response.content)


def get_user_picture_url(valid: bool):
    return (
        "https://drive.google.com/uc?export=download&id=1JNkUupLGWY9wXyme_XvZtwHrQHcYhSp0"
        if valid
        else "https://drive.google.com/uc?export=download&id=16_qFfid6pacGgnIwyTxivMK5Nsv7BGS0"
    )

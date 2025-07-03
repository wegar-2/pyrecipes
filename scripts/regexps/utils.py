from pathlib import Path

import requests

__all__ = [
    "get_txt_from_url",
    "get_txt_from_url_into_path"
]


def get_txt_from_url(url: str, encoding: str = "utf-8") -> str:
    r = requests.get(url=url)
    return r.content.decode(encoding=encoding)


def get_txt_from_url_into_path(
        url: str,
        path: Path,
        encoding: str = "utf-8",
        linesep: str = r"\r\n"
) -> None:
    text: str = get_txt_from_url(url=url, encoding=encoding)
    lines: list[str] = [x for x in text.split(sep=linesep) if x != ""]
    with open(path, mode="wt") as file:
        for line in lines:
            file.write(f"{line}\n")

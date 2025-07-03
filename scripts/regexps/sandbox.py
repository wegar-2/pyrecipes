from pathlib import Path

from scripts.regexps.utils import get_txt_from_url_into_path


if __name__ == "__main__":
    url = "https://wolnelektury.pl/media/book/txt/faraon-tom-pierwszy.txt"
    path: Path = Path(__file__).parent.parent.parent / "data" / "faraon_prus.txt"
    get_txt_from_url_into_path(url=url,path=path)

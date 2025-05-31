from pathlib import Path


def list_dir_contents_non_recursive(p: Path):
    for i, x in enumerate(p.iterdir()):
        print(f"{i}: {x}, is file?: {x.is_file()}")


def list_dir_contents_recursive(p: Path):
    for i, x in enumerate(p.rglob(pattern="*")):
        print(f"{i}: {x}, is file?: {x.is_file()}")


def create_dir_if_does_not_exist(p: Path):
    try:
        p.mkdir(mode=0o777, parents=False, exist_ok=False)
    except FileExistsError:
        print(f"Directory {p} already exists! ")


if __name__ == "__main__":

    root_path: Path = Path(__file__).parent.parent

    # 1. list all contents of the project root - one level only
    list_dir_contents_non_recursive(p=root_path)

    # 2. list all contents of the project root - one level only
    list_dir_contents_recursive(p=root_path)

    # 3. create dir if does not exist
    create_dir_if_does_not_exist(root_path / "tempdir")


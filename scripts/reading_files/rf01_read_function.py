from scripts.reading_files.reader import read_file, FILEPATH


if __name__ == "__main__":
    for n in range(7):
        read_file(path=FILEPATH, mode="rt", n=n, rf="read")
    for n in range(7):
        read_file(path=FILEPATH, mode="rb", n=n, rf="read")
        
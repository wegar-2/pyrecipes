from scripts.reading_files.reader import read_file, FILEPATH

if __name__ == "__main__":
    for n in range(2, 6, 1):
        read_file(path=FILEPATH, mode="rt", n=n, rf="readlines")
    for n in range(2, 6, 1):
        read_file(path=FILEPATH, mode="rb", n=n, rf="readlines")

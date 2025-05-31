from scripts.reading_files.reader import read_file, FILEPATH

if __name__ == "__main__":
    for n in range(6):
        read_file(path=FILEPATH, mode="rt", n=n, rf="readline")
    for n in range(6):
        read_file(path=FILEPATH, mode="rb", n=n, rf="readline")

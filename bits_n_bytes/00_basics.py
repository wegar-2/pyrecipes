# References:
# (1) ASCII codes: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html

if __name__ == "__main__":

    str_: str = "Hello world! "
    print(f"Printing ASCII codes of the letters of string {str_}")
    for i, s in enumerate(str_):
        print(f"{i:02}: {s=}, {ord(s)=}")

    print("Printing ASCII/Unicode symbols")
    for i in range(256):
        print(f"{i:03}: {chr(i)}")

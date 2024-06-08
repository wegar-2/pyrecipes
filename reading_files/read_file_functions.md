## Reading files

This file contains brief description of how the functions:
* `read`
* `readline`
* `readlines`

work. In order to make this description more practical the following text file
is used:

```plaintext
# myfile.txt
1ä
3ü
```

> **Remark**: The letters that are used are German letters with 
> umlaut diacritic sign. These letters are used due to their byte representation.
> 
> The hexadecimal encodings of German letters with Umlaut (under UTF-8) are:\
> ä ----> c3a4 \
> ö ----> c3b6 \
> ü ----> c3bc \
> ß ----> c39f
> 
> These encodings are given here as they will be of importance later in 
> these considerations.

### General Read Function

In order to elucidate the differences between the various read functions, 
the following function is used:
```python
from pathlib import Path
from typing import Literal, TypeAlias, Final

Mode: TypeAlias = Literal["rt", "rb"]
ReadFunction: TypeAlias = Literal["read", "readline", "readlines"]
FILEPATH: Final[Path] = Path(__file__).parent / "myfile.txt"


def read_file(path: Path, mode: Mode, n: int, rf: ReadFunction):
    with open(path, mode) as f:
        if rf == "read":
            output = f.read(n)
        elif rf == "readline":
            output = f.readline(n)
        else:
            output = f.readlines(n)
    print(f"{mode=}, {n=}, {rf=}; {output=}")
```

This function allows you to open the read file either in byte or 
text read mode - the `Literal` parameter `mode`.

Furthermore, it allows the user to pass the general function argument `n`. 
Its specific role varies across the three functions.


### Function `read`
Run the code:
```python
for n in range(3, 13):
    read_file(path=FILEPATH, mode="rt", n=n, rf="read")
for n in range(3, 13):
    read_file(path=FILEPATH, mode="rb", n=n, rf="read")
```

In order to get the output:
```commandline
mode='rt', n=0, rf='read'; output=''
mode='rt', n=1, rf='read'; output='1'
mode='rt', n=2, rf='read'; output='1ä'
mode='rt', n=3, rf='read'; output='1ä\n'
mode='rt', n=4, rf='read'; output='1ä\n3'
mode='rt', n=5, rf='read'; output='1ä\n3ü'
mode='rt', n=6, rf='read'; output='1ä\n3ü\n'
mode='rb', n=0, rf='read'; output=b''
mode='rb', n=1, rf='read'; output=b'1'
mode='rb', n=2, rf='read'; output=b'1\xc3'
mode='rb', n=3, rf='read'; output=b'1\xc3\xa4'
mode='rb', n=4, rf='read'; output=b'1\xc3\xa4\n'
mode='rb', n=5, rf='read'; output=b'1\xc3\xa4\n3'
mode='rb', n=6, rf='read'; output=b'1\xc3\xa4\n3\xc3'
```
This clearly shows that:
* in text mode: function loads a specified number of TEXT SYMBOLS
* in byte mode: function loads a specified number of BYTES

One observation that one can formulate here is that you can load incomplete 
encoding of a symbol when loading in the byte mode.

### Function `readline`
Run:
```python
for n in range(7):
    read_file(path=FILEPATH, mode="rt", n=n, rf="readline")
for n in range(7):
    read_file(path=FILEPATH, mode="rb", n=n, rf="readline")
```
To get:
```commandline
mode='rt', n=0, rf='readline'; output=''
mode='rt', n=1, rf='readline'; output='1'
mode='rt', n=2, rf='readline'; output='1ä'
mode='rt', n=3, rf='readline'; output='1ä\n'
mode='rt', n=4, rf='readline'; output='1ä\n'
mode='rt', n=5, rf='readline'; output='1ä\n'
mode='rb', n=0, rf='readline'; output=b''
mode='rb', n=1, rf='readline'; output=b'1'
mode='rb', n=2, rf='readline'; output=b'1\xc3'
mode='rb', n=3, rf='readline'; output=b'1\xc3\xa4'
mode='rb', n=4, rf='readline'; output=b'1\xc3\xa4\n'
mode='rb', n=5, rf='readline'; output=b'1\xc3\xa4\n'
```

This function works analogously to the `read` except that it loads at most
one line of text. Hence, assuming text mode, even if you order it to read
more characters than there are in the line at hand, it will not go to the next 
line in order to get more of them.

### Function `readlines`

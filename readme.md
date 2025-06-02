# pyrecipes


----
## Table of Contents

Contents are stored in two subfolders: `scripts` and `notebooks`. 
Cf. list of the specific contents in subsections below.

### scripts 
Python scripts with snippets pertaining to various topics 
1. [`algorithms`](./scripts/algorithms):
   * [`sorting`](./scripts/algorithms/sorting) - implementations of sorting algorithms
2. [`base64enc`](./scripts/base64enc) - doing `base64` encoding (WiP!) 
3. [`bits_n_bytes`](./scripts/bits_n_bytes) - working with Pythons `bytes`, `bytearray`, encoding numbers and test as bytes, etc.
4. [`builtin_gttrs_sttrs`](./scripts/builtin_gttrs_sttrs) - explained difference between `__getattr__` and `__getattribute__`
5. [`decorators`](./scripts/decorators) - overview of key use-cases of decorators
6. [`fs`](./scripts/fs) - file system operations (using `pathlib.Path` to iterate over directory contents, both recursively and non-recursively, etc.)
7. [`function_self_inspection`](./scripts/function_self_inspection) - how to get function's name from within that function 
8. [`gcp_notes`](./scripts/gcp_notes) - investigation of select `Google Cloud Platform` aspects 
9. [`hackerrank`](./scripts/hackerrank) - notes on [Hackerrank](http://hackerrank.com/) problems
10. [`heapq_notes`](./scripts/heapq_notes) - notes on using Python's `heapq` class
11. [`iterators_n_generators`](./scripts/iterators_n_generators) - overview of iterators and generators in Python
12. [`itertools_notes`](./scripts/itertools_notes) - notes on using select Python `itertools` package functions
13. [`metacls`](./scripts/metacls) - notes on metaclasses in Python
14. [`mypy`](./scripts/mypy) - notes on Pytohn's static type checked [mypy](https://mypy.readthedocs.io/en/stable/)
    * [`overload` basics](./scripts/mypy/overload_basics.py)
    * [`overload` for separating implementation of different values of a `Literat` type](./scripts/mypy/overload_literal_type.py)
15. [`oop`](./scripts/oop) - OOP in Python: notes
16. [`operators_overloading`](./scripts/operators_overloading) - overloading of operators in Python
17. [`reading_files`](./scripts/reading_files) - explained difference between `read`, `readline` and `readlines` methods called on open file
18. [`singleton_with_mcs`](./scripts/singleton_with_mcs) - implementing singleton patter in Python using metaclasses
  

### notebooks 
1. [Tutorial on working with time zones in `datetime`, `dateutil` and `pandas`](./notebooks/tutorial-timezones-datetime-dateutil-pandas.ipynb)
2. [Overview of useful string columns methods in `pandas`](./notebooks/dataframe_string_col_operations.ipynb)
3. [f-string formatting of numbers, datetimes and strings](./notebooks/fstring_tutorial.ipynb)

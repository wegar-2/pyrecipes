import json
from pathlib import Path


if __name__ == "__main__":
    """
    s = json.dumps(dict) - saves string representation of dictionary dict 
    into string s
    
    json.dump(dict, file) - saves dictionary into json file 
    """

    d = {
        "m1": "asdf",
        "m2": 123,
        "m3": 901.123,
        "m4": [1, 3, 10, 5],
        "m5": {
            "ms1": 123,
            "ms2": "qwerty"
        }
    }
    s: str = json.dumps(d)
    print(json.dumps(d))

    path_: Path = Path(__file__).parent / "sample_json.json"

    with open(path_, mode="w") as f:
        json.dump(d, f, indent=4)

    with open(path_, mode="r") as f:
        d = json.load(f)
    print(d)

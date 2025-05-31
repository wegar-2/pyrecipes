from typing import TypedDict

Person = TypedDict("Person", {
    "name": str,
    "surname": str,
    "age": int
})


def print_person(d: Person):
    for k, v in d.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    person = {
        "name": "John",
        "surname": "Smith",
        "age": 40
    }

    print_person(d=person)

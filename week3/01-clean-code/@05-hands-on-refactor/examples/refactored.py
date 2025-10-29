# refactored.py

from typing import Callable, Iterable


def clean(values: Iterable[str]) -> list[str]:
    return [v.strip() for v in values if v]


def filter_values(values: Iterable[str], predicate: Callable[[str], bool]) -> list[str]:
    return [v for v in values if predicate(v)]


def to_csv(values: Iterable[str]) -> str:
    return ",".join(values)


def save(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main(data: Iterable[str], kind: str, outfile: str | None = None) -> None:
    cleaned = clean(data)

    predicates = {
        "number": str.isdigit,
        "word": str.isalpha,
        "none": lambda s: True,
    }
    predicate = predicates.get(kind, lambda s: True)

    filtered = filter_values(cleaned, predicate)
    result = to_csv(filtered)

    if outfile:
        save(outfile, result)
    else:
        print(result)

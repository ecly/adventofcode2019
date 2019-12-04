import regex as re


def is_valid(n):
    decreases = n == int("".join(sorted(str(n))))
    adjacent = bool(re.search(r"(\d)\1{1,}", str(n)))
    return decreases and adjacent


def is_valid2(n):
    matches = re.findall(r"((\d)\2++)", str(n))
    return is_valid(n) and any(len(match) == 2 for match, _digit in matches)


def main():
    numbers = range(134565, 585159)
    print(len(list(filter(is_valid, numbers))))
    print(len(list(filter(is_valid2, numbers))))


if __name__ == "__main__":
    main()

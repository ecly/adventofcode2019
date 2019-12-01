import sys

def rec_fuel(mass):
    fuel = mass // 3 - 2
    if fuel > 6:
        return fuel + rec_fuel(fuel)

    return fuel

def main():
    masses = list(map(int, sys.stdin))
    print(sum(map(lambda x: x // 3 - 2, masses)))
    print(sum(map(lambda x: rec_fuel(x), masses)))

if __name__ == "__main__":
    main()

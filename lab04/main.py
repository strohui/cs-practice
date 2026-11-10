import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)

    non_empty = 0
    for line in lines:
        if line.strip() != "":
            non_empty += 1
    skipped = non_empty - len(records)

    print(len(records))
    print(skipped)

    if len(records) > 0:
        best = warmest_city(records)
        print(f"{average_by_city(records)[best]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()

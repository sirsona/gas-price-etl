from load import load

from extract import extract
from transform import transform


def main():
    data = extract()
    state, cities = transform(data)
    load(state, cities)


if __name__ == "__main__":
    main()

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--greet", action="store_true", default=False)
args = parser.parse_args()


def generate_message(greet):
    if greet:
        start_message = "Hello"
    else:
        start_message = "Goodbye"
        return f"{start_message} World"


if __name__ == "__main__":
    print(generate_message(args.greet))

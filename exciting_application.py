from datetime import datetime


def parse_time():
    time_part = datetime.now().strftime("%H:%M")
        return time_part


if __name__ == "__main__":
    print(generate_message())

from datetime import datetime


def generate_message():
    greeting_part = "Hello World"
    time_part = datetime.now().strftime("%H:%M")
        return f"{greeting_part}, it is {time_part}"


if __name__ == "__main__":
    print(generate_message())

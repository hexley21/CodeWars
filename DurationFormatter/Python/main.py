from DurationFormatter import Time


def main():
    while True:
        try:
            seconds = int(input("Enter amount of seconds: "))
            if (seconds < 0):
                raise ValueError
            time = Time(seconds)
            print(time.format_time())
            break
        except ValueError:
            print("Please enter positive integer\n")
        except Exception as e:
            print(str(e) + "\n")


if __name__ == "__main__":
    main()

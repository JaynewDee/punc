from datetime import datetime as dt
import time as t
import webbrowser
import sys


YEAR = 2023
MONTH = 3
HOUR = 0
MINUTE = 29


days = ['mar_13', 'mar_14', 'mar_16', 'mar_20', 'mar_21', 'mar_31']
day_vals = [13, 14, 16, 20, 21, 31]
urls = ['https://zoom.us/j/91027252569', 'https://zoom.us/j/96947278951',
        'https://zoom.us/j/96442631204', 'https://zoom.us/j/96442631204', 'https://zoom.us/j/96442631204', 'https://www.google.com/']

assert(len(days) == len(day_vals) == len(urls))


def get_sleep_duration():
    return int(input("How often do you wish to poll the time?\n\n(Sleep duration in seconds) ::: "))


def validate_input_args():
    args = sys.argv
    if len(args) > 2:
        print("USAGE: <executable>")
        return
    return args


def main():
    cl_input = validate_input_args()

    sleep_duration = get_sleep_duration()

    print("|script running|")
    running = True

    while running:
        try:
            date = dt.now().date()
            time = dt.now().time()

            print(f"Polled for events @ {time}")

            sessions = make_sessions()

            for details in sessions.values():
                url, thyme = details
                url, thyme = details[url], details[thyme]

                if date == thyme.date() and time >= thyme.time():
                    print(details)
                    # del sessions[details]
                    webbrowser.open(url)

            t.sleep(sleep_duration)

        except (EOFError, RuntimeError, SystemError, SystemExit, KeyboardInterrupt, StopIteration):
            print("The program was forced to terminate.")
            running = False
            sys.exit()


def make_sessions():
    class_sessions = {}

    for idx in range(len(urls)):
        day_str = days[idx]
        day_num = day_vals[idx]
        url = urls[idx]
        class_sessions[day_str] = {
            'url': url,
            'time': dt(YEAR, MONTH, day_num, HOUR, MINUTE)
        }

    return class_sessions


if __name__ == "__main__":
    main()

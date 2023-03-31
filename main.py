from datetime import datetime as dt
import time as t
import webbrowser
import sys

# Rewrite to remind user of anything!

YEAR = 2023
MONTH = 3
HOUR = 18
MINUTE = 29


days = ['mar_13', 'mar_14', 'mar_16', 'mar_20', 'mar_21']
day_vals = [13, 14, 16, 20, 21]
urls = ['https://zoom.us/j/91027252569', 'https://zoom.us/j/96947278951',
        'https://zoom.us/j/96442631204', 'https://zoom.us/j/96442631204', 'https://zoom.us/j/96442631204']

assert(len(days) == len(day_vals) == len(urls))


def main():
    timer = int(input(
        "How often do you wish to poll the time?\n\n(Sleep duration in seconds) ::: "))

    print("|script running|")
    running = True

    while running:
        try:
            date = dt.now().date()
            time = dt.now().time()

            for details in make_sessions().values():
                url, thyme = details
                url = details[url]
                thyme = details[thyme]

                if date == thyme.date() and time == thyme.time():
                    webbrowser.open(url)

            t.sleep(timer)
        except (EOFError, RuntimeError, SystemError, SystemExit, KeyboardInterrupt):
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

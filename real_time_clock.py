import time

RTC_PATH = "/dev/rtc0"


def read_rtc_time(rtc_path = RTC_PATH):
    with open("/sys/class/rtc/rtc0/time", "r", encoding="utf-8") as time_from_file:
        time_to_string = time_from_file.read().strip()
    return time_to_string

try:
    while True:
        print(read_rtc_time())
        time.sleep(1)
except KeyboardInterrupt:
    print("quitting.")

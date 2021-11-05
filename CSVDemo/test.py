from pynput.keyboard import Listener
import time
import threading


def press(key):
    print(str(key))
    global control
    if str(key) == "'a'":
        control = True
    else:
        control = False


def start_listing_key():
    with Listener(on_press=press) as listener:
        listener.join()


def test_for():
    t = threading.Thread(target=start_listing_key)
    t.start()
    file = open("person.csv", "r")
    for i in file:
        time.sleep(1)
        print(f"{i}", end="")
        while control:
            print("程序暂停中...")
            time.sleep(2)


if __name__ == '__main__':
    control = False
    test_for()

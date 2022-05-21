import time

from ppadb.client import Client as AdbClient


def connect():
    client = AdbClient(host="127.0.0.1", port=5037)  # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client


if __name__ == '__main__':
    device, client = connect()

    # open up camera app
    device.shell('input keyevent 27')

    # wait 5 seconds
    time.sleep(5)

    # take a photo with volume up
    device.shell('input keyevent 24')
    print('Taken a photo!')

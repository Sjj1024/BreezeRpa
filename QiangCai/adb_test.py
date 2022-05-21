from ppadb.client import Client as AdbClient

if __name__ == '__main__':
    client = AdbClient(host="127.0.0.1", port=5037)  # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

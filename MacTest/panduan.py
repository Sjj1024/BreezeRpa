import os
import platform


def play_voice(content):
    """
    播放声音提醒
    """
    system = platform.system()
    if system == "Windows":
        from playsound import playsound
        video_path = os.path.join(os.getcwd(), "11.mp3")
        playsound(video_path)
    else:
        os.system(f'say "{content}"')
    res = os.popen("pwd").read()
    print(res)


def is_mac():
    system = platform.system()
    if system == "Windows":
        print("当前系统是Windows")
        return False
    else:
        print("当前系统是Mac")
        return True


def get_device_list():
    print("get_device_list")
    root_path = os.getcwd()
    if is_mac():
        cmd = f"{root_path}/sources/mac_tools/adb devices"
    else:
        cmd = f"{root_path}/sources/win_tools/adb devices"
    res = os.popen(cmd).read()
    list_phone = [i for i in res.split("\n") if i]
    if len(list_phone) > 1:
        phone_num = [i.split("\t")[0] for i in list_phone[1:] if i]
        print(f"得到的设备列表是:{phone_num}")
    else:
        print(f"设备连接不正常,得到的adb devices结果是:\n{res}")
        raise Exception("设备连接不正常")


def play_mp3():
    from playsound import playsound
    # video_path = f"{os.getcwd()}/sources/success.mp3"
    # video_path = "/Users/jiang/PyProjects/BreezeRpa/MacTest/sources/videos/start.mp3"
    # video_path = "/Users/jiang/PyProjects/BreezeRpa/MacTest/sources/videos/error.mp3"
    video_path = f"{os.getcwd()}/sources/videos/success.mp3"
    print(video_path)
    playsound(video_path)


def run():
    get_device_list()


if __name__ == '__main__':
    play_mp3()

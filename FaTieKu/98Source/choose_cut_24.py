import os
# 随机抽选文件中24张照片，其余的全部删除
from PIL import Image


def get_pictures():
    root_dir = os.path.join(os.getcwd(), target_dir)
    dirs_lists = os.listdir(root_dir)
    dirs_pictures = [os.path.join(root_dir, i) for i in dirs_lists if os.path.isdir(os.path.join(root_dir, i))]
    print(f"扫描到{len(dirs_pictures)}个文件夹")
    return dirs_pictures


def del_others(dir):
    print("仅保留前24张")
    pictures = os.listdir(dir)
    need_pic = [os.path.join(dir, j) for j in pictures]
    # if len(pic_dir) > 23:
    #     others_del = pic_dir[23:]
    #     need_pic = pic_dir[:23]
    #     for one in others_del:
    #         os.remove(one)
    # else:
    #     need_pic = pic_dir
    for pic in need_pic:
        try:
            cut_pic(pic)
        except Exception as e:
            print(e)
            continue


def cut_pic(pic):
    img = Image.open(pic)
    size = img.size
    width = size[0]
    height = size[1] - 88
    cropped = img.crop((0, 0, width, height))  # (left, upper, right, lower)
    res = cropped.tobytes()
    cropped.save(pic)
    print(f"图片{pic}处理完成")


def run():
    print("开始运行")
    # 遍历文件夹下所有文件夹
    dirs_pictures = get_pictures()
    # 获取文件夹中图片个数并随机抽选24张
    for dir in dirs_pictures:
        del_others(dir)


if __name__ == '__main__':
    # 选中文件夹中24张图片，并剪切掉妹子图的logo，其余的删除
    target_dir = "自拍套图"
    run()

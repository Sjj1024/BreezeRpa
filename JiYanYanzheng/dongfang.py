# def open(self):
#    """
#     登录模块
#     """
#     # 定位密码登录
#     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div[1]/div[2]').click()
#     # 输入账号
#     username = '123456'
#     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys(username)
#     time.sleep(1)
#     # 输入密码
#     password = '123456789'
#     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div[2]/div[1]/form/div[2]/div/div/input').send_keys(password)
#     time.sleep(1)
#     # 登录
#     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div[2]/div[3]/button').click()
#
# def get_images(self):
#    """
#    获取验证码图片
#    :return: 图片的location信息
#    """
#    # 带缺口图片，使用js定位并读取图片的data信息 data:image/png;base64，直接调用识别缺口
#    fullgb = self.driver.execute_script('return document.getElementsByClassName("geetest_canvas_bg geetest_absolute")[0].toDataURL("image/png")')
#    # 完整图片，使用js定位并读取图片的data信息 data:image/png;base64，直接调用识别缺口
#    bg = self.driver.execute_script('return document.getElementsByClassName("geetest_canvas_fullbg geetest_fade geetest_absolute")[0].toDataURL("image/png")')
#    return bg, fullgb
#
# def get_decode_image(self, location_list):
#    """
#    解码图片的base64数据
#    """
#    # 提取图片base64数据
#    _, img = location_list.split(",")
#    # 数据转换为Bytes字节
#    img = base64.decodebytes(img.encode())
#    # 读取图片
#    new_im: PngImagePlugin.PngImageFile = image.open(BytesIO(img))
#    # new_im.convert("RGB")
#    # new_im.save(filename)
#    return new_im
#
# def compute_gap(self, img1, img2):
#    """
#    计算缺口偏移 这种方式成功率很高
#    """
#    # 将图片修改为RGB模式
#    img1 = img1.convert("RGB")
#    img2 = img2.convert("RGB")
#    # 计算差值
#    diff = ImageChops.difference(img1, img2)
#    # 灰度图
#    diff = diff.convert("L")
#    # 二值化
#    diff = diff.point(self.table, '1')
#    left = 43
#    for w in range(left, diff.size[0]):
#        lis = []
#        for h in range(diff.size[1]):
#            if diff.load()[w, h] == 1:
#                lis.append(w)
#            if len(lis) > 5:
#                return w
#
# def get_tracks(self, distance, seconds, ease_func):
#     """
#     :param distance: 缺口位置
#     :param seconds:  时间
#     :param ease_func: 生成函数
#     :return: 轨迹数组
#     """
#     tracks = [0]
#     offsets = [0]
#     for t in np.arange(0.0, seconds, 0.1):
#         ease = ease_func
#         offset = round(ease(t / seconds) * distance)
#         tracks.append(offset - offsets[-1])
#         offsets.append(offset)
#     return tracks
#
#
# def move_to_gap(self, track):
#     """滑动滑块"""
#     print('第一步,点击滑动按钮')
#     slider = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
#     ActionChains(self.driver).click_and_hold(slider).perform()
#     time.sleep(1)
#     print('第二步,拖动元素')
#     for track in track:
#         ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()  # 鼠标移动到距离当前位置（x,y）
#         time.sleep(0.0001)
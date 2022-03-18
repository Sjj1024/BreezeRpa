import pygame
import random


def main():
  # 初始化pygame
  pygame.init()

  # 默认不全屏
  fullscreen = False
  # 窗口未全屏宽和高
  WIDTH, HEIGHT = 2100, 1200

  init_width, init_height = WIDTH, HEIGHT

  # 字块大小，宽，高
  suface_height = 18
  # 字体大小
  font_size = 20

  # 创建一个窗口
  screen = pygame.display.set_mode((init_width, init_height))

  # 字体
  font = pygame.font.Font('/Library/Fonts/Arial Unicode.ttf', font_size)

  # 创建一个图像对象
  bg_suface = pygame.Surface((init_width, init_height), flags=pygame.SRCALPHA)
  pygame.Surface.convert(bg_suface)
  bg_suface.fill(pygame.Color(0, 0, 0, 28))

  # 用纯色填充背景
  screen.fill((0, 0, 0))

  # 显示的字符
  letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
            'c',
            'v', 'b', 'n', 'm']
  texts = [
    font.render(str(letter[i]), True, (0, 255, 0)) for i in range(26)
  ]

  # 也可以替换成0 1 显示
  # texts = [
  #     font.render('0',True,(0,255,0)),font.render('1',True,(0,255,0))
  # ]

  # 生成的列数
  column = int(init_width / suface_height)
  drops = [0 for i in range(column)]

  while True:
    # 按键检测
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        # 接受到退出事件后退出
        exit()
      elif event.type == pygame.KEYDOWN:
        # 按F11切换全屏，或窗口
        if event.key == pygame.K_F11:
          print("检测到按键F11")
          fullscreen = not fullscreen
          if fullscreen:
            # 全屏效果，参数重设
            size = init_width, init_height = pygame.display.list_modes()[0]
            screen = pygame.display.set_mode(size, pygame.FULLSCREEN | pygame.HWSURFACE)

          else:
            init_width, init_height = WIDTH, HEIGHT
            screen = pygame.display.set_mode((WIDTH, HEIGHT))

          # 图像对象重新创建
          bg_suface = pygame.Surface((init_width, init_height), flags=pygame.SRCALPHA)
          pygame.Surface.convert(bg_suface)
          bg_suface.fill(pygame.Color(0, 0, 0, 28))
          column = int(init_width / suface_height)
          drops = [0 for i in range(column)]
        elif event.key == pygame.K_ESCAPE:
          # 按ESC退出
          exit()
    # 延时
    pygame.time.delay(30)

    # 图像对象放到窗口的原点坐标上
    screen.blit(bg_suface, (0, 0))

    for i in range(len(drops)):
      # 随机字符
      text = random.choice(texts)

      # 把字符画到该列的下雨的位置
      screen.blit(text, (i * suface_height, drops[i] * suface_height))

      # 更新下雨的坐标
      drops[i] += 1

      # 超过界面高度或随机数，下雨位置置0
      if drops[i] * suface_height > init_height or random.random() > 0.95:
        drops[i] = 0

    # 更新画面
    pygame.display.flip()


if __name__ == '__main__':
  main()

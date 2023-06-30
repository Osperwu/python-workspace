import pygame
from pygame.locals import *

# 初始化Pygame
pygame.init()

# 設定遊戲視窗大小
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("反彈球遊戲")

# 設定球的初始位置和速度
ball_x = 100
ball_y = 100
ball_speed_x = 0.2
ball_speed_y = 0.2

# 遊戲主迴圈
running = True
while running:
    # 事件處理
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 移動球的位置
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 檢查球是否超出邊界，若超出則反彈
    # if ball_x < 0 or ball_x > screen_width:
    #     ball_speed_x *= -1
    if ball_y < 0 or ball_y > screen_height:
        ball_speed_y *= -1

    # 畫面更新
    screen.fill((0, 0, 0))  # 清除畫面
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)  # 繪製球
    pygame.display.update()

# 結束遊戲
pygame.quit()

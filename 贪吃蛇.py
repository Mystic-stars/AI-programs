# 导入pygame模块
import pygame
# 导入random模块
import random

# 初始化pygame
pygame.init()

# 设置屏幕大小和标题
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('贪吃蛇')

# 设置颜色常量
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 设置字体
font = pygame.font.SysFont('Microsoft Yahei', 32)

# 设置蛇的初始位置和方向
snake_x = 400
snake_y = 300
snake_dir = 'right'
snake_length = 1
snake_body = [(snake_x, snake_y)]

# 设置食物的初始位置
food_x = random.randint(0, 79) * 10
food_y = random.randint(0, 59) * 10

# 设置游戏状态和分数
game_over = False
score = 0

# 设置是否重新开始游戏的变量
restart = False

# 设置时钟对象，控制帧率
clock = pygame.time.Clock()

# 游戏主循环
while not game_over:
    # 如果restart为True，就重置游戏状态和变量，并设置restart为False
    if restart:
        # 重置蛇的初始位置和方向
        snake_x = 400
        snake_y = 300
        snake_dir = 'right'
        snake_length = 1
        snake_body = [(snake_x, snake_y)]

        # 重置食物的初始位置
        food_x = random.randint(0, 79) * 10
        food_y = random.randint(0, 59) * 10

        # 重置游戏状态和分数
        game_over = False
        score = 0

        # 设置restart为False
        restart = False

    # 处理事件
    for event in pygame.event.get():
        # 如果点击了关闭按钮，退出游戏
        if event.type == pygame.QUIT:
            game_over = True
        # 如果按下了键盘，改变蛇的方向
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != 'down':
                snake_dir = 'up'
            if event.key == pygame.K_DOWN and snake_dir != 'up':
                snake_dir = 'down'
            if event.key == pygame.K_LEFT and snake_dir != 'right':
                snake_dir = 'left'
            if event.key == pygame.K_RIGHT and snake_dir != 'left':
                snake_dir = 'right'

    # 根据蛇的方向，更新蛇的头部位置
    if snake_dir == 'up':
        snake_y -= 10
    if snake_dir == 'down':
        snake_y += 10
    if snake_dir == 'left':
        snake_x -= 10
    if snake_dir == 'right':
        snake_x += 10

    # 检查蛇是否超出了屏幕边界，如果是，游戏结束
    if snake_x < 0 or snake_x > 790 or snake_y < 0 or snake_y > 590:
        game_over = True

    # 检查蛇是否吃到了食物，如果是，增加分数和长度，并随机生成新的食物位置
    if snake_x == food_x and snake_y == food_y:
        score += 1
        snake_length += 1
        food_x = random.randint(0, 79) * 10
        food_y = random.randint(0, 59) * 10

    # 将蛇的头部位置添加到蛇的身体列表中
    snake_body.append((snake_x, snake_y))

    # 如果蛇的身体列表的长度超过了蛇的长度，删除最旧的一个元素（即蛇的尾部）
    if len(snake_body) > snake_length:
        snake_body.pop(0)

    # 检查蛇是否咬到了自己的身体，如果是，游戏结束
    for x, y in snake_body[:-1]:
        if x == snake_x and y == snake_y:
            game_over = True

    # 填充屏幕背景色为黑色
    screen.fill(BLACK)

    # 绘制食物为红色的矩形
    pygame.draw.rect(screen, RED, (food_x, food_y, 10, 10))

    # 绘制蛇的身体为绿色的矩形
    for x, y in snake_body:
        pygame.draw.rect(screen, GREEN, (x, y, 10, 10))

    # 绘制分数文本
    score_text = font.render('得分: ' + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))


    # 更新屏幕显示
    pygame.display.flip()

    # 设置帧率为10
    clock.tick(10)

# 退出pygame
pygame.quit()

import sys
import pygame
import time
import random
import math
pygame.init()

class MySurface:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Snake:
    cell = []
    __step = 20
    __direction = 1
    cracked = 0

    def __init__(self, color, step):
        for i in range(5):
            self.cell.append(pygame.Rect(
                140 - i * 20, 0, self.__step, self.__step))
        self.color = color
        self.__step = step

    def move(self):
        count = len(self.cell) - 1
        while (count > 0):
            self.cell[count].x = self.cell[count - 1].x
            self.cell[count].y = self.cell[count - 1].y
            count -= 1
        # 改头的位置
        if (self.__direction == 0):
            self.cell[0].y -= self.__step
        elif (self.__direction == 1):
            self.cell[0].x += self.__step
        elif (self.__direction == 2):
            self.cell[0].y += self.__step
        else:
            self.cell[0].x -= self.__step
        # 判断是否撞到了自己
        count = len(self.cell) - 1
        head = self.cell[0]
        while (count > 0):
            if (self.cell[count].x == head.x and self.cell[count].y == head.y):
                self.cracked = 1
                break
            count -= 1

    def getDirection(self):
        return self.__direction

    def setUpDirection(self):
        if (self.__direction == 2):
            return
        self.__direction = 0

    def setRightDirection(self):
        if (self.__direction == 3):
            return
        self.__direction = 1

    def setDownDirection(self):
        if (self.__direction == 0):
            return
        self.__direction = 2

    def setLeftDirection(self):
        if (self.__direction == 1):
            return
        self.__direction = 3

    def grow(self, food):
        # 吃到食物后，在头部插入一个单元
        self.cell.insert(0, food)

class Controller:
    def __init__(self, snake, gameSurface, infoSurface):
        self.__step = 20
        self.snake = snake
        self.food = pygame.Rect(random.randrange(
            0, 30)*20, random.randrange(0, 30)*20, self.__step, self.__step)
        self.gameSurface = gameSurface
        self.infoSurface = infoSurface
        self.gameOver = False

    def bEatTheFood(self):
        nextX = 0
        nextY = 0
        snake = self.snake
        head = snake.cell[0]
        if (snake.getDirection() == 0):
            nextX = head.x
            nextY = head.y - self.__step
        elif (snake.getDirection() == 1):
            nextX = head.x + self.__step
            nextY = head.y
        elif (snake.getDirection() == 2):
            nextX = head.x
            nextY = head.y + self.__step
        else:
            nextX = head.x - self.__step
            nextY = head.y
        if (self.food.x == nextX and self.food.y == nextY):
            # print('true')
            return True
        else:
            # print('false')
            return False

    def bHitTheWall(self):
        head = self.snake.cell[0]
        if (head.x < 0 or head.x + self.__step > self.gameSurface.get_width() or head.y < 0 or head.y + self.__step > self.gameSurface.get_height()):
            return True
        return False

    def IsGameOver(self):
        if (self.bHitTheWall()):
            self.gameOver = True
            print('hit the wall, game over!')
            return True
        elif (self.snake.cracked):
            self.gameOver = True
            print('hit yourself, game over!')
            return True
        return False

    def clear(self):
        self.gameSurface.fill((0, 0, 0))
        self.infoSurface.fill((0, 0, 0))

    def redraw(self):
        for rect in self.snake.cell:
            pygame.draw.rect(self.gameSurface, snakeColor, rect)
        pygame.draw.rect(self.gameSurface, foodColor, self.food)
        gameTime = math.ceil(time.time() - startTime)
        myFont = pygame.font.SysFont('arial', 16)
        self.infoSurface.blit(myFont.render(
            'snake length:' + str(len(snake.cell)), True, (255, 255, 255)), (0, 0))
        self.infoSurface.blit(myFont.render(
            'game time:' + str(gameTime) + 's', True, (255, 255, 255)), (0, 16))
        pygame.display.update()

    def setUpDirection(self):
        self.snake.setUpDirection()

    def setDownDirection(self):
        self.snake.setDownDirection()

    def setRightDirection(self):
        self.snake.setRightDirection()

    def setLeftDirection(self):
        self.snake.setLeftDirection()

    def snakeMove(self):
        self.snake.move()

    def snakeGrow(self):
        self.snake.grow(self.food)

    def resetFood(self):
        # 不能出现在蛇的位置
        # 最多就900个，暂时用最原始的方法
        flag = True
        while flag:
            rand = [random.randrange(0, gameSurface.get_width()/self.__step)*self.__step, random.randrange(0, gameSurface.get_width()/self.__step)*self.__step]
            repeated = False
            for rect in self.snake.cell:
                if (rect.x == rand[0] and rect.y == rand[1]):
                    repeated = True
                    break
            if (repeated):
                continue
            flag = False
        self.food = pygame.Rect(rand[0], rand[1], self.__step, self.__step)

def gameInit():
    global containerSurface
    global gameSurface
    global infoSurface
    global snakeColor
    global foodColor
    # 设置一些参数
    # 窗口尺寸
    size = width, height = 815, 610
    containerSurface = pygame.display.set_mode(size)
    # 窗口标题
    pygame.display.set_caption('Snake')
    # 边框
    frameThickness = 5
    frameColor = (0, 0, 255)
    containerSurface.fill(frameColor)
    # 游戏区域尺寸
    myGameSurface = MySurface(frameThickness, frameThickness,
                            600, height - 2 * frameThickness)
    gameSurface = containerSurface.subsurface(
        myGameSurface.x, myGameSurface.y, myGameSurface.w, myGameSurface.h)
    # 游戏信息尺寸
    myInfoSurface = MySurface(2 * frameThickness + myGameSurface.w, frameThickness,
                            width - 3 * frameThickness - myGameSurface.w, height - 2 * frameThickness)
    infoSurface = containerSurface.subsurface(
        myInfoSurface.x, myInfoSurface.y, myInfoSurface.w, myInfoSurface.h)
    # 蛇的颜色
    snakeColor = (255, 255, 255)
    # 食物的颜色
    foodColor = (255, 0, 0)

# 全局变量
gameSurface = None
infoSurface = None
containerSurface = None
snakeColor = None
foodColor = None

# 主函数

gameInit()
# 记录游戏开始时间
startTime = time.time()
snake = Snake(snakeColor, 20)
controller = Controller(snake, gameSurface, infoSurface)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 判断是否按下了方向键
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP):
                controller.setUpDirection()
            elif (event.key == pygame.K_RIGHT):
                controller.setRightDirection()
            elif (event.key == pygame.K_DOWN):
                controller.setDownDirection()
            elif (event.key == pygame.K_LEFT):
                controller.setLeftDirection()
    # 清空界面
    controller.clear()
    # 蛇的移动
    controller.snakeMove()
    if (controller.IsGameOver()):
        exit()
    if (controller.bEatTheFood()):
        controller.snakeGrow()
        controller.resetFood()
    # 重绘蛇和游戏信息
    controller.redraw()
    time.sleep(0.2)

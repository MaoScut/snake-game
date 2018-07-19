import sys, pygame, time, random
pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

white = (255, 255, 255)
# rect的参数，矩形左上角的坐标，宽度，高度

class Snake:
    cell = []
    __step = 20
    __direction = 1
    cracked = 0
    targetRect = {}
    def __init__(self):
        for i in range(5):
            self.cell.append(pygame.draw.rect(screen, white, [140 - i * 20, 0, self.__step, self.__step]))
        self.targetRect = pygame.Rect(random.randrange(0, 40) * 20, random.randrange(0, 30) * 20, self.__step, self.__step)
    def moveLeft(self):
        # 先逐个移动
        count = len(self.cell) - 1
        while (count > 0):
            self.cell[count].x = self.cell[count - 1].x
            self.cell[count].y = self.cell[count - 1].y
            count -= 1
        # 改头的位置
        self.cell[0].x -= self.__step

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

    def setUpDirection(self):
        if (self.__direction == 2): return
        self.__direction = 0

    def setRightDirection(self):
        if (self.__direction == 3): return
        self.__direction = 1   

    def setDownDirection(self):
        if (self.__direction == 0): return
        self.__direction = 2

    def setLeftDirection(self):
        if (self.__direction == 1): return
        self.__direction = 3  
    def setTarget(self):
        self.targetRect = pygame.Rect(random.randrange(0, 40) * 20, random.randrange(0, 30) * 20, self.__step, self.__step)
    def bEatTheFood(self):
        nextX = 0
        nextY = 0       
        head = self.cell[0]
        if (self.__direction == 0):
            nextX = head.x
            nextY = head.y - self.__step
        elif (self.__direction == 1):
            nextX = head.x + self.__step
            nextY = head.y
        elif (self.__direction == 2):
            nextX = head.x
            nextY = head.y + self.__step
        else:
            nextX = head.x - self.__step
            nextY = head.y
        if (self.targetRect.x == nextX and self.targetRect.y == nextY):
            print('true')
            return True
        else:
            print('false')
            return False
    def grow(self):
        # 吃到食物后，在头部插入一个单元
        self.cell.insert(0, self.targetRect)
snake = Snake()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP): 
                snake.setUpDirection()
            elif (event.key == pygame.K_RIGHT): 
                snake.setRightDirection()
            elif (event.key == pygame.K_DOWN): 
                snake.setDownDirection()
            elif (event.key == pygame.K_LEFT):
                snake.setLeftDirection()               
    screen.fill((0,0,0))
    snake.move()
    if (snake.bEatTheFood()):
        snake.grow()
        snake.setTarget()
    for rect in snake.cell:
        pygame.draw.rect(screen, white, rect)
    pygame.draw.rect(screen, white, snake.targetRect)
    pygame.display.update()
    if (snake.cracked): 
        print('cracked!')
        exit()
    time.sleep(0.5)
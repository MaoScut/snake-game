import sys, pygame, time
pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

white = (255, 255, 255)
# rect的参数，矩形左上角的坐标，宽度，高度

class Snake:
    cell = []
    step = 20
    direction = 1
    def __init__(self):
        for i in range(5):
            self.cell.append(pygame.draw.rect(screen, white, [150 - i * 20, 10, 20, 20]))
    def moveLeft(self):
        # 先逐个移动
        count = len(self.cell) - 1
        while (count > 0):
            self.cell[count].x = self.cell[count - 1].x
            self.cell[count].y = self.cell[count - 1].y
            count -= 1
        # 改头的位置
        self.cell[0].x -= self.step
    def move(self):
        # 先固定向右边移动
        count = len(self.cell) - 1
        head = self.cell[0]
        while (count > 0):
            self.cell[count].x = self.cell[count - 1].x
            self.cell[count].y = self.cell[count - 1].y
            count -= 1
        # 改头的位置
        if (self.direction == 0):
            self.cell[0].y -= self.step
        elif (self.direction == 1): 
            self.cell[0].x += self.step
        elif (self.direction == 2): 
            self.cell[0].y += self.step
        else:
            self.cell[0].x -= self.step
        
    # def grow(self):
        # 吃到食物后，在头部插入一个单元
        # cell.append()
snake = Snake()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP): 
                snake.direction = 0
            elif (event.key == pygame.K_RIGHT): 
                snake.direction = 1
            elif (event.key == pygame.K_DOWN): 
                snake.direction = 2
            elif (event.key == pygame.K_LEFT):
                snake.direction = 3                 
    screen.fill((0,0,0))
    snake.move()
    for rect in snake.cell:
        pygame.draw.rect(screen, white, rect)
    pygame.display.update()
    time.sleep(0.5)
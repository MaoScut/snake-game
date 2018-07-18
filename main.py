import sys, pygame
pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

white = (255, 255, 255)
# rect的参数，矩形左上角的坐标，宽度，高度
cell = pygame.draw.rect(screen, white, [150, 10, 50, 20])

class Cell:
    def __init__(self, drawer, screen, positionInfo):
        self.positionInfo = positionInfo
        self.drawer = drawer
        self.screen = screen
        self.rect = drawer(screen, white, positionInfo)
    def updatePosition(self):
        self.drawer(self.screen, white, self.positionInfo)
    def moveLeft(self):
        self.rect.move_ip([10,0])
        self.updatePosition()
    # def show(self):
    #     self.updatePosition()
# cell = Cell(pygame.draw.rect, screen, [150, 10, 50, 20])
# pygame.display.update()
cell2 = cell
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT): 
                screen.fill((0,0,0))
                cell.move_ip(-10,0)
                pygame.draw.rect(screen, white, cell)
                print('left')
    pygame.display.update()
import os
import pygame
import random
import sys
import cfg
from pathlib import Path

WINDOWWIDTH = 640
WINDOWHEIGHT = 640
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 40

'''滑雪者类'''
class SkierSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 滑雪者的朝向(-2到2)
        self.direction = 0
        rootdir = Path(__file__).parent
        self.images = [rootdir/'resources/images/skier_forward.png',
                       rootdir/'resources/images/skier_right1.png',
                       rootdir/'resources/images/skier_right2.png',
                       rootdir/'resources/images/skier_left2.png',
                       rootdir/'resources/images/skier_left1.png']
        # self.person = pygame.image.load(self.images[self.direction])
        self.image = self.images[self.direction]
        self.person = pygame.image.load(self.image)
        self.rect = self.person.get_rect()
        self.rect.center = [320, 100]
        self.speed = [self.direction, 6 - abs(self.direction) * 2]
    '''改变滑雪者的朝向. 负数为向左,正数为向右,0为向前'''
    def turn(self, num):
        self.direction += num
        self.direction = max(-2, self.direction)
        self.direction = min(2, self.direction)
        center = self.rect.center
        self.image = self.images[self.direction]
        self.person = pygame.image.load(self.image)
        self.rect = self.person.get_rect()
        self.rect.center = center
        self.speed = [self.direction, 6-abs(self.direction)*2]
        return self.speed
    '''移动滑雪者'''
    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centerx = max(20, self.rect.centerx)
        self.rect.centerx = min(620, self.rect.centerx)
    '''设置为摔倒状态'''
    def setFall(self):
        # self.image = self.image_fall
        pass
    '''设置为站立状态'''
    def setForward(self):
        self.direction = 0
        self.image = self.images[self.direction]


'''障碍物类'''
class ObstacleSprite(pygame.sprite.Sprite):
    def __init__(self, image, location, attribute):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        self.attribute = attribute
        self.passed = False
    '''移动'''
    def move(self, num):
        self.rect.centery = self.location[1] - num


'''main'''
def main():
    # Set up pygame.
    pygame.init()

    # Set up the window.
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Ski Game')
    # pygame.mouse.set_visible(False)

    # Set up the fonts.
    font = pygame.font.SysFont(None, 48)

    # 根目录
    rootdir = os.path.split(os.path.abspath(__file__))[0]

    # 游戏图片路径
    IMAGE_PATHS_DICT = {
        'skier': [
            os.path.join(rootdir, 'resources/images/skier_forward.png'),
            os.path.join(rootdir, 'resources/images/skier_right1.png'),
            os.path.join(rootdir, 'resources/images/skier_right2.png'),
            os.path.join(rootdir, 'resources/images/skier_left2.png'),
            os.path.join(rootdir, 'resources/images/skier_left1.png'),
            os.path.join(rootdir, 'resources/images/skier_fall.png')
        ],
        'tree': os.path.join(rootdir, 'resources/images/tree.png'),
        'flag': os.path.join(rootdir, 'resources/images/flag.png'),
    }

    # 背景音乐路径
    BGM_PATH = os.path.join(rootdir, 'resources/audios/bgm.mp3')

    # # Set up sounds.
    # pygame.mixer.init()
    # pygame.mixer.music.load('resources/audios/bgm.mp3')    

    # Set up the colors.
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)

    # Draw the white background onto the surface.
    screen.fill(BACKGROUNDCOLOR)

    # Show the "Start" screen.
    drawText('Ski Game', font, screen, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to start.', font, screen, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
    waitForPlayerToPressKey()

    # 实例化游戏精灵
    # --滑雪者
    skier = SkierSprite()

    # 游戏clock
    clock = pygame.time.Clock()
    # 记录滑雪的距离
    distance = 0
    # 记录当前的分数
    score = 0
    # 记录当前的速度
    speed = [0, 6]
    # Run the game loop.
    while True:
        # Check for events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    speed = skier.turn(-1)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    speed = skier.turn(1)
        # --更新当前游戏帧的数据
        skier.move()
        distance += speed[1]
        
        # --更新屏幕
        # self.updateFrame(screen, obstacles, skier, score)
        # clock.tick(cfg.FPS)
        screen.fill(BACKGROUNDCOLOR)
        screen.blit(skier.person, skier.rect)
        pygame.display.update()

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return
        pygame.display.update()

'''创建障碍物'''
def createObstacles(self, s, e, num=10):
    obstacles = pygame.sprite.Group()
    locations = []
    for i in range(num):
        row = random.randint(s, e)
        col = random.randint(0, 9)
        location  = [col * 64 + 20, row * 64 + 20]
        if location not in locations:
            locations.append(location)
            attribute = random.choice(['tree', 'flag'])
            image = self.resource_loader.images[attribute]
            obstacle = ObstacleSprite(image, location, attribute)
            obstacles.add(obstacle)
    return obstacles


'''run'''
if __name__ == '__main__':
    highest_score = 0
    flag = True
    while True:
        main()
        if not flag: break
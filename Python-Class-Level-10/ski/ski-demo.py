import os
import pygame
import random
import sys
import cfg

WINDOWWIDTH = 640
WINDOWHEIGHT = 640
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 60

'''滑雪者类'''
class SkierSprite(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        # 滑雪者的朝向(-2到2)
        self.direction = 0
        self.image_fall = images[-1]
        self.images = images[:-1]
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.speed = [self.direction, 6 - abs(self.direction) * 2]
    '''改变滑雪者的朝向. 负数为向左，正数为向右，0为向前'''
    def turn(self, num):
        self.direction += num
        self.direction = max(-2, self.direction)
        self.direction = min(2, self.direction)
        center = self.rect.center
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
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
        self.image = self.image_fall
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
    mainClock = pygame.time.Clock()

    # Set up the window.
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Ski Game')
    pygame.mouse.set_visible(False)

    # Set up the fonts.
    font = pygame.font.SysFont(None, 48)

    # Set up sounds.
    pygame.mixer.init()
    pygame.mixer.music.load('resources/audios/bgm.mp3')    

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

    # Run the game loop.
    while True:
        # Check for events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


'''配置类'''
class Config():
    # 根目录
    rootdir = os.path.split(os.path.abspath(__file__))[0]
    # FPS
    FPS = 40
    # 屏幕大小
    SCREENSIZE = (640, 640)
    # 标题
    TITLE = 'Ski Game'
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
    # 字体路径
    FONT_PATHS_DICT = {
        '1/5screenwidth': {'name': os.path.join(rootdir.replace('ski', 'base'), 'resources/fonts/simkai.ttf'), 'size': SCREENSIZE[0] // 5},
        '1/20screenwidth': {'name': os.path.join(rootdir.replace('ski', 'base'), 'resources/fonts/simkai.ttf'), 'size': SCREENSIZE[0] // 20},
        'default': {'name': os.path.join(rootdir.replace('ski', 'base'), 'resources/fonts/simkai.ttf'), 'size': 30},
    }

def ShowStartInterface(self, screen):
        screen.fill((255, 255, 255))
        tfont = self.resource_loader.fonts['1/5screenwidth']
        cfont = self.resource_loader.fonts['1/20screenwidth']
        title = tfont.render(u'滑雪游戏', True, (255, 0, 0))
        content = cfont.render(u'按任意键开始游戏', True, (0, 0, 255))
        trect = title.get_rect()
        trect.midtop = (self.cfg.SCREENSIZE[0] / 2, self.cfg.SCREENSIZE[1] / 5)
        crect = content.get_rect()
        crect.midtop = (self.cfg.SCREENSIZE[0] / 2, self.cfg.SCREENSIZE[1] / 2)
        screen.blit(title, trect)
        screen.blit(content, crect)
        while True:
            for event in pygame.event.get():
                # if event.type == pygame.QUIT:
                #     QuitGame()
                if event.type == pygame.KEYDOWN:
                    return
            pygame.display.update()

'''游戏开始界面'''
def GameStartInterface(screen, sounds, cfg):
    # dino = Dinosaur(cfg.IMAGE_PATHS['dino'])
    # ground = pygame.image.load(cfg.IMAGE_PATHS['ground']).subsurface((0, 0), (83, 19))
    # rect = ground.get_rect()
    # rect.left, rect.bottom = cfg.SCREENSIZE[0]/20, cfg.SCREENSIZE[1]
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()
    press_flag = False
    while True:
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

'''run'''
if __name__ == '__main__':
    highest_score = 0
    flag = True
    while True:
        main()
        if not flag: break
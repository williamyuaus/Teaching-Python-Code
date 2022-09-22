import os
import pygame
import random
import sys

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

pygame.init()
clock = pygame.time.Clock()
# windowSurface = pygame.display.set_mode((Config.SCREENSIZE))
pygame.display.set_caption(Config.TITLE)
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(Config.SCREENSIZE)
ShowStartInterface(screen)
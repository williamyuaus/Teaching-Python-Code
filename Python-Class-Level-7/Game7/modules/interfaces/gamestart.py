'''
Function:
    游戏开始界面
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import sys
import random
import pygame
from sprites.dinosaur import Dinosaur



'''游戏开始界面'''
def GameStartInterface(screen, sounds, cfg):
    dino = Dinosaur(cfg.IMAGE_PATHS['dino'])
    ground = pygame.image.load(cfg.IMAGE_PATHS['ground']).subsurface((0, 0), (83, 19))
    rect = ground.get_rect()
    rect.left, rect.bottom = cfg.SCREENSIZE[0]/20, cfg.SCREENSIZE[1]
    clock = pygame.time.Clock()
    press_flag = False
    while True:
        pygame.display.update()

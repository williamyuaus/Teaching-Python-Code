import cfg
import sys
import random
import pygame
from modules import *

def main(highest_score):
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('T-Rex Rush')
    GameStartInterface(screen, cfg)

    highest_score = highest_score
    clock = pygame.time.Clock()
    while True:
        screen.fill(cfg.BACKGROUND_COLOR)
        pygame.display.update()
        clock.tick(cfg.FPS)

if __name__ == '__main__':
    highest_score = 0
    while True:
        flag, highest_score = main(highest_score)
        if not flag: break
import cfg
import sys
import random
import pygame

def main(highest_score):
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('T-Rex Rush')
    GameStartInterface(screen, cfg)

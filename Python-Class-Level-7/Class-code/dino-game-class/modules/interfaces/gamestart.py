import sys
import pygame

def GameStartInterface(screen, cfg):
    clock = pygame.time.Clock()
    while True:
        screen.fill(cfg.BACKGROUND_COLOR)
        pygame.display.update()
        clock.tick(cfg.FPS)
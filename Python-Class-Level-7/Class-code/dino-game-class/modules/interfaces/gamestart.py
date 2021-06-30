import sys
import pygame

def GameStartInterface(screen, cfg):
    clock = pygame.time.Clock()
    press_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    press_flag = True
        screen.fill(cfg.BACKGROUND_COLOR)
        pygame.display.update()
        clock.tick(cfg.FPS)
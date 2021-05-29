#following tutorial sortof

import pygame

WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PVP Packman")

GREEN = 0,255,0
FPS = 60

def display():
    WIN.fill(GREEN)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        display()

    pygame.quit()

if __name__ == "__main__":
    main()
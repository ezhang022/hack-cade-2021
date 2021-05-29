#following tutorial sortof

import pygame
import sys
import os
pygame.init()
pygame.font.init()



def display():
    mouse = pygame.mouse.get_pos()
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND, (0,0))
    
    #"Username" Button
    pygame.draw.rect(WIN, LIGHT_GREY, [USERNAME_POS_X, USERNAME_POS_Y, USERNAME_SIZE_X, USERNAME_SIZE_Y])
    username = FONT.render(user_text, True, BLACK)
    WIN.blit(username, (USERNAME_POS_X, USERNAME_POS_Y))

    #"Find Game" button
    pygame.draw.rect(WIN,LIGHT_GREY,[FIND_GAME_POS_X, FIND_GAME_POS_Y, FIND_GAME_SIZE_X, FIND_GAME_SIZE_Y]) 
    if FIND_GAME_POS_X <= mouse[0] <= FIND_GAME_POS_X + FIND_GAME_SIZE_X and FIND_GAME_POS_Y <= mouse[1] <= FIND_GAME_POS_Y + FIND_GAME_SIZE_Y:
        pygame.draw.rect(WIN, GREEN, [FIND_GAME_POS_X, FIND_GAME_POS_Y, FIND_GAME_SIZE_X, FIND_GAME_SIZE_Y])
    WIN.blit(FIND_GAME, (FIND_GAME_POS_X + FIND_GAME_SIZE_X/4, FIND_GAME_POS_Y + FIND_GAME_SIZE_Y/3))

    #"Quit Button"
    pygame.draw.rect(WIN, LIGHT_GREY, [QUIT_POS_X, QUIT_POS_Y, QUIT_SIZE_X, QUIT_SIZE_Y])
    if QUIT_POS_X <= mouse[0] <= QUIT_POS_X + QUIT_SIZE_X and QUIT_POS_Y <= mouse[1] <= QUIT_POS_X + QUIT_SIZE_Y:
        pygame.draw.rect(WIN, RED, [QUIT_POS_X, QUIT_POS_Y, QUIT_SIZE_X, QUIT_SIZE_Y])
    WIN.blit(QUIT, (QUIT_POS_X + QUIT_POS_X/7, QUIT_POS_Y + QUIT_SIZE_Y/3))

    pygame.display.update()

def find_game_screen():
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND, (0,0))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    disp = True
    while run:
        mouse = pygame.mouse.get_pos()

        clock.tick(FPS)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if FIND_GAME_POS_X <= mouse[0] <= FIND_GAME_POS_X + FIND_GAME_SIZE_X and FIND_GAME_POS_Y <= mouse[1] <= FIND_GAME_POS_Y + FIND_GAME_SIZE_Y:
                    # Your Code Here Kai for what you want button to do
                    disp = False
                    find_game_screen()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_POS_X <= mouse[0] <= QUIT_POS_X + QUIT_SIZE_X and QUIT_POS_Y <= mouse[1] <= QUIT_POS_X + QUIT_SIZE_Y:  #if mouse click is in these two areas
                    pygame.quit()

            if event.type == pygame.KEYDOWN:
                global user_text
                user_text += event.unicode
                    

        if disp == True:
            display()

    pygame.quit()

if __name__ == "__main__":
    #Setting Up
    DIMENSIONS = (1000,1000)
    WIN = pygame.display.set_mode(DIMENSIONS)
    WIDTH = WIN.get_width()
    HEIGHT = WIN.get_height()
    BACKGROUND = pygame.image.load('boxes.png')
    FPS = 60
    pygame.display.set_caption("PVP Packman")

    #Colors
    BLACK = 0,0,0
    WHITE = 255,255,255
    RED = 255,0,0
    GREEN = 0,255,0
    LIGHT_GREY = 211,211,211


    #text
    DEFAULT_FONT = pygame.font.get_default_font()
    FONT = pygame.font.SysFont(DEFAULT_FONT, 30)
    FONT2 = pygame.font.SysFont(DEFAULT_FONT, 60)

    FIND_GAME = FONT.render('Find Game', True, BLACK)
    QUIT = FONT.render('Quit', True, BLACK)
    user_text = ''


    #Buttons
    USERNAME_POS_X = 282
    USERNAME_POS_Y = 407
    USERNAME_SIZE_X = 437
    USERNAME_SIZE_Y = 69

    FIND_GAME_POS_X = 166
    FIND_GAME_POS_Y = 614
    FIND_GAME_SIZE_X = 219
    FIND_GAME_SIZE_Y = 69

    QUIT_POS_X = 603
    QUIT_POS_Y = 614
    QUIT_SIZE_X = 219
    QUIT_SIZE_Y = 69
    
    main()
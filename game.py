import pygame
from pygame.locals import *
import time
import math

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pacman Game')

# define game variables
tile_size = 50
score = 0
invincibility = False

# load images
bg_img = pygame.image.load('black.png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))


#graphics junk
font = pygame.font.SysFont('Bauhaus 93', 30)
white = (255,255,255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))


class Player():
    def __init__(self, x, y):
        img = pygame.image.load('pacmanyellow.png')
        self.image = pygame.transform.scale(img, (50, 50))

        self.right = self.image
        self.left = pygame.transform.rotate(self.image, 180)
        self.up = pygame.transform.rotate(self.image, 90)
        self.down = pygame.transform.rotate(self.image, 270)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.prevdir = 0
        self.turndir = None
        self.cycles = 0

    def legal_check(self, prevdir, direction):
        global world_data
        tile_x_pix = self.rect.x
        tile_y_pix = self.rect.y

        if (prevdir == 0 and direction == 3) or (prevdir == 3 and direction == 1) or (prevdir == 0 and direction == 2) or (prevdir == 3 and direction == 0) :
            tile_x_pos=math.ceil(tile_x_pix/50)
            tile_y_pos=math.floor(tile_y_pix/50)
        elif(prevdir ==1 and direction ==3):
            tile_x_pos=math.floor(tile_x_pix/50)
            tile_y_pos=math.floor(tile_y_pix/50)
        elif (prevdir ==2 and direction ==0):
            tile_x_pos=math.ceil(tile_x_pix/50)
            tile_y_pos=math.ceil(tile_y_pix/50)
        else:
            tile_x_pos=math.floor(tile_x_pix/50)
            tile_y_pos=math.ceil(tile_y_pix/50)

        if direction == 0:
            tile_x_pos=round((tile_x_pix - 50)/50)
        elif direction == 1:
            tile_x_pos=round((tile_x_pix + 50)/50)
        elif direction == 2:
            tile_y_pos=round((tile_y_pix - 50)/50)
        elif direction == 3:
            tile_y_pos=round((tile_y_pix + 50)/50)
        if world_data[tile_y_pos][tile_x_pos] == 1:
            return False
        return True

    def update(self):
        dx=0
        dy=0
        key=pygame.key.get_pressed()

        any_key_pressed=key[pygame.K_LEFT] or key[pygame.K_RIGHT] or key[pygame.K_UP] or key[pygame.K_DOWN]

        if self.cycles > 0:
            self.cycles -= 1
            if self.turndir == 0:
                dx=-5
            elif self.turndir == 1:
                dx=5
            elif self.turndir == 2:
                dy=-5
            elif self.turndir == 3:
                dy=5

            self.rect.x += dx
            self.rect.y += dy

            screen.blit(self.image, self.rect)
            return

        if key[pygame.K_LEFT] and self.legal_check(self.prevdir, 0):
            dx -= 5
            self.image=self.left
            self.prevdir=0
        elif key[pygame.K_RIGHT] and self.legal_check(self.prevdir, 1):
            dx += 5
            self.image=self.right
            self.prevdir=1
        elif key[pygame.K_UP] and self.legal_check(self.prevdir, 2):
            dy -= 5
            self.image=self.up
            self.prevdir=2
        elif key[pygame.K_DOWN] and self.legal_check(self.prevdir, 3):
            dy += 5
            self.image=self.down
            self.prevdir=3
        else:
            if self.prevdir == 0:
                dx -= 5
                self.image=self.left
            elif self.prevdir == 1:
                dx += 5
                self.image=self.right
            elif self.prevdir == 2:
                dy -= 5
                self.image=self.up
            elif self.prevdir == 3:
                dy += 5
                self.image=self.down



        # check for collision
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx=0

            elif tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy=0


        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('point.png')
        self.image = pygame.transform.scale(img, (20,20))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class Fruit(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('strawberry.png')
        self.image = pygame.transform.scale(img, (40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class Ghost(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('dummyghost.png')
        self.image = pygame.transform.scale(img, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class World():
    def __init__(self, data):

        self.tile_list=[]

        wall_img=pygame.image.load('blue.png')

        row_count=0
        for row in data:
            col_count=0
            for tile in row:
                if tile == 1:
                    img=pygame.transform.scale(
                        wall_img, (tile_size, tile_size))
                    img_rect=img.get_rect()
                    img_rect.x=col_count * tile_size
                    img_rect.y=row_count * tile_size
                    tile=(img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    coin = Coin(col_count * tile_size + (tile_size // 2), row_count*tile_size + (tile_size // 2))
                    coin_group.add(coin)
                if tile == 3:
                    fruit = Fruit(col_count * tile_size + (tile_size // 2), row_count*tile_size + (tile_size // 2))
                    fruit_group.add(fruit)
                if tile == 4:
                    ghost = Ghost(col_count * tile_size + (tile_size // 2), row_count*tile_size + (tile_size // 2))
                    ghost_group.add(ghost)                                        
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


world_data=[
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 2, 2, 2, 2, 1, 3, 2, 2, 2, 2, 3, 1, 2, 2, 2, 2, 0, 1],
[1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1],
[1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1],
[1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1],
[1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1],
[1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1],
[1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1],
[1, 2, 1, 1, 1, 2, 1, 3, 2, 2, 2, 2, 3, 1, 2, 1, 1, 1, 2, 1],
[1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
[1, 3, 1, 2, 2, 2, 1, 2, 1, 0, 0, 1, 2, 1, 2, 2, 2, 1, 3, 1],
[1, 1, 1, 2, 1, 2, 1, 2, 1, 4, 4, 1, 2, 1, 2, 1, 2, 1, 1, 1],
[1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1],
[1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1],
[1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1],
[1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1],
[1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1],
[1, 0, 2, 2, 2, 2, 1, 3, 2, 2, 2, 2, 3, 1, 2, 2, 2, 2, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

player=Player(50, 50)
coin_group = pygame.sprite.Group()
fruit_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
world=World(world_data)


clock=pygame.time.Clock()
run=True
while run:
    clock.tick(60)
    screen.blit(bg_img, (0, 0))

    world.draw()
    player.update()
    coin_group.draw(screen)
    fruit_group.draw(screen)
    ghost_group.draw(screen)

    draw_text('Score: ' + str(score), font, white, tile_size, 10)

    if pygame.sprite.spritecollide(player, coin_group, True):
        score += 10
    
    if pygame.sprite.spritecollide(player, fruit_group, True):
        invincibility = True

    if pygame.sprite.spritecollide(player, ghost_group, False):
        run = False

    if invincibility:
        draw_text("INVINCIBILITY ON", font, white, 715, 10)
        #this is also supposed to have a timer and a countdown for when it ends but i'm dumb and can't figure it out kai help pls

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()

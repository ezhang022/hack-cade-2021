import pygame 
import pygame.locals
from pygase import Client


### SETUP ###

# Subclass pygase classes to scope event handlers and game-specific variables.
class ChaseClient(Client):
    def __init__(self):
        super().__init__()
        self.player_id = None
        self.status = "lobby"
        self.match_id =None
        
        #register stuff
        self.register_event_handler("PLAYER_CREATED", self.on_player_created)
        self.register_event_handler("JOINED_QUE", self.on_joined_que)
        self.register_event_handler("JOINED_GAME", self.on_joined_game)


    # "PLAYER_CREATED" event handler
    def on_player_created(self, player_id):
        # Remember the id the backend assigned the player.
        self.player_id = player_id
        print(player_id)

    # "JOINED_QUE" event handler
    def on_joined_que(self, status):
        self.status = status
        print(self.status)
    
    # "JOINED_GAME" event handler
    def on_joined_game(self, match_id):
        self.status = "match"
        game_loop_is_running = False
        self.match_id == match_id
        #TODO: add join real game stuff


# Create a client.
client = ChaseClient()

def display():
    mouse = pygame.mouse.get_pos()
    pygame.display.set_caption("PvP Pac-Man")
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND1, (0,0))
    
    #"Username" Button
    pygame.draw.rect(WIN, LIGHT_GREY, [USERNAME_POS_X, USERNAME_POS_Y, USERNAME_SIZE_X, USERNAME_SIZE_Y])
    username = FONT2.render(user_text, True, BLACK)
    WIN.blit(USERNAME_TITLE, (USERNAME_POS_X, USERNAME_POS_Y - 20))
    WIN.blit(username, (USERNAME_POS_X, USERNAME_POS_Y+10))

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

def find_game_screen(position):
    pygame.display.set_caption("PvP Pac-Man - Finding Game")
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND2, (0,0))
    
    WIN.blit(PACMAN, (position.x, position.y))

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    display_one = True
    while run:
        mouse = pygame.mouse.get_pos()

        clock.tick(FPS)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

            

                    
            #quit
            if event.type == pygame.MOUSEBUTTONDOWN and display_one:
                if QUIT_POS_X <= mouse[0] <= QUIT_POS_X + QUIT_SIZE_X and QUIT_POS_Y <= mouse[1] <= QUIT_POS_X + QUIT_SIZE_Y:  #if mouse click is in these two areas
                    run = False

            #username
            if event.type == pygame.KEYDOWN:    #enter username
                global user_text
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if len(user_text) < 10:
                        user_text += event.unicode
            
            #find game
            if event.type == pygame.MOUSEBUTTONDOWN and display_one:
                if FIND_GAME_POS_X <= mouse[0] <= FIND_GAME_POS_X + FIND_GAME_SIZE_X and FIND_GAME_POS_Y <= mouse[1] <= FIND_GAME_POS_Y + FIND_GAME_SIZE_Y:
                    
                    client.dispatch_event("CREATE", user_text)
                    # Wait until "PLAYER_CREATED" has been handled.
                    while client.player_id is None:
                        pass
                    
                    client.dispatch_event("JOIN_QUE", client.player_id)
                    while client.status == "lobby":
                        pass
                    
                    display_one = False
                    pac = pygame.Rect(50, 670, PACMAN_WIDTH, PACMAN_HEIGHT)
                    find_game_screen(pac)
                    
            if client.status =="match":
                pass
                #TODO: launch actual game



        if display_one:
            display()

    pygame.quit()

### MAIN PROCESS ###

if __name__ == "__main__":
    # Connect the client.
    client.connect_in_thread(hostname="localhost", port=8080)
    
    # Set up pygame.
    keys_pressed = set()  # all keys that are currently pressed down
    clock = pygame.time.Clock()
    # Initialize a pygame screen.
    pygame.init()
    pygame.font.init()
    #Setting Up
    DIMENSIONS = (1000,1000)
    WIN = pygame.display.set_mode(DIMENSIONS)
    WIDTH = WIN.get_width()
    HEIGHT = WIN.get_height()
    BACKGROUND1 = pygame.image.load('MainScreen.png')
    BACKGROUND2 = pygame.image.load('LoadingScreen.png')
    PACMAN_IMAGE = pygame.image.load('pacmanyellow.png')
    PACMAN_WIDTH = 50
    PACMAN_HEIGHT = 51
    PACMAN = pygame.transform.scale(PACMAN_IMAGE, (PACMAN_HEIGHT, PACMAN_WIDTH))
    FPS = 50
    

    #Colors
    BLACK = 0,0,0
    WHITE = 255,255,255
    RED = 255,0,0
    GREEN = 0,255,0
    LIGHT_GREY = 211,211,211


    #text
    DEFAULT_FONT = pygame.font.get_default_font()
    FONT = pygame.font.SysFont(DEFAULT_FONT, 30)
    FONT2 = pygame.font.SysFont(DEFAULT_FONT, 80)

    FIND_GAME = FONT.render('Find Game', True, BLACK)
    QUIT = FONT.render('Quit', True, BLACK)
    USERNAME_TITLE = FONT.render("Username:", True, WHITE)
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
    

    pygame.quit()

    # Disconnect afterwards and shut down the server if the client is the host.
    client.disconnect(shutdown_server=True)
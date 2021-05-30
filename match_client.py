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
    
    #"Playername" Button
    pygame.draw.rect(WIN, LIGHT_GREY, [PLAYERNAME_POS_X, PLAYERNAME_POS_Y, PLAYERNAME_SIZE_X, PLAYERNAME_SIZE_Y])
    playername = FONT2.render(user_text, True, BLACK)
    WIN.blit(PLAYERNAME_TITLE, (PLAYERNAME_POS_X, PLAYERNAME_POS_Y - 20))
    WIN.blit(playername, (PLAYERNAME_POS_X, PLAYERNAME_POS_Y+10))

    #"Find Game" button
    pygame.draw.rect(WIN,LIGHT_GREY,[FIND_GAME_POS_X, FIND_GAME_POS_Y, FIND_GAME_SIZE_X, FIND_GAME_SIZE_Y]) 
    if FIND_GAME_POS_X <= mouse[0] <= FIND_GAME_POS_X + FIND_GAME_SIZE_X and FIND_GAME_POS_Y <= mouse[1] <= FIND_GAME_POS_Y + FIND_GAME_SIZE_Y:
        pygame.draw.rect(WIN, GREEN, [FIND_GAME_POS_X, FIND_GAME_POS_Y, FIND_GAME_SIZE_X, FIND_GAME_SIZE_Y])
    WIN.blit(FIND_GAME, (FIND_GAME_POS_X + FIND_GAME_SIZE_X/4, FIND_GAME_POS_Y + FIND_GAME_SIZE_Y/3))

    #"Quit Button"
    pygame.draw.rect(WIN, LIGHT_GREY, [QUIT_POS_X, QUIT_POS_Y, QUIT_SIZE_X, QUIT_SIZE_Y])
    if QUIT_POS_X <= mouse[0] <= QUIT_POS_X + QUIT_SIZE_X and QUIT_POS_Y <= mouse[1] <= QUIT_POS_X + QUIT_SIZE_Y:
        pygame.draw.rect(WIN, RED, [QUIT_POS_X, QUIT_POS_Y, QUIT_SIZE_X, QUIT_SIZE_Y])
    WIN.blit(QUIT, (QUIT_POS_X + QUIT_SIZE_X/2.6, QUIT_POS_Y + QUIT_SIZE_Y/3))

    #"Tutorial" Button
    pygame.draw.rect(WIN, LIGHT_GREY, [TUTORIAL_POS_X, TUTORIAL_POS_Y, TUTORIAL_SIZE_X, TUTORIAL_SIZE_Y])
    if TUTORIAL_POS_X <= mouse[0] <= TUTORIAL_POS_X + TUTORIAL_SIZE_X and TUTORIAL_POS_Y <= mouse[1] <= TUTORIAL_POS_Y + TUTORIAL_SIZE_Y:
        pygame.draw.rect(WIN, GOLD, [TUTORIAL_POS_X, TUTORIAL_POS_Y, TUTORIAL_SIZE_X, TUTORIAL_SIZE_Y])
    WIN.blit(TUTORIAL, (TUTORIAL_POS_X + TUTORIAL_SIZE_X/3.25, TUTORIAL_POS_Y + TUTORIAL_SIZE_Y/2.75))

    pygame.display.update()

def find_game_screen():
    mouse = pygame.mouse.get_pos()
    pygame.display.set_caption("PvP Pac-Man - Finding Game")
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND2, (0,0))
    
    pygame.draw.rect(WIN, LIGHT_GREY, [QUIT_POS_X, QUIT_POS_Y, QUIT_SIZE_X, QUIT_SIZE_Y])
    if QUIT_POS_X <= mouse[0] <= QUIT_POS_X + QUIT_SIZE_X and QUIT_POS_Y <= mouse[1] <= QUIT_POS_X + QUIT_SIZE_Y:
        pygame.draw.rect(WIN, RED, [QUIT_POS_X, QUIT_POS_Y, QUIT_SIZE_X, QUIT_SIZE_Y])
    WIN.blit(QUIT, (QUIT_POS_X + QUIT_POS_X/7, QUIT_POS_Y + QUIT_SIZE_Y/3))

    pygame.display.update()

def tutorial_screen():
    mouse = pygame.mouse.get_pos()
    pygame.display.set_caption("PvP Pac-Man - Tutorial")
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND4, (0,0))

    pygame.draw.rect(WIN, LIGHT_GREY, [BACK_POS_X, BACK_POS_Y, BACK_SIZE_X, BACK_SIZE_Y])
    if BACK_POS_X <= mouse[0] <= BACK_POS_X + BACK_SIZE_X and BACK_POS_Y <= mouse[1] <= BACK_POS_Y + BACK_SIZE_Y:
        pygame.draw.rect(WIN, GOLD, [BACK_POS_X, TUTORIAL_POS_Y, TUTORIAL_SIZE_X, TUTORIAL_SIZE_Y])
    WIN.blit(BACK, (BACK_POS_X + BACK_SIZE_X/2.75, BACK_POS_Y + BACK_SIZE_Y/2.75))

    pygame.display.update()

def match_found_screen():
    pygame.display.set_captaion("PvP Pac-Man - Match Found!")
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND3, (0,0))

    pygame.display.update()
    

def main():
    clock = pygame.time.Clock()
    run = True
    display_main = True
    display_tutorial = False
    display_find_game = False
    while run:
        mouse = pygame.mouse.get_pos()

        clock.tick(FPS)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:   #windows quit button
                run = False

            #quit
            if event.type == pygame.MOUSEBUTTONDOWN and (display_main or display_find_game):
                if QUIT_POS_X <= mouse[0] <= QUIT_POS_X + QUIT_SIZE_X and QUIT_POS_Y <= mouse[1] <= QUIT_POS_Y + QUIT_SIZE_Y:  #if mouse click is within this area
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN and display_main:
                if TUTORIAL_POS_X <= mouse[0] <= TUTORIAL_POS_X + TUTORIAL_SIZE_X and TUTORIAL_POS_Y <= mouse[1] <= TUTORIAL_POS_Y + TUTORIAL_SIZE_Y:
                    display_main = False
                    display_tutorial = True
                    tutorial_screen()
            
            if event.type == pygame.MOUSEBUTTONDOWN and display_tutorial:
                if BACK_POS_X <= mouse[0] <= BACK_POS_X + BACK_SIZE_X and BACK_POS_Y <= mouse[1] <= BACK_POS_Y + BACK_SIZE_Y:
                    display_main = True
                    display_tutorial = False



            #playername
            if event.type == pygame.KEYDOWN and display_main:    #enter playername
                global user_text
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if len(user_text) < 10:
                        user_text += event.unicode

            #find game
            if event.type == pygame.MOUSEBUTTONDOWN and display_main:
                if FIND_GAME_POS_X <= mouse[0] <= FIND_GAME_POS_X + FIND_GAME_SIZE_X and FIND_GAME_POS_Y <= mouse[1] <= FIND_GAME_POS_Y + FIND_GAME_SIZE_Y:
                    client.dispatch_event("CREATE", user_text)
                    # Wait until "PLAYER_CREATED" has been handled.
                    while client.player_id is None:
                        pass
                    
                    client.dispatch_event("JOIN_QUE", client.player_id)
                    while client.status == "lobby":
                        pass
                    
                    display_main = False
                    display_find_game = True

                    find_game_screen()

            # if event.type == pygame.MOUSEBUTTONDOWN and display_find_game:
            #     if QUIT_POS_X <= mouse[0] <= QUIT_POS_X + QUIT_SIZE_X and QUIT_POS_Y <= mouse[1] <= QUIT_POS_Y + QUIT_SIZE_Y:
            #         run = False

            if client.status == "match":
                pass
                #match_found_screen()
                #TODO: launch actual game



        if display_main:
            display()
        if display_find_game:
            find_game_screen()
        if display_tutorial:
            tutorial_screen()

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
    BACKGROUND3 = pygame.image.load('GameFound.png')
    BACKGROUND4 = pygame.image.load('Tutorial.png')
    FPS = 50
    

    #Colors
    BLACK = 0,0,0
    WHITE = 255,255,255
    RED = 255,0,0
    GREEN = 0,255,0
    LIGHT_GREY = 211,211,211
    GOLD = 255, 215, 0


    #text
    DEFAULT_FONT = pygame.font.get_default_font()
    FONT = pygame.font.SysFont(DEFAULT_FONT, 30)
    FONT2 = pygame.font.SysFont(DEFAULT_FONT, 80)

    FIND_GAME = FONT.render('Find Game', True, BLACK)
    QUIT = FONT.render('Quit', True, BLACK)
    PLAYERNAME_TITLE = FONT.render("Playername:", True, WHITE)
    TUTORIAL = FONT.render('Tutorial', True, BLACK)
    BACK = FONT.render('Back', True, BLACK)
    user_text = ''


    #Buttons
    PLAYERNAME_POS_X = 282
    PLAYERNAME_POS_Y = 407
    PLAYERNAME_SIZE_X = 437
    PLAYERNAME_SIZE_Y = 69

    FIND_GAME_POS_X = 166
    FIND_GAME_POS_Y = 614
    FIND_GAME_SIZE_X = 219
    FIND_GAME_SIZE_Y = 69

    QUIT_POS_X = 603
    QUIT_POS_Y = 614
    QUIT_SIZE_X = 219
    QUIT_SIZE_Y = 69

    TUTORIAL_POS_X = 739
    TUTORIAL_POS_Y = 892
    TUTORIAL_SIZE_X = 219
    TUTORIAL_SIZE_Y = 69

    BACK_POS_X = 71
    BACK_POS_Y = 892
    BACK_SIZE_X = 219
    BACK_SIZE_Y = 69
    
    main()
    

    pygame.quit()

    # Disconnect afterwards and shut down the server if the client is the host.
    client.disconnect(shutdown_server=True)
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
        print('joined match')
        print(match_id)
        #TODO: add join real game stuff


# Create a client.
client = ChaseClient()

### MAIN PROCESS ###

if __name__ == "__main__":
    # Connect the client, let the player input a name and join the server.
    client.connect_in_thread(hostname="localhost", port=8080)
    client.dispatch_event("CREATE", input("Player name: "))
    # Wait until "PLAYER_CREATED" has been handled.
    while client.player_id is None:
        pass
    # Set up pygame.
    print("created ham")
    keys_pressed = set()  # all keys that are currently pressed down
    clock = pygame.time.Clock()
    # Initialize a pygame screen.
    pygame.init()
    screen_width = 640
    screen_height = 420
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Start the actual main loop.
    game_loop_is_running = True
    
    while game_loop_is_running:
        # Run at 50 FPS
        dt = clock.tick(50)
        # Clear the screen.
        screen.fill((0, 0, 0))
        # Handle pygame input events.
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                game_loop_is_running = False
            if event.type == pygame.locals.KEYDOWN:
                keys_pressed.add(event.key)
            if event.type == pygame.locals.KEYUP:
                keys_pressed.remove(event.key)
        # Handle player movement.
        if client.status == "lobby" and input("join que") == 'y':
            client.dispatch_event("JOIN_QUE", client.player_id)
            while client.status == "lobby":
                pass
            
        # Do the thing.
        pygame.display.flip()
    # Clean up.
    pygame.quit()

    # Disconnect afterwards and shut down the server if the client is the host.
    client.disconnect(shutdown_server=True)
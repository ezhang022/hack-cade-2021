import random
from pygase import GameState, Backend, client


### SETUP ###

# Initialize the game state.
initial_game_state = GameState(
    players={},  # dict with `player_id: player_dict` entries
    matches={}, # dict iwth 'match_id: match_dict'
    in_que=[], #list with player ids
)

# Define the game loop iteration function.
def time_step(game_state, dt):
    # Before a player joins, updating the game state is unnecessary.
    if len(game_state.players) == 0:
        return {}

    
    
    # Check que and create match.
    if len(game_state.in_que) >=3:
        player_ids = [game_state.in_que[0],game_state.in_que[1],game_state.in_que[2]]
        client_addresses = []
        for playerid in player_ids:
            client_addresses.append(game_state.players[playerid]["address"])
        matches = game_state.matches.copy()
        in_que = game_state.in_que.copy()
        players = game_state.players.copy()
        match_id = len(matches)
        matches[match_id] = player_ids
        
        for player_id, client_address in list(zip(player_ids, client_addresses)):
            players[player_id]["status"] = "match"
            in_que.remove(player_id)
            backend.server.dispatch_event("JOINED_GAME", match_id, target_client=client_address)
        print("1")
        print(players, matches, in_que)
        return {
            "players": players,  
            "matches": matches,
            "in_que" : in_que,
        }

    return {}

backend = Backend(initial_game_state, time_step)

def on_create(player_name, game_state, client_address, **kwargs):
    print(f"{player_name} joined.")
    player_id = len(game_state.players)
    # Notify client that the player successfully joined the game.
    backend.server.dispatch_event("PLAYER_CREATED", player_id, target_client=client_address)
    return {
        "players": {player_id: {"name": player_name, "status": "lobby", "address" :client_address}},
        "matches": game_state.matches,
        "in_que" : game_state.in_que,
    }

def on_join_que(player_id, game_state, client_address, **kwargs):
    print("2")
    in_que = game_state.in_que.copy()
    in_que.append(player_id)
    players = game_state.players
    players[player_id]["status"] = "que"
    backend.server.dispatch_event("JOINED_QUE", "que", target_client=client_address)
    print("3")
    print(players)
    print(in_que)
    return {
        "players": players,
        "matches": game_state.matches,
        "in_que" : in_que,
    }


# Register the handlers.
backend.game_state_machine.register_event_handler("CREATE", on_create)
backend.game_state_machine.register_event_handler("JOIN_QUE", on_join_que)

### MAIN PROCESS ###

if __name__ == "__main__":
    backend.run(hostname="localhost", port=8080)
# PvP-Pacman

## What is Pacman PvP?
Pacman PvP is a remake of the classic game Pacman, one that all three members of our team have fond memories of. Growing up with simple computer games, we can all clearly remember the suspense of a ghost closing in behind you and the triumph that comes when you manage to eat a power-up dot and chase the ghost instead.
##
Because of quarantine, the best games are multiplayer ones. We turned Pacman into a competitive battle-style multiplayer game. In each game, four players compete against each other to be the last one standing.
##
Like classic Pacman, the player can collect points, but they use these points to spawn an own army of offensive ghosts. Each dot is worth 10 points, and when the player collects 200 points they spawn a ghost for their team. Their team of ghosts does not hurt them and instead attacks enemy players.
Collecting a fruit will give the player the ability to catch ghosts for 15 seconds. While the player has the power-up, the top right corner displays "INVINCIBILITY ON". Each ghost the player touches with invincibility will disappear and reward 50 points. Both fruits and points will respawn after a certain time, to ensure the game stays interesting.
##
If an enemy ghost touches the player or if their ghosts run out, the player is out. The last player alive wins!

## How we built it
The game itself and the client were built using Pygame, while the matchmaking and server are handled by Linode.
##
Pacman PvP's client is the game's starting screen. It includes a tutorial page for players who are new to the game, and an option to quit once someone is done playing. The player can type in a username and click start game, which brings them to a loading screen where they will be matched with other players.
##
In the Pacman PvP client, we created backgrounds using Paint.net that would serve as the foundation of our client windows. Jumping off from these backgrounds, we were able to easily add in objects such as buttons and text boxes that gave our client seamless functionality. This allows a player to effortlessly navigate from the landing page, to the tutorial page, to jumping straight into the game.
##
Linode handles the matchmaking and connects the player to three other players, and then forwards everyone to the game server. The game server is also hosted on a Linode server, making Pacman PvP easily accessible from any part of the world. This server connects the players and synchronizes their games so that the movements and actions of the four players line up.
##
The world, players, and sprites were built using Pygame, while the Linode game server communicated player and game actions in real time. The points, fruits, and ghosts are Pygame sprites. The game's map of walls, points, fruits, players, and enemies was built using a tile system, where each tile was coded to start with a certain object, and loaded that way. Pygame's collide module was used to prevent Pacman from going through walls and to help him interact with points, fruits, and ghosts. Pacman movement and animation is connected to key presses controlling Pacman's movement.

## Challenges we ran into
Most of our challenges were from bugs that we couldn't figure out and confusing naming systems. Part of this is because most of us are used to coding on our own and did not comment our code as much as we should have, which we learned the hard way. 
##
We also struggled with the multiplayer aspect of the game, since we started off by programming Pacman for a single player from scratch, so it was difficult to implement some features when transitioning to multiple players. The structure of the game was built for one player, so a lot had to be changed so the game worked for multiple players.
##
The pathfinding algorithm for ghosts was also a challenge since ghosts had many players and situations to take into account, but we eventually thought our way through it.
##
Everything (in general) was a challenge because it was our first time using the tools we did and also our first time creating a multiplayer game.
##
Hopefully, these challenges made us better programmers for the future!

## Accomplishments that we're proud of
Learning so much and using new tools is something our team is very proud of. None of us have had experience with creating games at all, not to mention the fact that we were using completely new tools. Managing to create the game and get it running is something we are very proud of, especially with the time constraints. It's very motivating to see countless words and carefully thought-out logic typed into Visual Studio Code come to life. It was also very fun to play against each other, especially because it was the product of our own hard work. 
##
Learning to use new tools is what we are most proud of. We struggled through tutorials and bugs but made everything work in the end, which is a great accomplishment for us even if it is just a simple game.

## What we learned
It was the first time the three of us used Pygame and Linode. Creating a multiplayer game taught us a lot. Pygame really showed us a whole new side of Python. 
##
Previously we had only used Python for computational purposes, but during Hack-cade, we learned how to use Python to create a playable character, sprites, and an interactive world. 
##
Using Linode taught us a lot about servers. We learned how to host both a match-making server that connected players and the game server which allowed multiple player actions to happen in real-time. 

## What's next for Pacman PvP
Though we've managed to accomplish a lot in a short time, Pacman PvP can certainly improve. If we decide to take our project further, some features we might build are private rooms with codes, different maps, various difficulty settings such as smarter ghosts and higher speed, and modes with a different number of players. Game mechanics that can be added to Pacman PvP are different functions of the fruits, more map interactions such as portals, and more player-player interactions.

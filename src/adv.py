from room import Room
from player import Player
import os
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# create items


# Randomize allocation to rooms (except make sure grappling is in overlook)
# print(room_items["grappling_hook"])


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

nav = ['n','e','s','w']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

new_name = input("What is your name? ")
new_player = Player(str(new_name),room['outside'], 100, [])
print(new_player)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# set current room, player name
# 
# do while true
# conditional based on input check ._to based on current room

def player_moves(move):
    #assign current room
    room = new_player.room
    # new_room = whatever the room represented by {move}
    #check if the room has the attribute --> can you make the move?
        #if the move is allowed update the room in the player object to the new room 
        #else if the move is not allowed, don't change object, print message

while True:
    room = new_player.room
    name = new_player.name
    health = new_player.health
    inventory = new_player.inventory


    print(f"\nPlayer: {name}\n{room}\nHealth: {health}\nInventory: {inventory}")
    move = input(f"")






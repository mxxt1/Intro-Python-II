from room import Room
from player import Player
from items import Items
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
room_items = {
    "hook": Items("hook", "A deployable hook for crossing chasms", 0, 0, 0),
    "sword": Items("Wooden Sword", "...It's a pretty bad sword", 2, 0, 0),
    "broadsword": Items("Hero's Sword", "Now this is a sword", 8, 0,0),
    "shield": Items("Sturdy Shield", "A reliable shield", 0, 2, 0),
    "elixir": Items("Healing Elixir", "Soylent Green is people!", 0, 0, 10)
}

# Randomize allocation to rooms (except make sure grappling is in overlook)
# print(room_items["grappling_hook"])
room["outside"].addInventory(random.choice(list(room_items.keys())))
room["foyer"].addInventory(random.choice(list(room_items.keys())))
room["overlook"].addInventory(random.choice(list(room_items.keys())))
room["overlook"].addInventory(room_items["hook"].name)
room["narrow"].addInventory(random.choice(list(room_items.keys())))
room["treasure"].addInventory(random.choice(list(room_items.keys())))


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


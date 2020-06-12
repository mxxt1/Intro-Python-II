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

room["outside"].addItem(random.choice(list(room_items.keys())))
room["foyer"].addItem(random.choice(list(room_items.keys())))
room["overlook"].addItem(random.choice(list(room_items.keys())))
room["overlook"].addItem(room_items["hook"].name)
room["narrow"].addItem(random.choice(list(room_items.keys())))
room["treasure"].addItem(random.choice(list(room_items.keys())))


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
# print(new_player)

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

# def player_moves(move):
#     #assign current room
#     room = new_player.room
#     # new_room = whatever the room represented by {move}
#     #check if the room has the attribute --> can you make the move?
#         #if the move is allowed update the room in the player object to the new room 
#         #else if the move is not allowed, don't change object, print message

def clearTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


while True:
    room = new_player.room
    name = new_player.name
    health = new_player.health
    inventory = new_player.inventory
    room_items = new_player.room.items


    print(new_player)
    move = input(f"\n\nWhat would you like to do, {name}?\nNavigation: (n)orth, (e)ast, (s)outh, (w)est\nActions: type 'get [item]' or 'drop [item]'\nExit: q\n\n\nEnter selection: ")
    #Navigation
    if move.lower() in nav:
        newRoom = f'{move}_to'
        if hasattr(room,newRoom) and getattr(room,newRoom) != None:
            new_player.room = getattr(room,newRoom)
            clearTerminal()
        else:
            clearTerminal()
            print("You cannot go that way\n\n")
    elif ('get' in str(move).lower()):
        words = move.lower().split()
        if words[1] in room_items:
            activeItem = str(words[1])
            room.removeItem(words[1])
            new_player.addItem(words[1])
            clearTerminal()
        else:
            clearTerminal()
            print(f'\n\nSorry, there is no {words[1]} in {room.name}\n\n')
    elif ('drop' in str(move).lower()):
        words = move.lower().split()
        if words[1] in inventory:
            room.addItem(words[1])
            new_player.removeItem(words[1])
            clearTerminal()
    elif (move == 'q'):
        clearTerminal()
        print(f'Thanks for playing, {name}\n\n\n\n')
        break

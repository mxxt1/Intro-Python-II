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
    "hook": Items("Hook", "A deployable hook for crossing chasms", 0, 0, 0),
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

print("       ~~~~~****WELCOME TO PURGATORY****~~~~~~")
print("\"A game where you literally walk around purgatory\"(TM)(C)\n\n")

# Make a new player object that is currently in the 'outside' room.

np_name = input("What's your name? ")
new_player = Player(str(np_name),room['outside'],int(100),[])


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

def playerMove(move):
    room = new_player.room
    newRoom = f'{move}_to'
    if (hasattr(room,newRoom) and getattr(room,newRoom) != None):
        new_player.room = getattr(room,newRoom)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('You can\'t go that way, friend.')

while True: 
    location = new_player.room
    name = new_player.player
    health = new_player.health
    items = new_player.room.items
    inventory = new_player.inventory
  
    print(f"\n\nPlayer: {name}\nHealth: {health}\nCurrent Location: {location}Room Items: {items}\n\n")
    move = input(f"{name}, what would you like to do? \n\nOptions: \n\nNavigation: (n)orth, (e)ast, (s)outh, (w)est \n\nActions: (v)iew inventory, (p)ick up item, ('get' ',' 'item'), (r)emove item \n\nQuit: (q)uit\n\nYour Selection: ")
    move = move.lower()
    # Navigation --> move this to player.py
    if (move in nav):
        playerMove(move)
    # Pick items
    elif ("get" in move):
        words = move.split(' ',-1)
        print(words)
        print(room_items[f'{words[1]}'].name)
        if (words[1] in items):
            item = str(words[1])
            new_player.addItem(item)
            location.removeInventory(item)
            os.system('cls' if os.name == 'nt' else 'clear')
    elif(move == 'p'):
        if (len(room_items) > 1):
            count = int(0)
            for item in items:
                print(f'{count} {item}')
                count += 1
            print('\n\n')
            itemInd = input(f'Which item would you like to select? ')
            print(items[int(itemInd)])
            new_player.addItem(items[int(itemInd)])
            location.removeInventory(items[int(itemInd)])
            os.system('cls' if os.name == 'nt' else 'clear')
            room_items[item].onTake(item)
            room_items[item].onTake(f'{item}')
        else:
            # print(room_items[0])
            item = str(room_items[0])
            new_player.addItem(item)
            location.removeInventory(item)
            room_items[item].onTake(f'{item}')
            os.system('cls' if os.name == 'nt' else 'clear')
            room_items[item].onTake(item)
            room_items[item].onTake(f'{item}')
    # View and edit inventory
    elif(move == 'v'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n{name}\'s Inventory:')
        count = int(0)
        for item in inventory:
            print(f'{count} {item}')
            count += 1
        invAction = input(f'What would you like to do?\nOptions: (r)emove item, (n)othing\nYour selection: ')
        if (invAction == 'r'):
            os.system('cls' if os.name == 'nt' else 'clear')
            invCount = int(0)
            for item in inventory:
                print(f'{invCount} {item}')
                invCount += 1
            selection = input(f'Which item would you like to remove? ')
            new_player.removeItem(inventory[int(selection)])
            os.system('cls' if os.name == 'nt' else 'clear')
    elif (move == 'q'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Thanks for playing, {name}')
        break
    #unconfigured inputs    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n!!*****YOU CAN'T DO THAT, BUDDY.*****!!\n")
    


# if (move == 'n' and hasattr(location,'n_to') and location.n_to != None):
#         new_player.room = new_player.room.n_to
#         os.system('cls' if os.name == 'nt' else 'clear')
#     elif (move == 'e' and hasattr(location,'e_to') and location.e_to != None):
#         new_player.room = new_player.room.e_to
#         os.system('cls' if os.name == 'nt' else 'clear')
#     elif (move == 's' and hasattr(location,'s_to') and location.s_to != None):
#         new_player.room = new_player.room.s_to
#         os.system('cls' if os.name == 'nt' else 'clear')
#     elif (move == 'w' and hasattr(location,'w_to') and location.w_to != None):
#         new_player.room = new_player.room.w_to
#         os.system('cls' if os.name == 'nt' else 'clear')
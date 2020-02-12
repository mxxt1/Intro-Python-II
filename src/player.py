# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, player, room, health, inventory):
        self.player = player
        self.room = room
        self.health = health
        self.inventory = inventory
    
    #prints the class as a string instead of memory id 
    def __str__(self):
        return f'Player name: {self.player}\nCurrent Room: {self.room}'
    
    

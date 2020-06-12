# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, health, inventory=[]):
        self.name = name
        self.room = room
        self.health = health
        self.inventory = inventory
    
    def __str__(self):
        return f'Player: {self.name}\n{self.room}\nHealth: {self.health}\nInventory: {self.inventory}'
    
    def addItem(self,item):
        self.inventory.append(item)

    def removeItem(self,item):
        self.inventory.remove(item)
    
    
    

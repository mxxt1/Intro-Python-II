# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None
    
    def __str__(self):
        return f'\n Room name: {self.name} \n Description:\n {self.description}\n\n'
    
    def addInventory(self,item):
        self.items.append(item)
    
    def removeInventory(self,item):
        self.items.remove(item)



        
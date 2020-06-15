class Items:
    def __init__(self,name,description,damage,defense,healing):
        self.name = name
        self.description = description
        self.damage = damage
        self.defense = defense
        self.healing = healing
    
    def __str__(self):
        return f"Item Name: {self.name}\nDescription: {self.description}"
    
    def onTake(self, name):
        return print(f'You have picked up {self.name}')
    
    def onDrop(self):
        return print(f'You have dropped {self.name}')
    


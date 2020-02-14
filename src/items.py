class Items:
    def __init__(self, name, description, damage, defense, healing):
        self.name = name
        self.description = description
        self.damage = damage
        self.defense = defense
        self.healing = healing
    
    def __str__(self):
        return f'Item Name: {self.name}\nItem Description: {self.description}\nDamage: {self.damage}\nDefense: {self.defense}\nHealing: {self.healing}'
    
    def onTake(self,name):
        print(f'you have picked up {name}')
class Items:
    def __init__(self,name,description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"Item Name: {self.name}\nDescription: {self.description}"
    
    def take(self):
        print(f'You have picked up {self.name}')

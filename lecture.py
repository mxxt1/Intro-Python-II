# OOP
## Objects or Class
### blueprints/prototypes
### holds data :attributes
### methods:functions

# Pet Blueprint (Class)
## name, height, gender, species, diet, number of legs
### feed_pet
### play()

# Pet("rover","2","M","dog",etc etc)

class Store:
    #attributes
    #name
    #categories
    #inventory
    #employees

    # constructor
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories
        self.employees = []
    
    def __str__(self):
        return f'name is {self.name}, categories are {self.categories} and employees are {self.employees}'
    
    def __repr__(self):
        return f'self.name = {self.name} ; categories = {self.categories}'
        



sports_store = Store("matt's store",["football","basketball","baseball"]), ["test"]

print(sports_store)


# REPL <-- Read evaluate print loop
# 



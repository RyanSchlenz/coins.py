# class inheritance and polymorphism
# class inheritance - new class created gets methods from parent class
# polymorphism - same function name, but does something different 

import random

# general class that works for everything
# **kwargs = keyword arguments which allows parent class to accept data from child class
# kwargs takes keywords from child dictionary and packs it down into a dictionary called kwargs

class Coin:
    def __init__(self,rare=False, clean=True, heads = True, **kwargs):

        for key,value in kwargs.items(): # loop through all kwargs to set keys and values
            setattr(self,key,value)

        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self): 
        self.color = self.rusty_color

    def clean(self): 
        self.color = self.clean_color

    # destructor (spending coin)
    def __del__(self):
        print("coin Spent!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "Euro{} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))
        


# pound class inherits from coin class
# first class init function runs, which creates Pound class
# then we get the parents init function (constructor) to do the rest of the setup
# super allows us to access the parent class by unpacking the data from the new class

class One_Pence(Coin):
    def __init__(self): #constructor

        # dictionary of data
        data = {
            "original_value": .01,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
            }
        super().__init__(**data) #inheritance from parent class to create keyword args


class Two_Pence(Coin):
    def __init__(self): #constructor

        # dictionary of data to store data of pound
        data = {
            "original_value": .02,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
            }
        super().__init__(**data) #inheritance from parent class to create keyword args


class Five_Pence(Coin):
    def __init__(self): #constructor

        # dictionary of data to store data of pound
        data = {
            "original_value": 0.05,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
            }
        super().__init__(**data)

        def rust(self): #polymorphism
            self.color = self.clean_color

        def clean(self): # polymorphism
            self.color = self.clean_color

class Ten_Pence(Coin):
    def __init__(self): #constructor

        # dictionary of data to store data of pound
        data = {
            "original_value": 0.10,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.50
            }
        super().__init__(**data)

        def rust(self): #polymorphism
            self.color = self.clean_color

        def clean(self): # polymorphism
            self.color = self.clean_color


class Twenty_Pence(Coin):
    def __init__(self): #constructor

        # dictionary of data to store data of pound
        data = {
            "original_value": 0.20,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5.00
            }
        super().__init__(**data)

        def rest(self): # polymorphism
            self.color = self.clean_color

        def clean(self): # polymorphism
            self.color = self.clean_color


class Fifty_Pence(Coin):
    def __init__(self): #constructor

        # dictionary of data to store data of pound
        data = {
            "original_value": 0.50,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 8.00
            }
        super().__init__(**data)

        def rest(self): # polymorphism
            self.color = self.clean_color

        def clean(self): # polymorphism
            self.color = self.clean_color

class One_Pound(Coin):
    def __init__(self): #constructor

        # dictionary of data to store data of pound
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
            }
        super().__init__(**data) #inheritance from parent class to create keyword args

class Two_Pound(Coin):
    def __init__(self): #constructor

        # dictionary of data to store data of pound
        data = {
            "original_value": 2.00,
            "clean_color": "gold & silver",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 28.4,
            "thickness": 2.50,
            "mass": 12.00
            }
        super().__init__(**data) #inheritance from parent class to create keyword args
            

coins = [One_Pence(), Two_Pence(), Five_Pence(), Ten_Pence(), Twenty_Pence(),
         Fifty_Pence(), One_Pound(), Two_Pound()]

# loop through coins
for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]
    
    string = "{} - Color {}, value:{}, diameter(mm):{}, thickness(mm):{}, number_of_edges:{}, mass(g):{}".format(*arguments)
    print(string)

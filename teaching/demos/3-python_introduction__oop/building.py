# Objective: Let's make a city in code!
# TODO: Make all of the buildings that comprise a town
# # # - Homes
# # # - Apartments
# # # - Restaurants
# # # - Retail Stores
# # # - Mall


class Building(object):
    def __init__(self, floors, doors, address, walls=4):
        self.walls = walls
        self.floors = floors
        self.doors = doors
        self.address = address
        self.open = False

    def paintWalls(self, color):
        self.color = color
        return self

    def openDoors(self):
        self.open = not self.open
        return self

    def __str__(self):
        return "{}, {}, {}, {} ".format(self.walls,self.floors , self.doors, self.address)

class Home(Building):
    def __init__(self, floors, doors, address, bed, walls=4):
        super(Home, self).__init__(floors, doors, address, walls)
        self.bed = bed

    def goToBed(self):
        return self

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {} ".format(self.walls,self.floors , self.doors, self.address, self.bed, self.open, self.color)
        

home = Home(2, 2, 4000, 5, 2)
home2 = Home(2, 2, 32, 5, 1)

home2.paintWalls('white')

print home2
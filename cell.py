import random as rd

class MazeCell():
    def __init__(self):
        self.directions = [True, True, True, True]  #is direction taken
        self.toCheck = True
        self.wasVisited = False

    def __str__(self):
        return str(self.directions.count(True))
        #if self.wasVisited: return '⊡'
        #return '∎'

    def __repr__(self):
        return str(self.directions.count(True))
        #if self.wasVisited: return '⊡'
        #return '∎'

    def isDirGood(self, dir:int):
        if self.directions[dir]:
            return True
        return False

    def setAllDir(self, up:bool, down:bool, left:bool, right: bool):
        self.directions = [up, down, left, right]
        self.checkAvailability()

    def setOneDir(self, direction:int, value:bool):
        self.directions[direction] = value

    def pickDirection(self):
        if not self.toCheck:
            return -1
        if not self.checkAvailability():
            return -2
        indices = list(range(4))
        while len(indices) > 0:
            dir = rd.choice(indices)
            if self.directions[dir]:
                self.directions[dir] = False
                return dir
            else:
                indices.remove(dir)
        
        # Getting here means checking availability went wrong. Should not ever get here really
        self.toCheck = False
        return -3

    def checkAvailability(self):
        for dir in self.directions:
            if dir == True:
                self.toCheck = True
                return True
        # If gets here then no direction was available
        self.toCheck = False
        return False

if __name__ == '__main__': # if run from file itself
    print('Inside cell.py')
    c1 = MazeCell()
    c1.setAllDir(False, True, True, False)
    print(c1.pickDirection())
else: # if run from exterior
    print('Importing cell.py')
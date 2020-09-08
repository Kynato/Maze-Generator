if __name__ == '__main__':
    print('Inside cell.py')
else:
    print('Improrting cell.py')

class MazeCell():
    def __init__(self):
        self.directions = [True, True, True, True]  #is direction taken
        self.toCheck = True

    def __init__(self, up:bool, down:bool, left:bool, right:bool):
        self.directions = [up, down, left, right]

    def pickDirection(self):
        if not self.toCheck:
            return -1
        if not self.availability():
            return -1
        
        

    def availability(self):
        for dir in self.directions:
            if self.directions[dir]:
                return True
        # If gets here then no dir was available
        self.toCheck = False
        return False

from cell import *

def createTable(rows:int, cols:int):
    output = []
    for row in range(rows):
        newRow = []
        for col in range(cols):
            newRow.append(MazeCell())
        output.append(newRow)
    
    return output

def coordsPlusDir(oldCoords, dir:int):
    if dir < 0 or dir > 3:
        print('Error: Direction was wrong')
        return [-1, -1]
    if dir == 0:
        return [oldCoords[0], oldCoords[1] - 1]
    if dir == 1:
        return [oldCoords[0], oldCoords[1] + 1]
    if dir == 2:
        return [oldCoords[0] - 1, oldCoords[1]]
    if dir == 3: 
        return [oldCoords[0] + 1, oldCoords[1]]
        

class Maze:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.table = createTable(width, height)
        self.limitByWalls()
        self.labirynth = []
        self.generateLabirynth()


    def __repr__(self):
        output = ''
        for row in range(self.height):
            newRow = ''
            for col in range(self.width):
                newRow += str(self.table[row][col]) + ' '
            output += newRow + '\n'
        
        return output

    def limitByWalls(self):
        for col in range(self.width):
            self.table[0][col].setOneDir(0, False)
            self.table[self.height-1][col].setOneDir(1, False)
        for row in range(self.height):
            self.table[row][0].setOneDir(2, False)
            self.table[row][self.width-1].setOneDir(3, False)

    def generateLabirynth(self):
        output = []
        for row in range(self.height):
            newRow = []
            for col in range(self.width):
                newRow.append(-1)
            output.append(newRow)
        
        self.labirynth = output
        coords = [0,0]
        # 0-up 1-down 2-left 3-right
        while True:
            chosenDir = self.table[coords[0]][coords[1]].pickDirection()
            self.table[coords[0]][coords[1]].setOneDir(chosenDir, False)
            self.labirynth[coords[0]][coords[1]] = chosenDir
            coords = coordsPlusDir(coords, chosenDir)
            self.printLabirynth()
            input()

    def printLabirynth(self):
        
        output = '-------------------\n'
        for row in range(self.height):
            newRow = ''
            for col in range(self.width):
                dir = self.labirynth[row][col]
                if dir == 0:
                    newRow += '↑ '
                if dir == 1:
                    newRow += '↓ '
                if dir == 2:
                    newRow += '← '
                if dir == 3: 
                    newRow += '→ '
            output += newRow + '\n'
        
        print(output + '-------------------\n')



if __name__ == '__main__': # if run from file itself
    print('Inside maze.py')
    m1 = Maze(10, 10)
    print(m1)
    m1.printLabirynth()
    
else: # if run from exterior
    print('Importing maze.py')
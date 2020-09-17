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

def opositeDir(dir:int):
    if dir == 0:
        return 1
    if dir == 1:
        return 0
    if dir == 2:
        return 3
    if dir == 3:
        return 2

    return -1
        

class Maze:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.table = createTable(width, height)
        self.coordHistory = []
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
        self.coordHistory.append([0,0])
        
        prevDir = chosenDir = self.table[self.coordHistory[-1][1]][self.coordHistory[-1][0]].pickDirection()
                #[col, row]
        # 0-up 1-down 2-left 3-right
        while True:
            if chosenDir < 0:
                print('Something went wrong')
                
            # mark direction as used
            self.table[self.coordHistory[-1][1]][self.coordHistory[-1][0]].setOneDir(chosenDir, False)
            # mark cell as visited
            self.table[self.coordHistory[-1][1]][self.coordHistory[-1][0]].wasVisited = True
            # mark chosen direction in labirynth matrix
            self.labirynth[self.coordHistory[-1][1]][self.coordHistory[-1][0]] = chosenDir
            # mark direction we came from as used
            self.table[self.coordHistory[-1][1]][self.coordHistory[-1][0]].setOneDir(prevDir, False)
            # set coords to new position
            self.coordHistory.append(coordsPlusDir(self.coordHistory[-1], chosenDir))

            # remember old direction
            prevDir = chosenDir

            # pick new direction
            indices = list(range(4))
            while len(indices) > 0:
                chosenDir = rd.choice(indices)
                print('dir: ' + str(chosenDir))
                if self.table[self.coordHistory[-1][1]][self.coordHistory[-1][0]].isDirGood(chosenDir):
                    tmp = coordsPlusDir(self.coordHistory[-1], chosenDir)
                    if self.labirynth[tmp[1]][tmp[0]] == -1:
                        #self.table[self.coordHistory[-1][1]][self.coordHistory[-1][0]].setOneDir(chosenDir, False)
                        break
                indices.remove(chosenDir)
            if len(indices) == 0:
                print('No available cells. Need to backtrack.')
                self.labirynth[self.coordHistory[-1][1]][self.coordHistory[-1][0]] = 4
                self.table[self.coordHistory[-1][1]][self.coordHistory[-1][0]].wasVisited = True
                while not self.isNewBreakpoint(self.coordHistory[-1][1], self.coordHistory[-1][0]):
                    print('Popped once')
                    self.coordHistory.pop()
                indices = list(range(4))
                while len(indices) > 0:
                    chosenDir = rd.choice(indices)
                    #chosenDir = self.table[coords[1]][coords[0]].pickDirection()
                    print('dir: ' + str(chosenDir))
                    if self.table[self.coordHistory[-1][1]][self.coordHistory[-1][0]].isDirGood(chosenDir):
                        tmp = coordsPlusDir(self.coordHistory[-1], chosenDir)
                        if self.labirynth[tmp[1]][tmp[0]] == -1:
                            self.table[self.coordHistory[-1][1]][self.coordHistory[-1][0]].setOneDir(chosenDir, False)
                            break
                    indices.remove(chosenDir)
            
            self.printLabirynth()
            input()

    def printLabirynth(self):
        
        output = '-------------------\n'
        for row in range(self.height):
            newRow = ''
            for col in range(self.width):
                dir = self.labirynth[row][col]
                if dir == -1:
                    newRow += '  '
                if dir == 0:
                    newRow += '↑ '
                if dir == 1:
                    newRow += '↓ '
                if dir == 2:
                    newRow += '← '
                if dir == 3: 
                    newRow += '→ '
                if dir == 4: 
                    newRow += '# '
            output += newRow + '\n'
        
        print(output + '-------------------\n')

    def isNewBreakpoint(self, row:int, col:int):
        if not self.table[row+1][col].wasVisited and row+1 < self.height:
            return True
        if not self.table[row-1][col].wasVisited and row > 0:
            return True
        if not self.table[row][col+1].wasVisited and col+1 < self.width:
            return True
        if not self.table[row][col-1].wasVisited and col > 0:
            return True
        return False




if __name__ == '__main__': # if run from file itself
    print('Inside maze.py')
    m1 = Maze(10, 10)
    print(m1)
    m1.printLabirynth()
    
else: # if run from exterior
    print('Importing maze.py')
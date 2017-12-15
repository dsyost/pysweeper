import sys
from random import randint

class sweeper():
    def __init__(self, height, width, mine_number):
        self.score = 0
        self.comment = "explore or mark?"
        self.height = height-1
        self.width = width-1
        self.mine_number = mine_number
        self.grid_hidden = [["#" for _ in range(width)] for _ in range(height)]
        self.grid = [["0" for _ in range(width)] for _ in range(height)]
        for i in range(mine_number):
            x = 0
            while not self.addMine(randint(0,self.height), randint(0,self.width)) and x < height*width: x+=1

    def addMine(self, height, width):
        if self.grid[height][width] == "*":
            return False
        else:
            self.grid[height][width] = "*"
            for [i,j] in self.getNeighbors(height,width):
                if self.grid[i][j] != "*":
                    self.grid[i][j] = str(int(self.grid[i][j]) + 1)
            return True

    def getNeighbors(self, height, width):
        neighbors = []
        for i in range(height-1,height+2):
            for j in range(width-1, width+2):
                if i <= self.height and j <= self.width and i >=0 and j >=0:
                    neighbors.append([i,j])
        neighbors.remove([height,width])  
        return neighbors

    def explore(self, height, width):
        if self.grid[height-1][width-1] == "0":
            self.clearZeros(height-1, width-1)
        else:
            self.grid_hidden[height-1][width-1] = self.grid[height-1][width-1]
        if self.grid[height-1][width-1] == "*":
            self.comment="game over"
            self.grid_hidden = self.grid
            self.displayGrid()
            sys.exit()

    def clearZeros(self, height, width):
        self.grid_hidden[height][width] = self.grid[height][width]
        neighbors = self.getNeighbors(height, width)
        for [i,j] in neighbors:
            if self.grid_hidden[i][j] == "#":
                if self.grid[i][j] != "0":
                    self.grid_hidden[i][j] = self.grid[i][j]
                else:
                    self.grid_hidden[i][j] = self.grid[i][j]
                    self.clearZeros(i,j)
                    
    def mark(self, height, width):
        self.grid_hidden[height-1][width-1] = "?"
        if self.grid[height-1][width-1] == "*":
            self.score += 1
            if self.score == self.mine_number:
                self.comment="you win!!"
                self.grid_hidden = self.grid
                self.displayGrid()
                sys.exit()
        
    def displayGrid(self):
        for h in range(len(self.grid_hidden)):
            for w in self.grid_hidden[h]:
                print(w,end="")
            print("")
        print(self.comment)
        self.comment="explore or mark?"

    def additionalComment(self, comment):
        self.comment = comment

if __name__ == "__main__":
    height = int(input("what height?\n> "))
    width = int(input("what width?\n> "))
    mine_number = int(input("how many mines?\n> "))
    s = sweeper(height,width,mine_number)
    s.additionalComment("you can either explore or mark in the grid by first putting\nthe command followed by height and width\nie. mark 3 2 keep in mind the upper left hand corrner is 1 1")
    while True:
        s.displayGrid()
        command = input("> ")
        command_split = command.split()
        if len(command_split) == 3:
            if command_split[0] == "explore" or command_split[0] == "e" or command_split[0] == ".":
                s.explore(int(command_split[1]), int(command_split[2]))
            elif command_split[0] == "mark" or command_split[0] ==  "m" or command_split[0] == "?":
                s.mark(int(command_split[1]), int(command_split[2]))
            else:
                s.additionalComment("please enter a valid command")
        else:
            s.additionalComment("please enter a valid command followed by a height and width")

"""

    All the tiles on the board will be a power of 2 like 2, 4, 8, 16, 32, 64, 128,...., 2048.
    There are 4 possible moves: left, right, top, bottom.
    On each move, all the tiles slide in the direction of the move until they are stopped by another tile or an edge.
    A random tile will be inserted at a random empty spot on the board after every move.
    If after sliding, two tiles with the same values collide in the direction of the slide then they will merge into a tile with the value being the total of the collided tiles.
    Example: Two tiles numbered 4 will merge to form a tile numbered 8. The merging will happen in the direction of the movement.
    A merged tile will not merge with another tile in the same move.
    In case 3 consecutive tiles have the same number then the farther tile in the direction of the move will merge. In case all four tiles have the same number then the first two and last two will merge.
    The game is won if the board has a tile numbered 2048.
    The game is lost if there are no possible moves left: No empty tile and no adjacent tiles with the same number.

"""



import random
class Box:
    
    def __init__(self):
        self.box = [["_"]*4 for _ in range(4)]
        self.max = 2
        self.desired_max = 2048
        self.win = False
        self.game_over = False
        self.place_random()
        
    
    def place_random(self):
        number = random.choice([2,4])
        empty = [(i,j) for i in range(4) for (j) in range(4) if self.box[i][j]=="_"]
        x,y = random.choice(empty)
        self.box[x][y] = number
        return number
    
    def print_box(self):
        for i in range(4):
            print("  ".join([str(x) for x in self.box[i]]))
        
    def move_left(self):
        self.move_horizontally(1)
        self.place_random()
        
    def move_right(self):
        self.move_horizontally(-1)
        self.place_random()

    def move_up(self):
        self.move_vertically(1)
        self.place_random()
        
    def move_down(self):
        self.move_vertically(-1)
        self.place_random()

    def move_vertically(self,stepx):
        startx,endx = (0,4) if stepx==1 else (3,-1)
        starty,endy,stepy = 0,4,1
        for j in range(starty,endy,stepy):
            last = None
            lastx = None
            for i in range(startx,endx,stepx):
                if self.box[i][j]!="_":
                    if last and last == self.box[i][j]:
                        self.box[lastx][j] *= 2
                        self.max = max(self.max,self.box[lastx][j])
                        self.box[i][j]="_"
                        last,lastx = None,None
                    else:
                        last = self.box[i][j]
                        lastx = i
        for j in range(starty,endy,stepy):
            k = startx
            for i in range(startx,endx,stepx):
                if self.box[i][j]!="_":
                    self.box[i][j],self.box[k][j] = self.box[k][j],self.box[i][j]
                    k+=stepx
    def move_horizontally(self,stepy):
        startx,endx,stepx = 0,4,1
        starty,endy = (0,4) if stepy==1 else (3,-1)
        for i in range(startx,endx,stepx):
            last = None
            lasty = None
            for j in range(starty,endy,stepy):
                if self.box[i][j]!="_":
                    if last and last == self.box[i][j]:
                        self.box[i][lasty] *= 2
                        self.max = max(self.max,self.box[i][lasty])
                        self.box[i][j]="_"
                        last,lasty = None,None
                    else:
                        last = self.box[i][j]
                        lasty = j
        for i in range(startx,endx,stepx):
            k = starty
            for j in range(starty,endy,stepy):
                if self.box[i][j]!="_":
                    self.box[i][j],self.box[i][k] = self.box[i][k],self.box[i][j]
                    k+=stepy
                    
    def update_current_state(self):
        mat = self.box
        if self.max==self.desired_max:
            self.win = True
            return
        for i in range(4):
            for j in range(4):
                if(mat[i][j]== 0):
                    return
        for i in range(3):
            for j in range(3):
                if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
                    return
    
        for j in range(3):
            if(mat[3][j]== mat[3][j + 1]):
                return
 
        for i in range(3):
            if(mat[i][3]== mat[i + 1][3]):
                return
    
        # else we have lost the game
        self.game_over = True
        return
                

b = Box() 

while True:
        
    b.print_box()
    inp = input("Press\nW: Upward\nA: Leftward\nS: Downward\nD: Rightward\nQ: Quit \n")
    if inp=="q":
        break
    elif inp=='w':
        b.move_up()
    elif inp=='s':
        b.move_down()
    elif inp=='a':
        b.move_left()
    elif inp=='d':
        b.move_right()
    b.update_current_state()
    if b.win or b.game_over:
        b.print_box()
        print("Game Over" if b.game_over else "WIN")
        break

        
        
        
        
from constants import DEFAULT_BOARD_SIZE
class Board:
    def __init__(self,size=DEFAULT_BOARD_SIZE):
        self.size = size
        self.jumps = {}
    def add_ladder_or_snake(self,start,end):
        self.jumps[start] = end
    
    def get_final_position(self,number):
        return self.jumps.get(number,number)
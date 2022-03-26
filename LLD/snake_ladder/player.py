
from constants import DEFAULT_START_POSITION
class Player:
    AUTO_INCREMENT_ID = 0
    def __init__(self,name,start_position=DEFAULT_START_POSITION):
        self.id = Player.AUTO_INCREMENT_ID
        Player.AUTO_INCREMENT_ID+=1
        self.name = name
        self.cur_position = start_position
        self.rank_status = None
    def update_rank(self,rank):
        self.rank_status = rank
import random
from constants import DEFAULT_START_POSITION,DICE_CHOICES
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
    def roll_dice(self,dices):
        input("Hey {}! Press any key to roll dice(s). ".format(self.name))
        count = 0
        count_per_dice = []
        for _ in range(dices):
            rand = random.choice(DICE_CHOICES)
            count_per_dice.append(rand)
            count+=rand
        return count,count_per_dice
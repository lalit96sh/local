
import collections
import random
from board import Board
from constants import DEFAULT_DICE_NUMBER,DEFAULT_PLAYER_COUNT,DICE_CHOICES,DEFAULT_LADDERS,DEFAULT_SNAKE
from player import Player
class Game:
    def __init__(self,dices=DEFAULT_DICE_NUMBER,players=DEFAULT_PLAYER_COUNT):
        self.dices = dices
        self.players=[]
        self.board = Board()
        for _ in range(players):
            self.add_player()
        self.active_players_count = players
        self.winners = []
        self.turn_counter = -1
    def add_player(self):
        name = input("Name of Player:    ")
        self.players.append(Player(name))
        
    def roll_dice(self):
        count = 0
        count_per_dice = []
        for _ in range(self.dices):
            rand = random.choice(DICE_CHOICES)
            count_per_dice.append(rand)
            count+=rand
        return count,count_per_dice

    def check_and_update_player_status(self,player):
        if player.cur_position==self.board.size:
            import pdb;pdb.set_trace()
            self.winners.append(player)
            player.update_rank(len(self.winners))
            self.active_players_count-=1
            self.turn_counter-=1
            self.players.remove(player)
    
    def move_player(self,player,step_count):
        if (player.cur_position + step_count) > self.board.size:
            return
        
        player.cur_position = self.board.get_final_position(player.cur_position + step_count)
        self.check_and_update_player_status(player)
        
    def get_turn_player(self):
        self.turn_counter = (self.turn_counter+1)%self.active_players_count
        return self.players[self.turn_counter]
    
    def game_over(self):
        return len(self.players)<2
    
    def play_game(self):
        while not self.game_over():
            self.print_game()
            player = self.get_turn_player()
            input("Hey {}! Press any key to roll dice(s). ".format(player.name))
            count,count_presentation = self.roll_dice()
            print("Dice result: {}".format(count_presentation))
            self.move_player(player,count)
        self.print_result()
        print("Game Over!")
        
    def print_game(self):
        player_map = collections.defaultdict(list)
        num_map = {}
        for jump in [DEFAULT_LADDERS,DEFAULT_SNAKE]:
            for start,end in jump:
                num_map[start]="+"
                num_map[end] = "-"
        for p in self.players:
            player_map[p.cur_position].append(p.name)
            
        n = self.board.size
        
        while n>0:
            st = []
            for _ in range(10):
                st.append("{}{} {}".format(n,num_map.get(n,""),player_map[n] if player_map[n] else ""))
                n-=1
            print("\t".join(st))
            
    def print_result(self):
        
        for i,_ in enumerate(self.winners):
            print("Rank: {}\t{}".format(i+1,_.name))
        print("Loser\t{}".format(self.players[0].name))
        
            
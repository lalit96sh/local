
from game import Game
from constants import DEFAULT_LADDERS,DEFAULT_SNAKE
g = Game()
for default_jump in [DEFAULT_LADDERS,DEFAULT_SNAKE]:
    for start,end in default_jump:
        g.board.add_ladder_or_snake(start,end)
g.play_game()
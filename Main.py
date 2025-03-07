from Assets.Cards import Cards
from Assets.Player import Player
import json

cards = Cards()

cards.shuffle_cards()
board_state = cards.set_board()
print(json.dumps(board_state, indent=4))

player = Player(cards, board_state)
player.solitaire_player_SRA()
# player.solitaire_player_MbRA()

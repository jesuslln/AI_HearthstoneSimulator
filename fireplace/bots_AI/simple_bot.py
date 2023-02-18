from .bot_agent import bot_agent
from .utils import random_heropower, play_max_mana_cards, random_attacks
import random


class simple_bot(bot_agent):

    def play_next_turn(self, game, player):

        # use hero power randomly
        random_heropower(player)

        # iterate over our hand and play whatever is playable
        play_max_mana_cards(player)

        # Randomly attack with whatever can attack
        random_attacks(player)

#!/usr/bin/env python
import sys

from fireplace import cards
from fireplace.exceptions import GameOver
from fireplace.utils import play_full_game


sys.path.append("..")


def test_full_game(stats):
	try:
		play_full_game()
	except GameOver as winner:
		print("Game completed normally. " + str(winner) +" Won")
		if(str(winner) == "Player1"):
			stats[0] += 1
		elif (str(winner) == "Player2"):
			stats[1] += 1
		else:
			stats[2] += 1
		print(stats)
	# except Exception:
	# 	print("Game error")
		#play_full_game()
		


def main():
	statistics = [0,0,0]
	cards.db.initialize()
	if len(sys.argv) > 1:
		numgames = sys.argv[1]
		if not numgames.isdigit():
			sys.stderr.write("Usage: %s [NUMGAMES]\n" % (sys.argv[0]))
			exit(1)
		for i in range(int(numgames)):
			test_full_game(statistics)
		print("Player 1 Winrate is: " + str(statistics[0]/(statistics[0] + statistics[1]) ))	
		
	else:
		test_full_game(statistics)


if __name__ == "__main__":
	main()

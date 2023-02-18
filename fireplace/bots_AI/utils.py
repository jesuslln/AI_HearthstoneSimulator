import random



## Play Hand Cards

def random_handcards(player):
    for card in player.hand:
        if card.is_playable() and random.random() < 0.5:
            target = None
            if card.must_choose_one:
                card = random.choice(card.choose_cards)
            if card.requires_target():
                target = random.choice(card.targets)
            print("Playing %r on %r" % (card, target))
            card.play(target=target)

            if player.choice:
                choice = random.choice(player.choice.cards)
                print("Choosing card %r" % (choice))
                player.choice.choose(choice)

def play_max_mana_cards(player):
    hand_sorted = sort_hand_max_mana(player)
    for card in hand_sorted:
        if card.is_playable():
            target = None
            if card.must_choose_one:
                card = random.choice(card.choose_cards)
                if card.requires_target():
                    target = random.choice(card.targets)
                print("Playing %r on %r" % (card, target))
                card.play(target=target)

            if player.choice:
                choice = random.choice(player.choice.cards)
                print("Choosing card %r" % (choice))
                player.choice.choose(choice)


## Other hand functions
def sort_hand_max_mana(player):       
    cost_card_dict = create_cost_dict(player.hand)
    cost_card_sorted = sorted(cost_card_dict, reverse=True)
    hand_sorted = get_cards_dict(cost_card_sorted, cost_card_dict)
    return hand_sorted
        

# This function creates a dict with cost as keys and cards as values
def create_cost_dict(hand):
	hand_cost = {}

	for card in hand:
		if card.cost in hand_cost:
			hand_cost[card.cost].append(card)
		else:
			hand_cost[card.cost] = []
			hand_cost[card.cost].append(card)

	return hand_cost


def get_cards_dict(keys, dict):
	hand_sorted = []
	for key in keys:
		cards = dict[key]

		if type(cards) == list:
			for c in cards:
				hand_sorted.append(c)
		else:
			hand_sorted.append(cards)

	return hand_sorted


## Attack Functions

def random_attacks(player):
    for character in player.characters:
        if character.can_attack():
            character.attack(random.choice(character.targets))

## Hero Power functions

def random_heropower(player):
    heropower = player.hero.power
    if heropower.is_usable() and random.random() < 0.1:
            if heropower.requires_target():
                heropower.use(target=random.choice(heropower.targets))
            else:
                heropower.use()



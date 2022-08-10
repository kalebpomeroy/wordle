from wordle.play import Game
from pprint import pprint
from wordle.words import all_words


def do_a_bunch(starting_guess, limit=1000):
    results = {"L": 0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0}
    for x in range(0, limit):
        game = Game()
        if game.play(starting_guess):
            results["{}".format(game.turns)] += 1
        else:
            results["L"] += 1

    print(starting_guess, results)


for guess in ['clasp', 'slate', 'alert', 'ocean']:
    do_a_bunch(guess)

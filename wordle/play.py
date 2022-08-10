from pprint import pprint
from random import choice
from copy import copy
from wordle.words import all_words
from wordle import score


class Game():
    def __init__(self, answer=None):
        self.answer = answer or choice(all_words)
        self.guess_letters = [[], [], [], [], []]
        self.options = []
        self.guesses = []
        self.final_answer = [None, None, None, None, None]
        self.turns = 1
        self.valid_choices = copy(all_words)

    def play(self, first_guess):
        self.guesses.append(first_guess)
        while not self.check_answer(self.guesses[self.turns - 1]):
            if self.turns >=6:
                return False

            self.make_guess()
            self.turns += 1

        return True

    def check_answer(self, guess):
        # If it's right it's right
        if guess == self.answer:
            return True

        # If it's not right, lets save some information about each guess letter
        for i, letter in enumerate(guess):

            # If it's not in the letter at all, fill every position with the
            # letter so we know it's not a valid guess for that position
            # aka grey letters
            if self.answer.find(letter) < 0:
                [self.guess_letters[p].append(letter) for p in range(0, 5)]

            # If the letter in the answer is the same, we know it's part of the
            # right answer. aka green letters
            elif self.answer[i] == letter:
                self.final_answer[i] = letter

            # If it's there, but not in the right position, save it as an option
            # but don't reguess that position aka yellow letters
            else:
                self.guess_letters[i].append(letter)
                self.options.append(letter)

        # print "    guess {}: {}".format(self.turns+1, guess)
        return False

    def is_possible_word(self, candidate_word):
        # For each letter in the potential word, see if we've already guessed
        # that letter in that position
        for i, letter in enumerate(candidate_word):
            if letter in self.guess_letters[i]:
                return False

        # For each letter in our "yellow" list, make sure our guess includes it
        for letter in self.options:
            if letter not in candidate_word:
                return False

        # For each letter in our "green" list, make sure our guess includes it
        for i, letter in enumerate(self.final_answer):
            if letter and candidate_word[i] != letter:
                return False

        return candidate_word

    def make_guess(self):
        # Generate a list of every valid guess based on what we know
        self.valid_choices = [x for x in [self.is_possible_word(w) for w in self.valid_choices] if x]

        # Out of those, which ever word has the highest positional score, use that
        guess = score.get_highest_score_word(self.valid_choices, use_positional=True, skip_repeated_chars=False)
        self.guesses.append(guess)

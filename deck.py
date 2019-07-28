import uuid
import numpy

POSSIBLE_SUITES = ("clubs", "diamonds", "hearts", "spades")
POSSIBLE_RANKS = ("two", "three", "four", "five", "six", "seven", "eight",
                  "nine", "ten", "jack", "queen", "king", "ace")

VALUES = {
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": 10,
    "queen": 10,
    "king": 10,
    "ace": 11
}


class Deck():

    class Card():
        def __init__(self, suite, rank):
            self.suite = suite
            self.rank = rank
            self.uuid = uuid.uuid4()
            self.value = VALUES[self.rank]
            self.friendly_name = self.rank.capitalize() + ' of ' + self.suite

    def shuffle(self):
        self.temp_dict = {}
        for i in self.cards:
            num = numpy.floor(numpy.random.random(1)[0] * self.deck_count * 52)
            while num in self.temp_dict.keys():
                if self.debug:
                    print(num, num in self.temp_dict.keys())
                    print(self.temp_dict.keys())
                num = numpy.floor(numpy.random.random(1)[0] *
                                  self.deck_count * 52)
            self.temp_dict[num] = self.cards[i]
        self.cards = self.temp_dict
        del self.temp_dict

    def __init__(self, deck_count=1, shuffle=True, debug=False):
        self.deck_count = deck_count
        self.debug = debug
        self.cards = {}
        self.do_shuffle = shuffle

        for suite in POSSIBLE_SUITES:
            for rank in POSSIBLE_RANKS:
                for _ in range(0, self.deck_count):
                    self.cards[len(self.cards)] = self.Card(suite, rank)

        if self.do_shuffle:
            self.shuffle()

        del self.do_shuffle

    def _print(self):
        for i in self.cards:
            print(self.cards[i].uuid, self.cards[i].friendly_name)

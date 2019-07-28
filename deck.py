import uuid
import numpy

POSSIBLE_SUITES = ("clubs", "diamonds", "hearts", "spades")
POSSIBLE_VALUES = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "jack",
                   "queen", "king", "ace")


class Deck():

    class Card():
        def __init__(self, suite, value):
            self.suite, self.value, self.uuid = suite, value, uuid.uuid4()

        def friendly_name(self):
            return self.value + ' of ' + self.suite

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
            for value in POSSIBLE_VALUES:
                for _ in range(0, self.deck_count):
                    self.cards[len(self.cards)] = self.Card(suite, value)

        if self.do_shuffle:
            self.shuffle()

        del self.do_shuffle

    def _print(self):
        for i in self.cards:
            print(self.cards[i].uuid, self.cards[i].friendly_name())

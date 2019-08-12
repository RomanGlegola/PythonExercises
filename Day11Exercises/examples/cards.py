import random
import matplotlib.pyplot as mpplot
import matplotlib.image as mpimg

class Card():
    FIGURES = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    COLORS = ["hearts", "clubs", "diamonds", "spades"]

    def __init__(self, figure, color):
        self.__figure = figure
        self.__color = color

    def __str__(self):
        return f"{self.__figure} of {self.__color}"


class CardDeck:

    def __init__(self):
        self.__deck = []
        self.__current_card_index = 0

        for figure in Card.FIGURES:
            for color in Card.COLORS:
                self.__deck.append(Card(figure, color))

    def suffle(self):
        pass
        # random().shuffle(self.__deck[random])

    # def give_card(self):
    #     card_to_return = self.__deck[self.__current_card_index]
    #     self.__current_card_index += 1

    def cards_count(self):
        return len(self.__deck)

    def show_all_the_cards(self):

        # for card in self.__deck:
        #     string_to_return = ""
        #     string_to_return += str(card)+"\n"
        #
        # return string_to_return
        return "\n".join({str(x) for x in self.__deck})


# print(CardDeck().cards_count())



print(CardDeck().show_all_the_cards())
number_of_cards = 5
card_hand = []

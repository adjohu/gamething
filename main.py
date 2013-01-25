from event import EventManager
from tick import TickController
from keyboard import KeyboardController
from player import Player
from view import View
from game import Game


def main():

    evManager = EventManager()

    tick = TickController(evManager)
    view = View(evManager)
    game = Game(evManager)
    keyboard = KeyboardController(evManager)

    tick.Run()

if __name__ == '__main__':
    main()

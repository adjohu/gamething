from event import EventManager
from tick import TickController
from keyboard import KeyboardController
from view import View
from game import Game
from world import World


def main():

    evManager = EventManager()

    tick = TickController(evManager)
    view = View(evManager)
    game = Game(evManager)
    world = World(evManager)
    keyboard = KeyboardController(evManager)

    tick.Run()

if __name__ == '__main__':
    main()

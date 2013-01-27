from event_manager import EventManager
from tick import TickController
from keyboard import KeyboardController
from view import View
from game import Game
from world import World


def main():

    evManager = EventManager()

    tick = TickController(evManager)
    world = World(evManager)
    view = View(evManager)
    game = Game(evManager)
    keyboard = KeyboardController(evManager)

    tick.Run()

if __name__ == '__main__':
    main()

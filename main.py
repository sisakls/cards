#!/usr/bin/env python3

from game import *

def main() -> None:
    """Entry point function."""

    game_data = DataLoader("test.json")
    test = game(game_data.dungeon, game_data.loot, game_data.town)

    test.run_setup()
    end = False
    while end is False:
        test.run_turn()

if __name__ == "__main__":    
    main()
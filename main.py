#!/usr/bin/env python3
"""Main entry-point module. This script is used to start the program."""

from game import *


def main() -> None:
    """Entry point function."""
    decklist_1 = 2*["amoba_nagy"] + 5*["amoba_orias"] + 4*["kardfogu_szunyog"] + 1*["kobold_felderito"]
    #decklist_2 = 3*["kobold_bandita"] + 4*["kobold_vadasz"] + 1*["kobold_felderito"] + 2*["eltorlaszolt_jarat"]
    dungeon_1 = deck(decklist_1, boss="eltorlaszolt_jarat")
    test = game(dungeon_1, deck(3*["kobold_bandita"] + 4*["kobold_vadasz"]), deck([]))

    test.run_setup()
    end = False
    while end is False:
        test.run_turn()


if __name__ == "__main__":
    main()
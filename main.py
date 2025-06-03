#!/usr/bin/env python3
"""Main entry-point module. This script is used to start the program."""

from game import *


def main() -> None:
    """Entry point function."""
    decklist_1 = 2*["monster/amoba_nagy"] + 5*["monster/amoba_orias"] + 4*["monster/kardfogu_szunyog"] + 1*["monster/kobold_felderito"]
    #decklist_2 = 3*["monster/kobold_bandita"] + 4*["monster/kobold_vadasz"] + 1*["monster/kobold_felderito"] + 2*["monster/eltorlaszolt_jarat"]
    dungeon_1 = deck(decklist_1, boss="monster/eltorlaszolt_jarat")
    test = game(dungeon_1, deck(3*["monster/kobold_bandita"] + 4*["monster/kobold_vadasz"]), deck([]))

    test.run_setup()
    end = False
    while end is False:
        test.run_turn()


if __name__ == "__main__":
    main()
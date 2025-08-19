#!/usr/bin/env python3

from game import *
import json

class DataLoader:
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.rawdata = json.load(f)
        self.dungeon = self.build_deck("dngn_list_1")
        self.dungeon.add(self.build_deck("dngn_list_2"))
        self.loot = self.build_deck("loot_list")
        self.town = self.build_deck("town_list")

    def build_deck(self, deck_name):
        decklist = []
        for card_name, count in self.rawdata[deck_name].items():
            decklist = decklist + count*[card_name]
        return deck(decklist)


def main() -> None:
    """Entry point function.""" #TODO: fix naming

    game_data = DataLoader("test.json")
    test = game(game_data.dungeon, game_data.loot, game_data.town)

    test.run_setup()
    end = False
    while end is False:
        test.run_turn()


if __name__ == "__main__":    
    main()
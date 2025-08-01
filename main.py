#!/usr/bin/env python3

from game import *


def main() -> None:
    """Entry point function.""" #TODO: move this mess to a config file, fix naming
    dngnlist_1 = 2*["monster/amoba_nagy"] + 5*["monster/amoba_orias"] + 4*["monster/kardfogu_szunyog"] + 1*["monster/kobold_felderito"]
    dngnlist_2 = 3*["monster/kobold_bandita"] + 4*["monster/kobold_vadasz"] + 1*["monster/kobold_felderito"] + 2*["monster/eltorlaszolt_jarat"]
    dungeon = deck(dngnlist_1)
    dungeon.add(deck(dngnlist_2))

    lootlist = 2*["powerup/cha_up"] + 2*["powerup/mag_up"] + 2*["powerup/sth_up"] + 4*["powerup/vit_up"]
    loot = deck(lootlist)

    townlist_1 = ["item/armor/bearskin"] + ["item/armor/chain_mail"] + ["item/armor/leather_armor"] + ["item/armor/thief_cloak"] + ["item/armor/wizard_cloak"]
    townlist_2 = 4*["item/consumable/health_potion"] + 2*["item/consumable/scroll_of_fire"] + 2*["item/consumable/throwing_knife"]
    townlist_3 = ["item/weapon/baszottnehez_ko"] + ["item/weapon/foldrengeto"] + ["item/weapon/ij"] + ["item/weapon/parittya"] + ["item/weapon/vadaszkes"]
    town = deck(townlist_1)
    town.add(deck(townlist_2))
    town.add(deck(townlist_3), shuffle=True)

    test = game(dungeon, loot, town)

    test.run_setup()
    end = False
    while end is False:
        test.run_turn()


if __name__ == "__main__":
    main()
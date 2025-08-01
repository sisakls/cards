import random

class card:
    def __init__(self, path, mod=None):
        self.path = "card_files/" + path + ".txt"
        self.type = path.split('/')[0]
        self.subtype = None
        if self.type == "item":
            self.subtype == path.split('/')[1]
        with open(self.path, encoding="utf-8") as f:
            self.graphics = [line[:-1] for line in f]
            self.num_mods = len(self.graphics) / 7
            if mod is None:
                self.mod = random.randint(0, self.num_mods-1)
            else:
                self.mod = mod
            self.idx = self.mod * 7
            
    def show(self):
        for line in self.graphics[self.idx:self.idx+7]: print(line)


class deck:
    def __init__(self, decklist, shuffle=True, boss=None):
        self.cards = [card(monster) for monster in decklist]
        if shuffle:
            random.shuffle(self.cards)
        if boss is not None:
            self.cards.append(card(boss))

    def add(self, target, shuffle=False):
        self.cards = self.cards + target.cards
        if shuffle: 
            random.shuffle(self.cards)

    def move(self, target, num=1, idx=0):
        tmp = self.cards[idx:idx+num]
        del self.cards[idx:idx+num]
        target.cards = tmp + target.cards

    def size(self):
        return len(self.cards)

    def show(self):
        for card in self.cards: card.show()
        if self.size()==0: print("Ez a pakli üres!")


class game:
    def __init__(self, dungeon, loot, town):
        self.state = "inicializáció"
        self.dngn = dungeon
        self.dngn_bin = deck([])
        self.loot = loot
        self.loot_bin = deck([])
        self.town = town
        self.town_bin = deck([])
        self.hand = deck([])
        self.turn = 0

    def run_setup(self):
        self.state = "előkészület"
        self.num_players = self.get_int("Hány játékos játszik?")
        self.player_invs = {}
        for i in range(self.num_players):
            name = input("Írd be a(z) {}. játékos nevét!".format(i+1))
            self.player_invs[name] = deck([])
        print("A játék kezdődik.")

    def run_turn(self):
        self.turn += 1
        print("\no==========================( {}. KÖR )==========================o\n".format(self.turn))
        for name, items in self.player_invs.items():
            self.p = name
            self.state = "{} köre - hajnal".format(name)
            print("{} jön. Hátizsák:".format(name))
            items.show()
            
            destination = self.get_command("Mit szeretnél csinálni?", {"K":"kaland", "F":"falu", "?":"súgó"})
            if destination == "K": self.run_dngn()
            elif destination == "F": self.run_town()

    def run_dngn(self):
        self.state = "{} köre - kaland".format(self.p)
        num_draw = self.get_int("Hány lapot húzol a kazamatából?")
        self.dngn.move(self.hand, num_draw)
        print("Az alábbi lapokat húztad:")
        self.hand.show()
        self.move_sequence(self.hand, self.dngn_bin, "Melyik szörnyeket győzted le?")
        self.hand.move(self.dngn, self.hand.size())

        self.state = "{} köre - zsákmány".format(self.p)
        num_draw = self.get_int("Hány lapot húzol a zsákmányból?")
        self.loot.move(self.hand, num_draw)
        print("Az alábbi lapokat húztad:")
        self.hand.show()
        self.move_sequence(self.hand, self.loot_bin, "Melyik zsákmányt veszed el?")
        self.hand.move(self.loot, self.hand.size())

    def run_town(self):
        self.state = "{} köre - falu".format(self.p)
        num_draw = self.get_int("Hány lapot húzol a faluból?")
        self.town.move(self.hand, num_draw)
        print("Az alábbi lapokat húztad:")
        self.hand.show()
        self.move_sequence(self.hand, self.player_invs[self.p], "Melyik felszerelést vetted meg?")
        self.hand.move(self.town, self.hand.size())

    def move_sequence(self, source, target, prompt):
        while True:
            cmd = input(prompt)
            if cmd == "?":
                print("A játék \"{}\" fázisban van. Lehetséges parancsok:".format(self.state))
                print("{egész számok, 'V': 'végeztem', '?': súgó}")
            elif cmd == "V": 
                return
            else:
                try:
                    source.move(target, idx=int(cmd)-1)
                    print("A megmaradt lapok:")
                    source.show()
                except:
                    print("A \"{}\" parancs nem található.".format(cmd))

    def get_command(self, prompt, valid_inputs):
        while True:
            cmd = input(prompt)
            if cmd not in valid_inputs.keys():
                print("A \"{}\" parancs nem található.".format(cmd))
            elif cmd == "?":
                print("A játék \"{}\" fázisban van. Lehetséges parancsok:".format(self.state))
                print(valid_inputs)
            else: return cmd

    def get_int(self, prompt):
        while True:
            cmd = input(prompt)
            if cmd == "?":
                print("A játék \"{}\" fázisban van. Lehetséges parancsok:".format(self.state))
                print("{egész számok, '?': 'súgó'}")
            else:
                try: return int(cmd)
                except: print("A \"{}\" parancs nem található.".format(cmd))
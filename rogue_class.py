from player_class import Player
class Mergen(Player):

    def __init__(self, nameput):
        super().__init__(nameput, 450, 12, 4, 7, "Mergen")

    def skillOne(self):
        dmg = self.atk * 3 - 3
        print(self.name + " strikes 3x with reduced damage, doing a total of " + str(dmg) + " damage")
        return dmg

    def skillTwo(self):
        i = 1 + rand(5)
        dmg = self.atk * i
        print(self.name + " strikes " + str(i) + " amounts of time, doing a total of " + str(dmg) + " damage")
        return dmg

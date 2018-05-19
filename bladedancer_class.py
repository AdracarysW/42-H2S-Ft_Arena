from player_class import Player

class Swordsinger(Player):

	def __init__(self, nameput):
		super().__init__(nameput, 400, 14, 3, 6, "Swordsinger")

	def skillOne(self):
		dmg = self.atk * 2
		self.df += 2
		print(self.name + " increases their defenses, allowing them to do " + str(dmg) + " damage")
		return dmg

	def skillTwo(self):
		dmg = self.atk * 3
		self.atk += 2
		print(self.name + " stregthens themselves, allowing them to do " + str(dmg) + " damage")
		return dmg

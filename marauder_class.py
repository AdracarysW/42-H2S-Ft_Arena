from player_class import Player

class Murmillo(Player):

	def __init__(self, nameput):
		super().__init__(nameput, 500, 9, 7, 5, "Murmillo")


	def skillTwo(self):
		loss = (500 - self.hp) / 4;
		self.hp += loss
		print(self.name + " recovers a quarter of their missing health! Their health healed " + str(loss) + ". Current health: " + str(self.hp))
		return 0

	def skillOne(self):
		heal = self.atk * 2
		self.hp += heal
		print(self.name + " strikes twice, healing for " + str(heal) + " points of damage. Current health: " + str(self.hp))
		return self.atk * 2

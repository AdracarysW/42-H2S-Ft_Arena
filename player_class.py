class Player():

	def __init__(self, nameput, health, attack, defense, speed, job):
		self.name = nameput
		self.hp = health
		self.atk = attack
		self.df = defense
		self.spd = speed
		self.job = job

	def getName(self):
		return self.name

	def getJob(self):
		return self.job

	def getAttack(self):
		return self.atk

	def getHealth(self):
		return self.hp

	def getStamina(self):
		return self.sp

	def getDefense(self):
		return self.df

	def getSpeed(self):
		return self.spd

	def attack(self):
		print(self.name + " attacks the enemy!")
		return self.atk

	def takeDamage(self, attack):
		self.hp -= attack - self.df
		damage = attack - self.df
		print(self.name + " took " + str(damage) + " amount of damage. Current health: " + str(self.hp))
		return attack - self.df

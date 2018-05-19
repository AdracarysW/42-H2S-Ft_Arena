import time
from random import randint

class Arena():

    class some_class:
        def __init__(self):
            players = None

    def __init__(self):
        self.players = []
        self.job
        self.name

    def menu(self):
        print("""
            Menu (Please enter the numeric value to access)
			1. Player Types
			2. Add Players
			3. Play Arena
            4. View Players
            """)
        value = input("> ")
        if str(value) == "1":
            jobDetail()
        elif str(value) == "2":
            createPlayer()
        elif str(value) == "3":
            playArena()
        elif str(value) == "4":
            viewPlayer()
        elif value == "exit" or value == "quit":
            print("Exiting arena")
        else:
            menu()

    def fight(self, x, y):
		i = 3
		print("BATTLE WILL COMMENCE BETWEEN " + self.players[x].getName.upper + " AND " + self.players[y].getName.upper)
		while i >= 0:
            print(str(i) + "...")
            time.sleep(1)
            i -= 1

		while self.players[x].getHealth > 0 and self.players[y].getHealth > 0:
            i = 1 + randint(0,6)
            if (self.players[x].getSpeed > self.players[y].getSpeed):
				if i <= 3:
					self.players[y].takeDamage(self.players[x].attack)
				elif i == 6:
					self.players[y].takeDamage(self.players[x].skillTwo)
				else:
					self.players[y].takeDamage(self.players[x].skillOne)

				if (self.players[y].getHealth <= 0):
					print(self.players[x].getName + " won the fight!")
					menu()

				i = 1 + randint(0,6)
				if i <= 3:
					self.players[x].takeDamage(self.players[y].attack)
				elif i == 6:
					self.players[x].takeDamage(self.players[y].skillTwo)
				else:
					self.players[x].takeDamage(self.players[y].skillOne)

				if (self.players[x].getHealth <= 0):
					print(self.players[y].getName + " won the fight!")
					menu()
				print("")
                # time.sleep(2)
			else:
				i = 1 + randint(0,6)
				if i <= 3:
					self.players[x].takeDamage(self.players[y].attack)
				elif i == 6:
					self.players[x].takeDamage(self.players[y].skillTwo)
				else:
					self.players[x].takeDamage(self.players[y].skillOne)

				if (self.players[x].getHealth <= 0):
					print(self.players[y].getName + " won the fight!")
					menu()

				i = i + randint(0,6)
				if i <= 3:
					self.players[y].takeDamage(self.players[x].attack)
				elif i == 6:
					self.players[y].takeDamage(self.players[x].skillTwo)
				else:
					self.players[y].takeDamage(self.players[x].skillOne)

				if (self.players[y].getHealth <= 0):
					print(self.players[x].getName + " won the fight!")
					menu()
			print("")
			time.sleep(2)


	def playArena(self):
		if self.players.size <= 1:
			print("You must have at least two players to begin fighting")
		else:
			i = 0;
			print("Please type the number for the player you want to use for player one")
			while i < self.players.size:
					print("Player " + str(i) + ": " + self.players[i].getName + " (" + self.players[i].getJob + ")")
				i += 1
			input = int(input("> "))
			if input >= self.players.size;
				print("Please enter a valid player number (just the number)")
			else:
				print("Please type the number for the player you want to use for player two")
				num2 = int(input("> "))
				if num2 >= self.players.size:
					print("Please enter a valid player number (just the number)")
				elif num2 == input:
					print("You cannot repeat the same player number")
				else:
					fight(num1, num2)
		menu()

	def viewPlayer(self):
		i = 0;
		if self.players.size == 0:
			print("No players has been added yet")
		else:
			while i < self.players.size:
				if (i != 0):
					print("")
				print("Player Name: " + self.players[i].getName + ("\n")
					"Player Job: " + self.players[i].getJob + ("\n")
					"Health: " + self.players[i].str(getHealth) + ("\n")
					"Attack: " + self.players[i].str(getAttack) + ("\n")
					"Defense: " + self.players[i].str(getDefense) + ("\n")
					"Speed: " + self.players[i].str(getSpeed))
				i += 1
		menu()

	def jobDetail(self):
		print("""
            There are three jobs that players can obtain:

			Marauder: Aggresive melee fighter who specializes in defense and survivability
			Skill 1: Recovers half of their missing health
			Skill 2: Strikes twice and heals self for the damage dealt

			BladeDancer: Close combat spell caster that mix melee and magic
			Skill 1: Raises own defense while dealing damage
			Skill 2: Raises own attack while dealing damage

			Rogue: Swift ranged users who specialize in multiple hits
			Skill 1: Strikes enemy three times with reduce damage
			Skill 2: Hits enemy a random amount of time with no damage penalty

            """)
		menu()

	def createPlayer(self):
		print("Please provide what job you want the player to be:")
		job = input("> ")
		if (job.casecmp("MARAUDER") == 0 || job.casecmp("BLADEDANCER") == 0 ||
			job.casecmp("ROGUE") == 0):
			print("Please proivde a name for the player:")
			nameput = input("> ")
			addPlayer(job, nameput)
		else:
			print("Invalid job, please enter a valid player type")
		menu()


	def addPlayer(self, job, nameput):
		if job.casecmp("MARAUDER") == 0:
			player = Marauder.new(nameput)
			print("Created Marauder player")
		elif job.casecmp("BLADEDANCER") == 0:
			player = Swordsinger.new(nameput)
			print("Created Swordsinger player")
		elif job.casecmp("ROGUE") == 0:
			player = Rogue.new(nameput)
			print("Created Rogue player")
		self.players.push(player)

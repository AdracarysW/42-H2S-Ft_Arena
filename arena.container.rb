class Arena
	attr_accessor :players

	def initialize
		@players = []
		@job
		@name
	end

	def menu
		puts "Menu (Please enter the numeric value to access)",
			"1. Player Types",
			"2. Add Players",
			"3. Play Arena",
			"4. View Players"
		print "> "
		input = gets.chomp
		if input.to_s == "1"
			jobDetail
		elsif input.to_s == "2"
			createPlayer
		elsif input.to_s == "3"
			playArena
		elsif input.to_s == "4"
			viewPlayer
		elsif input == "exit" or input == "quit"
			puts "Exiting arena"
		else
			menu
		end
	end

	def fight(x, y)
		i = 3
		puts "BATTLE WILL COMMENCE BETWEEN " + @players[x].getName.upcase + " AND " + @players[y].getName.upcase
		while i >= 0 do
			puts i.to_s + "..."
			sleep 1
			i -= 1
		end
		while @players[x].getHealth > 0 and @players[y].getHealth > 0
			i = 1 + rand(6)
			if (@players[x].getSpeed > @players[y].getSpeed)
				if i <= 3
					@players[y].takeDamage(@players[x].attack)
				elsif i == 6
					@players[y].takeDamage(@players[x].skillTwo)
				else
					@players[y].takeDamage(@players[x].skillOne)
				end
				if (@players[y].getHealth <= 0)
					puts @players[x].getName + " won the fight!"
					menu
				end
				i = 1 + rand(6)
				if i <= 3
					@players[x].takeDamage(@players[y].attack)
				elsif i == 6
					@players[x].takeDamage(@players[y].skillTwo)
				else
					@players[x].takeDamage(@players[y].skillOne)
				end
				if (@players[x].getHealth <= 0)
					puts @players[y].getName + " won the fight!"
					menu
				end
				puts ""
				sleep 2
			else
				i = 1 + rand(6)
				if i <= 3
					@players[x].takeDamage(@players[y].attack)
				elsif i == 6
					@players[x].takeDamage(@players[y].skillTwo)
				else
					@players[x].takeDamage(@players[y].skillOne)
				end
				if (@players[x].getHealth <= 0)
					puts @players[y].getName + " won the fight!"
					menu
				end
				i = i + rand(6)
				if i <= 3
					@players[y].takeDamage(@players[x].attack)
				elsif i == 6
					@players[y].takeDamage(@players[x].skillTwo)
				else
					@players[y].takeDamage(@players[x].skillOne)
				end
				if (@players[y].getHealth <= 0)
					puts @players[x].getName + " won the fight!"
					menu
				end
			end
			puts ""
			sleep 2
		end
	end

	def playArena
		if @players.size <= 1
			puts "You must have at least two players to begin fighting"
		else
			i = 0;
			puts "Please type the number for the player you want to use for player one"
			while i < @players.size do
					puts "Player " + i.to_s + ": " + @players[i].getName + " (" + @players[i].getJob + ")"
				i += 1
			end
			print "> "
			input = gets.to_i
			if input >= @players.size
				puts "Please enter a valid player number (just the number)"
			else
				puts "Please type the number for the player you want to use for player two"
				print "> "
				input2 = gets.to_i
				if input2 >= @players.size
					puts "Please enter a valid player number (just the number)"
				elsif input2 == input
					puts "You cannot repeat the same player number"
				else
					fight(input, input2)
				end
			end
		end
		menu
	end

	def viewPlayer
		i = 0;
		if @players.size == 0
			puts "No players has been added yet"
		else
			while i < @players.size do
				if (i != 0)
					puts ""
				end
				puts "Player Name: " + @players[i].getName,
					"Player Job: " + @players[i].getJob,
					"Health: " + @players[i].getHealth.to_s,
					"Attack: " + @players[i].getAttack.to_s,
					"Defense: " + @players[i].getDefense.to_s,
					"Speed: " + @players[i].getSpeed.to_s
				i += 1
			end
		end
		menu
	end

	def jobDetail
		puts "There are three jobs that players can be",
			"Murmillo: Aggresive melee fighter who specialize in defense and survivability",
			"Skill 1: Recovers half of their missing health",
			"Skill 2: Strikes twice and heals self for the damage dealt", " ",
			"Swordsinger: Close combat spell caster that mix melee and magic",
			"Skill 1: Raises own defense while dealing damage",
			"Skill 2: Raises own attack while dealing damage", " ",
			"Mergen: Swift ranged users who specialize in multiple hits",
			"Skill 1: Strikes enemy three times with reduce damage",
			"Skill 2: Hits enemy a random amount of time with no damage penalty"
		menu
	end

	def createPlayer
		puts "Please provide what job you want the player to be:"
		print "> "
		input = gets.chomp
		if (input.casecmp("MURMILLO") == 0 || input.casecmp("SWORDSINGER") == 0 ||
			input.casecmp("MERGEN") == 0)
			puts "Please proivde a name for the player:"
			print "> "
			nameput = gets.chomp
			addPlayer(input, nameput)
		else
			puts "Invalid job, please enter a valid player type"
		end
		menu
	end

	def addPlayer(input, nameput)
		if input.casecmp("MURMILLO") == 0
			player = Murmillo.new(nameput)
			puts "Created Murmillo player"
		elsif input.casecmp("SWORDSINGER") == 0
			player = Swordsinger.new(nameput)
			puts "Created Swordsinger player"
		elsif input.casecmp("MERGEN") == 0
			player = Mergen.new(nameput)
			puts "Created Mergen player"
		end
		@players.push(player)
	end

end

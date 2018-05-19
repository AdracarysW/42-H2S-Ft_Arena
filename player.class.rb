class Player

	def initialize(nameput, health, attack, defense, speed, job)
		@name = nameput
		@hp = health
		@atk = attack
		@def = defense
		@spd = speed
		@job = job
	end

	def getName
		return @name
	end

	def getJob
		return @job
	end

	def getAttack
		return @atk
	end

	def getHealth
		return @hp
	end

	def getStamina
		return @sp
	end

	def getDefense
		return @def
	end

	def getSpeed
		return @spd
	end

	def attack
		puts @name + " attacks the enemy!"
		return @atk
	end

	def takeDamage(attack)
		@hp -= attack - @def
		damage = attack - @def
		puts @name + " took " + damage.to_s + " amount of damage. Current health: " + @hp.to_s
		return attack - @def
	end
end

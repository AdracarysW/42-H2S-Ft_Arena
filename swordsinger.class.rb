class Swordsinger < Player

	def initialize(nameput)
		super(nameput, 400, 14, 3, 6, "Swordsinger")
	end

	def skillOne
		dmg = @atk * 2
		@def += 2
		puts @name + " increases their defenses, allowing them to do " + dmg.to_s + " damage"
		return dmg
	end

	def skillTwo
		dmg = @atk * 3
		@atk += 2
		puts @name + " stregthens themselves, allowing them to do " + dmg.to_s + " damage"
		return dmg
	end
end

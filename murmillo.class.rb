class Murmillo < Player

	def initialize(nameput)
		super(nameput, 500, 9, 7, 5, "Murmillo")
	end

	def skillTwo
		loss = (500 - @hp) / 4;
		@hp += loss
		puts @name + " recovers a quarter of their missing health! Their health healed " + loss.to_s + ". Current health: " + @hp.to_s
		return 0
	end

	def skillOne
		heal = @atk * 2
		@hp += heal
		puts @name + " strikes twice, healing for " + heal.to_s + " points of damage. Current health: " + @hp.to_s
		return @atk * 2
	end
end

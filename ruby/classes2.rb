class Player
    # attr_accessor creater getters and setters for our instance variables
    attr_accessor :name, :team

    @@num_players = 0

    def initialize(name, team)
        @name = name
        @team = team
        @@num_players = @@num_players + 1
    end
    
    # Class method with self before
    def self.num_players
        @@num_players
    end

end

# create a child class from Player
class Crack < Player
    attr_accessor :ability
    def initialize(name, team, ability)
        @name = name
        @team = team
        @@num_players = @@num_players + 1
        @ability = ability
    end 
end


player = Player.new("pablo", "sfb")
player2 = Player.new("pedro", "sfb")

puts player.name
player.name = "Pablito"
puts player.name

puts Player.num_players

crack = Crack.new("messi", "fcb", "regate")
puts crack.name

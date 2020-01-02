
class Player

    @@num_players = 0

    def initialize(name, team)
        @name = name
        @team = team
        @@num_players = @@num_players + 1
    end
    # GETTERS For instance variables
    def name
        @name
    end
    def team
        @team
    end

    # Class method with self before
    def self.num_players
        @@num_players
    end

    # SETTERS
    def name=(name)
        @name = name
    end
    def team=(team)
        @team=team
    end
end


player = Player.new("pablo", "sfb")
player2 = Player.new("pedro", "sfb")

puts player.name
player.name = "Pablito"
puts player.name

puts Player.num_players

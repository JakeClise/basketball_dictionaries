
class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
    
    def __repr__(self):
        return f'Player: {self.name} Age: {self.age} Position: {self.position} Team: {self.team}'


kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

#CREATE A NEW PLAYER
lauren = {
    "name": "Lauren Clise",
    "age": 28, 
    "position": "Point Guard",
    "team": "Chicago Bulls"
}

#CREATE PLAYER INSTANCES
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
player_lauren = Player(lauren)

print(player_kevin)
print(player_jason)
print(player_kyrie)
print(player_lauren)












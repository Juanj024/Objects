class Player:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} {self.position}"


player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

playerList = [player1,player2,player3,player4]

class Team:
    name = "Saviors"
    teamPlayers = playerList

    def __str__(self):
        players_str = "\n ".join([str(player) for player in self.teamPlayers])
        return f"{ self.name}\n {players_str}"

team =Team()
print(team)
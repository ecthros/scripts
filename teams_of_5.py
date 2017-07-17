import operator

class Player(object): #player object, has name and elo
	def __init__(self, name, elo):
		self.name = name
		self.elo = elo

	def __str__(self):
		return str(self.name) + "\t\t" + str(self.elo)



##########################
# CREATE PLAYERS HERE!!!!! 

p1 = Player("Jake1", 1001)
p2 = Player("Jake2", 1300)
p3 = Player("Jake3", 3145)
p4 = Player("Jake4", 3462)
p5 = Player("Jake5", 2433)
p6 = Player("Jake6", 1346)
p7 = Player("Jake7", 245)
p8 = Player("Jake8", 2452)
p9 = Player("Jake9", 3453)
p10 = Player("Jake10", 1032)

##########################



def choose_iter(players, length): #chooses groups of 5 from size 10
	for i in range(len(players)):
		if length == 1:
			yield (players[i],)
		else:
			for player in choose_iter(players[i+1:len(players)], length-1):
				yield (players[i],) + player


class Team(object): #team object, has array of players and elo
	def __init__(self, p1, p2, p3, p4, p5, elo):
		
		self.totalElo = elo
		self.players = [p1, p2, p3, p4, p5]

	def __str__(self):
		string = "Team: (" + str(self.totalElo) + "): \n"
		for player in self.players:
			string += "\t" + str(player)
			string += "\n"
		return string

class Game(object): #game object, has two teams and a difference in elo
	def __init__(self, t1, t2):
		self.t1 = t1
		self.t2 = t2
		if self.t1.totalElo > self.t2.totalElo:
			self.diff = self.t1.totalElo - self.t2.totalElo
		else:
			self.diff = self.t2.totalElo - self.t1.totalElo

	def __str__(self):
		string = "Game (" + str(self.diff) + "): \n"
		string += "    " + str(self.t1)
		string += "    " + str(self.t2)
		return string



players = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
teams = []

for team in choose_iter(players, 5):
	teamMembers = []
	totalElo = 0
	for player in team:
		totalElo += player.elo
		teamMembers.append(player)
	teams.append(Team(teamMembers[0], teamMembers[1], teamMembers[2], teamMembers[3], teamMembers[4], totalElo))

teams2 = teams
games = []
for team in teams:
	for team2 in teams2:
		if(team.players[0] not in team2.players) and ((team.players[1] not in team2.players)) and (team.players[2] not in team2.players) and (team.players[3] not in team2.players) and (team.players[4] not in team2.players):
			newGame = Game(team, team2)
			games.append(newGame)


sorted_games = sorted(games, key=operator.attrgetter("diff"), reverse=True)

for game in sorted_games[1::2]: #this is some cancer to remove duplicates, but should work
	print game
import json

class Unit:

	PLAYER = 0
	ENEMY = 1

	def __init__(self, stats_path, alliance):
		self.alliance = alliance
		with open(stats_path, "r") as read_file:
			self.data = json.load(read_file)

	def __str__(self):
		return self.data["name"]

	__repr__ = __str__
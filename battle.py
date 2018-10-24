from unit import Unit

jarrock = Unit("jarrock.json", Unit.PLAYER)
narry = Unit("narry.json", Unit.PLAYER)
running = True

class Battle:

	def __init__(self):
		self.units = []

	def add_unit(self, unit):
		self.units.append(unit)

	def remove_unit(self, unit):
		self.units.remove(unit)

	def start_battle(self):
		#sort the units by speed
		self.units.sort(key = lambda x: x.data["speed"], reverse = True)
		print(self.units)
		#while(running):
			#do things

battle = Battle()
battle.add_unit(jarrock)
battle.add_unit(narry)
battle.start_battle()

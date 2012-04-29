
class General():
	def __init__(self):
		pass

	def getBetween(self, Str, Start, End):
		Loc1 = Str.find(Start)
		Loc1 += len(Start)
		#print "LOC1: " + str(Loc1)
		Loc2 = Str[Loc1:len(Str)].find(End)+Loc1
		#print "LOC2: " + str(Loc2)
		return Str[Loc1:Loc2]
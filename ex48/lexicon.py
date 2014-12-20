# pass argument 'north' into scan, should return 'directions' and 'north'
# pass argument "north south east", and result should be an array [direction, north] [direction, south] [direction, east]
# pass argument 'go', return verb, go
directions = ["north", "south", "east"]
verbs = ["go", "kill", "eat"]
stops = ["the", "in", "of"]
nouns = ['bear', "princess"]

def scan(argument):
	try:
		words = argument.split()
		numlist = []
		for i in words:
			numlist.append(('number', int(i)))
		return numlist
	except ValueError:
		words = argument.split()
		list = []
		for x in words:
			if x in directions:
				list.append(('direction', x))
			if x in verbs:
				list.append(('verb', x))
			if x in stops:
				list.append(('stop', x))
			if x in nouns:
				list.append(('noun', x))
			if x not in directions and x not in verbs and x not in stops and x not in nouns:
				list.append(('error', x))
		return list



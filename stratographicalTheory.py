# stratographicalTheory.py
# Luke Haskins
# trivia_prep

import random

def stratTheory():
	# intro
	print "This program is to test your memorization of the various stages of earth's formation according to modern American theory."

	# basic version: Create a random number (A year between 0 and 4.6 billion) and have a user name the eon to which it belongs
	randNum = random.randint(0, 4600000000)
	
	# determine Eon, Era, Period, Epoch, and Age
	if (randNum <= 541000000):
		supereon = "None"
		eon = "Phanerozoic"
		if (randNum <= 66000000):
			era = "Cenozoic"
		elif (randNum <= 251902000):
			era = "Mesozoic"
		else:
			era = "Paleozoic"
	else:
		supereon = "Precambrian"
		if (randNum <= 2500000000):
			eon = "Proterozoic"
			if (randNum <= 1600000000):
				era = "Neoproterozoic"
			elif (randNum <= 1000000000):
				era = "Mesoproterozoic"
			else:
				era = "Paleoproterozoic"
		elif (randNum <= 4000000000):
			eon = "Archean"
			if (randNum <= 2800000000):
				era = "Neoarchean"
			elif (randNum <= 3200000000):
				era = "Mesoarchean"
			elif (randNum <= 3600000000):
				era = "Paleoarchean"
			else:
				era = "Eoarchean"
		else:
			eon = "Hadean"
			era = "None"
			period = "None"
			epoch = "None"
			age = "None"

	# print results
	print supereon
	print eon
	print era

stratTheory()
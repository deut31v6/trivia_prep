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
			if (randNum <= 2580000):
				period = "Quaternary"
				if (randNum <= 11700):
					epoch = "Holocene"
					if (randNum <= 4200):
						age = "Meghalayan"
					elif (randNum <= 8200):
						age = "Northgrippian"
					else:
						age = "Greenlandian"
				else:
					epoch = "Pleistocene"
					if (randNum <= 129000):
						age = "Upper"
					elif (randNum <= 774000):
						age = "Chibanian"
					elif (randNum <= 1800000):
						age = "Calabrian"
					else:
						age = "Gelasian"
			elif (randNum <= 23030000):
				period = "Neogene"
				if (randNum <= 5333000):
					epoch = "Pliocene"
					if (randNum <= 3600000):
						age = "Piacenzian"
					else:
						age = "Zanclean"
				else:
					epoch = "Miocene"
					if (randNum <= 7246000):
						age = "Messinian"
					elif (randNum <= 11630000):
						age = "Tortonian"
					elif (randNum <= 13820000):
						age = "Serravallian"
					elif (randNum <= 15970000):
						age = "Langhian"
					elif (randNum <= 20440000):
						age = "Burdigalian"
					else:
						age = "Aquitanian"
			else:
				period = "Paleogene"
				if (randNum <= 33900000):
					epoch = "Oligocene"
					if (randNum <= 27820000):
						age = "Chattian"
					else:
						age = "Rupelian"
				elif (randNum <= 56000000):
					epoch = "Eocene"
					if (randNum <= 37800000):
						age = "Priabonian"
					elif (randNum <= 41200000):
						age = "Bartonian"
					elif (randNum <= 47800000):
						age = "Lutetian"
					else:
						age = "Ypresian"
				else:
					epoch = "Paleocene"
					if (randNum <= 59200000):
						age = "Thanetian"
					elif (randNum <= 61600000):
						age = "Selandian"
					else:
						age = "Danian"
		elif (randNum <= 251902000):
			era = "Mesozoic"
			if (randNum <= 145000000):
				period = "Cretaceous"
				if (randNum <= 100500000):
					epoch = "Upper"
					if (randNum <= 72100000):
						age = "Maastrichtian"
					elif (randNum <= 83600000):
						age = "Campanian"
					elif (randNum <= 86300000):
						age = "Santonian"
					elif (randNum <= 89800000):
						age = "Coniacian"
					elif (randNum <= 93900000):
						age = "Turonian"
					else:
						age = "Cenomanian"
				else:
					epoch = "Lower"
					if (randNum <= 113000000):
						age = "Albian"
					elif (randNum <= 125000000):
						age = "Aptian"
					elif (randNum <= 129400000):
						age = "Barremian"
					elif (randNum <= 132600000):
						age = "Hauterivian"
					elif (randNum <= 139800000):
						age = "Valanginian"
					else:
						age = "Barriasian"
			elif (randNum <= 201300000):
				period = "Jurassic"
				if (randNum <= 163500000):
					epoch = "Upper"
					if (randNum <= 152100000):
						age = "Tithonian"
					elif (randNum <= 157300000):
						age = "Kimmeridgian"
					else:
						age = "Oxfordian"
				elif (randNum <= 174100000):
					epoch = "Middle"
					if (randNum <= 166100000):
						age = "Callovian"
					elif (randNum <= 168300000):
						age = "Bathonian"
					elif (randNum <= 170300000):
						age = "Bajocian"
					else:
						age = "Aalenian"
				else:
					epoch = "Lower"
					if (randNum <= 182700000):
						age = "Toarcian"
					elif (randNum <= 190800000):
						age = "Pliensbachian"
					elif (randNum <= 199300000):
						age = "Sinemurian"
					else:
						age = "Hettangian"
			else:
				period = "Triassic"
				if (randNum <= 237000000):
					epoch = "Upper"
					if (randNum <= 208500000):
						age = "Rhaetian"
					elif (randNum <= 227000000):
						age = "Norian"
					else:
						age = "Carnian"
				elif (randNum <= 247200000):
					epoch = "Middle"
					if (randNum <= 242000000):
						age = "Ladinian"
					else:
						age = "Anisian"
				else:
					epoch = "Lower"
					if (randNum <= 251200000):
						age = "Olenekian"
					else:
						age = "Induan"
		else:
			era = "Paleozoic"
			if (randNum <= 298900000):
				period = "Permian"
				if (randNum <= 259100000):
					epoch = "Lopingian"
					if (randNum <= 254140000):
						age = "Changhsingian"
					else:
						age = "Wuchiapingian"
				elif (randNum <= 272950000):
					epoch = "Guadalupian"
					if (randNum <= 265100000):
						age = "Capitanian"
					elif (randNum <= 268800000):
						age = "Wordian"
					else:
						age = "Roadian"
				else:
					epoch = "Cisuralian"
					if (randNum <= 283500000):
						age = "Kungurian"
					elif (randNum <= 290100000):
						age = "Artinskian"
					elif (randNum <= 293520000):
						age = "Sakmarian"
					else:
						age = "Asselian"
			elif (randNum <= 358900000):
				period = "Carboniferous"
				if (randNum <= 323200000):
					epoch = "Pennsylvanian"
					if (randNum <= 303700000):
						age = "Gzhelian"
					elif (randNum <= 307000000):
						age = "Kasimovian"
					elif (randNum <= 315200000):
						age = "Moscovian"
					else:
						age = "Bashkirian"
				else:
					epoch = "Mississippian"
					if (randNum <= 330900000):
						age = "Serpukhovian"
					elif (randNum <= 346700000):
						age = "Visean"
					else:
						age = "Tournaisian"
			elif (randNum <= 419200000):
				period = "Devonian"
				if (randNum <= 382700000):
					epoch = "Upper"
					if (randNum <= 372200000):
						age = "Famennian"
					else:
						age = "Frasnian"
				elif (randNum <= 393300000):
					epoch = "Middle"
					if (randNum <= 387700000):
						age = "Givetian"
					else:
						age = "Eifelian"
				else:
					epoch = "Lower"
					if (randNum <= 407600000):
						age = "Emsian"
					elif (randNum <= 410800000):
						age = "Pragian"
					else:
						age = "Lochkovian"
			elif (randNum <= 443800000):
				period = "Silurian"
				if (randNum <= 423000000):
					epoch = "Pridoli"
					age = "None"
				elif (randNum <= 427400000):
					epoch = "Ludlow"
					if (randNum <= 425600000):
						age = "Ludfordian"
					else:
						age = "Gorstian"
				elif (randNum <= 433400000):
					epoch = "Wenlock"
					if (randNum <= 430500000):
						age = "Homerian"
					else:
						age = "Sheinwoodian"
				else:
					epoch = "Llandovery"
					if (randNum <= 438500000):
						age = "Telychian"
					elif (randNum <= 440800000):
						age = "Aeronian"
					else:
						age = "Rhuddanian"
			elif (randNum <= 485400000):
				period = "Ordovician"
				if (randNum <= 458400000):
					epoch = "Upper"
					if (randNum <= 445200000):
						age = "Himantian"
					elif (randNum <= 453000000):
						age = "Katian"
					else:
						age = "Sandbian"
				elif (randNum <= 470000000):
					epoch = "Middle"
					if (randNum <= 467300000):
						age = "Darriwilian"
					else:
						age = "Dapingian"
				else:
					epoch = "Lower"
					if (randNum <= 477700000):
						age = "Floian"
					else:
						age = "Tremadocian"
			else:
				period = "Cambrian"
				if (randNum <= 497000000):
					epoch = "Furongian"
					if (randNum <= 489500000):
						age = "Stage 10"
					elif (randNum <= 494000000):
						age = "Jiangshanian"
					else:
						age = "Paibian"
				elif (randNum <= 509000000):
					epoch = "Miaolingian"
					if (randNum <= 500500000):
						age = "Guzhangian"
					elif (randNum <= 504500000):
						age = "Drumian"
					else:
						age = "Wuliuan"
				elif (randNum <= 521000000):
					epoch = "Series 2"
					if (randNum <= 514000000):
						age = "Stage 4"
					else:
						age = "Stage 3"
				else:
					epoch = "Terreneuvian"
					if (randNum <= 529000000):
						age = "Stage 2"
					else:
						age = "Fortunian"
	else:
		supereon = "Precambrian"
		if (randNum <= 2500000000):
			eon = "Proterozoic"
			if (randNum <= 1000000000):
				era = "Neoproterozoic"
				if (randNum <= 635000000):
					period = "Ediacaran"
					epoch = "None"
					age = "None"
				elif (randNum <= 720000000):
					period = "Cryogenian"
					epoch = "None"
					age = "None"
				else:
					period = "Tonian"
					epoch = "None"
					age = "None"
			elif (randNum <= 1600000000):
				era = "Mesoproterozoic"
				if (randNum <= 1200000000):
					period = "Stenian"
					epoch = "None"
					age = "None"
				elif (randNum <= 1400000000):
					period = "Ectasian"
					epoch = "None"
					age = "None"
				else:
					period = "Calymmian"
					epoch = "None"
					age = "None"
			else:
				era = "Paleoproterozoic"
				if (randNum <= 1800000000):
					period = "Statherian"
					epoch = "None"
					age = "None"	
				elif (randNum <= 2050000000):
					period = "Orosirian"
					epoch = "None"
					age = "None"
				elif (randNum <= 2300000000):
					period = "Rhyacian"
					epoch = "None"
					age = "None"
				else:
					period = "Siderian"
					epoch = "None"
					age = "None"
		elif (randNum <= 4000000000):
			eon = "Archean"
			if (randNum <= 2800000000):
				era = "Neoarchean"
				period = "None"
				epoch = "None"
				age = "None"
			elif (randNum <= 3200000000):
				era = "Mesoarchean"
				period = "None"
				epoch = "None"
				age = "None"
			elif (randNum <= 3600000000):
				era = "Paleoarchean"
				period = "None"
				epoch = "None"
				age = "None"
			else:
				era = "Eoarchean"
				period = "None"
				epoch = "None"
				age = "None"
		else:
			eon = "Hadean"
			era = "None"
			period = "None"
			epoch = "None"
			age = "None"

	# print results
	print randNum
	print supereon
	print eon
	print era
	print period
	print epoch
	print age

stratTheory()
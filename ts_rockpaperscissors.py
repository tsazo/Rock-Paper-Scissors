from random import choice

print "This is rock, paper, scissors.\nI'm Jasmine, a program designed to beat you at this game.\n Ready? Type 'Rock', 'Paper', 'Scissors', or quit if you want to stop playing."
comp_score = 0
human_score = 0

while True:
	s = ["Rock", "Paper", "Scissors"]
	comp = choice(s)
	s = raw_input("> ")

	if s == comp:
		print "I play", comp
		print "Tie... No points for either of us."
		print "Your score:", human_score
		print "My score:", comp_score
	elif s == "Rock":
		if comp == "Scissors":
			print "I play", comp
			print "You hacked..."
			human_score = human_score + 1
			print "Your score:", human_score
			print "My score:", comp_score
		else:
			print "I play", comp
			print "Can\'t beat me."
			comp_score = comp_score + 1
			print "Your score:", human_score
			print "My score:", comp_score
	elif s == "Paper":
		if comp == "Rock":
			print "I play", comp
			print "You hacked..."
			human_score = human_score + 1
			print "Your score:", human_score
			print "My score:", comp_score
		else:
			print "I play", comp
			print "Can\'t beat me."
			comp_score = comp_score + 1
			print "Your score:", human_score
			print "My score:", comp_score
	elif s == "Scissors":
		if comp == "Paper":
			print "I play", comp
			print "You hacked..."
			human_score = human_score + 1
			print "Your score:", human_score
			print "My score:", comp_score
		else:
			print "I play", comp
			print "Can\'t beat me."
			comp_score = comp_score + 1
			print "Your score:", human_score
			print "My score:", comp_score
	elif s == "quit" or s == "Quit":
		break
	else:
		print "Invalid answer, type in 'Rock', 'Paper', 'Scissors', or 'quit' if you want to stop playing." 

if human_score == comp_score:
	print "Good Game."
	print "Your score:", human_score
	print "My score:", comp_score
elif comp_score>human_score:
	print "Well, told you I was programmed to defeat you."
else:
	print "I don't know how you did it. Until next time."
print("As you begin to dream, you find yourself in a long hallway with two doors. One is red. One is blue.")
user_answer1 = input("Do you walk through the red or the blue?: ")
while user_answer1 != "red" and user_answer1 != "blue":
	user_answer1 = input("Do you walk through the red or the blue?: ")
if user_answer1 == "red":
	print("You decided to enter through the red door. You encounter a wizard and a centaur who each promise to lead you to what you most desire.")
	user_answer2 = input("Who do you go with?: ")
	while user_answer2 != "wizard" and user_answer2 != "centaur":
		user_answer2 = input("Who do you go with?: ")
	if user_answer2 == "wizard":
		print("You decided to follow the wizard. You make it no farther than five feet before he traps you and brews you into a potion of gold. You die.")
	else:
		print("You decided to follow the centaur. You climb his back and you ride to a cave. In that cave, you find two bottles. One is a steaming purple milk with the scent of plums. The other foams green with the sea of lichen.")
		user_answer4 = input("Do you drink the purple or the green?: ")
		while user_answer4 != "purple" and user_answer4 != "green":
			user_answer4 = input("Do you drink the purple or the green?: ")
		if user_answer4 == "purple":
			print("You chose to drink the purple potion. You choke on goop and die. Bye.")
		else:
			print("You chose to drink the green potion. As you swallow, you blink to find yourself at home, warm in your bed. Congratulations! You have survived the test.")
else:
	print("You decided to enter through the blue door into a forest with paths toward a river and toward a mountain.")
	user_answer3 = input("Do you walk towards the river or the mountain?: ")
	while user_answer3 != "river" and user_answer3 != "mountain":
		user_answer3 = input("Do you walk towards the river or the mountain?: ")
	if user_answer3 == "river":
		print("You decided to walk towards the river, coming across a boat that takes you safely to a cave. In that cave, you find two bottles. One is a steaming purple milk with the scent of plums. The other foams green with the sea of lichen.")
		user_answer5 = input("Do you drink the purple or the green?: ")
		while user_answer5 != "purple" and user_answer5 != "green":
			user_answer5 = input("Do you drink the purple or the green?: ")
		if user_answer5 == "purple":
			print("You chose to drink the purple potion. You choke on goop and die. Bye.")
		else:
			print("You chose to drink the green potion. As you swallow, you blink to find yourself at home, warm in your bed. Congratulations! You have survived the test.")
	else:
		print("You decided to walk to the path of the perilous mountains. You start to climb only to be squished in an avalanche. You die.")

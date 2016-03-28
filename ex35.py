#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from sys import exit # sys is the library systems
# exit is a special function, that allows us to use some functions
# refering them without having to define them first.

def gold_room():
	print "This room is full of gold. How much do you take? Enter a number."
	
	choice = raw_input("> ") # assigns the raw input that a person gives to a variable called choice
	if "0" in choice or "1" in choice:
		how_much = int(choice) # the number entered as raw input is saved as a string, and the function int() converts it to an integer.
	else: # if we type anything other than 0 or 1, it 
		dead("Man, learn to type a number.") # function dead is defined bellow
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
		# exit is a system function that was imported at the top
		# 0 is a code for an error-free exit (vs. 2, 16, 89, etc.); there are no errors
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	# bear_moved is a boolean variable
	
	while True: 
	# the while True keeps it going forever
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved: # ok, now I get it: bear_moved is False (see above)
		# this condition says that if you write taunt bear and not bear_moved (which means that bear moved is False, which is the case)
		# then bear_moved changes to True
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" in choice:
	# if a person types flee in the previous prompt,
	# it starts the function start() which is defined bellow
		start()
	elif "head" in choice:
	# if your type head, the function dead() is run (also defined bellow)
		dead("Well that was tasty!")
	else:
		cthulhu_room()
	# if you type anything else you go to the beginning of the room.
def dead(why):
	# why will be what is writen inside the dead('this is the why')'s above 
	print why, "Good job!" # so it prints the why and then says good job.
	exit(0) # and then you have the exit() function with 0, without an error

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left": # if you type left, bear_room is run
		bear_room()
	
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()
# this is the only function that is run automatically from the beginning

# Why did you write while True ?
# That makes an infinite loop.

# What does exit(0) do?
# On many operating systems a program can abort with exit(0) ,
# and the number passed in will indicate an error or not. If you do
# exit(1) then it will be an error, but exit(0) will be a good exit.
# The reason it's backward from normal boolean logic (with
# 0==False is that you can use different numbers to indicate
# different error results. You can do exit(100) for a different error
# result than exit(2) or exit(1) .
# Why is raw_input() sometimes written as raw_input('> ') ?
# The parameter to raw_input is a string t
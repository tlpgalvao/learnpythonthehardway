#-*-coding:utf8;-*-
#qpy:2
#qpy:console

people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs."

# The code x += 1 is the same as doing x = x + 1 but involves
# less typing. You can call this the "increment by" operator. The
# same goes for -= and many other expressions you'll learn later.

# An if-statement creates what is called a "branch" in the code. It's
# kind of like those choose your own adventure books where
# you are asked to turn to one page if you make one choice,
# and another if you go a different direction. The if‐statement
# tells your script, "If this boolean expression is True, then run
# the code under it, otherwise skip it."

# A colon at the end of a line is how you tell Python
# you are going to create a new "block" of code, and then
# indenting four spaces tells Python what lines of code are in
# that block. This is exactly the same thing you did when you
# made functions in the first half of the book.

# If it isn't indented, you will
# most likely create a Python error. Python expects you to
# indent something after you end a line with a : (colon).

# Because you are comparing numbers, if
# you change the numbers, different if-statements will
# evaluate to True and the blocks of code under them will
# run. Go back and put different numbers in and see if you can
# figure out in your head which blocks of code will run.
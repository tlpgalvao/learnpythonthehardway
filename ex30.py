#-*-coding:utf8;-*-
#qpy:2
#qpy:console

people = 20
cars = 40
trucks = 15

if cars > people and trucks > cars:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."
	
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
	
# What happens if multiple elif blocks are True ?
# Python starts and the top runs the first block that is True , so it
# will run only the first one.
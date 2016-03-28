#-*-coding:utf8;-*-
#qpy:2
#qpy:console

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print " Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Fristbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # the code runs until it's 10
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] # prints 1, the second on the list
print stuff[-1] # whoa! fancy -1 indexes form the end
print stuff.pop() # it prints the element that it pops off the list
print ' '.join(stuff) #what? cool!
print '#'.join(stuff[3:5]) # super atellar!

# What does stuff[3:5] do?
# That extracts a "slice" from the stuff list that is from element 3
# to element 4, meaning it does not include element 5. It's similar to
# how range(3,5) would work.
#-*-coding:utf8;-*-
#qpy:2
#qpy:console

# Lists

# hairs = ['brown', 'blond', 'red']
# eyes = ['brown', 'blue', 'green']
# weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in items
for i in change:
	print "I got %r" % i
	
# we can also built lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists underdtand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" %i
	
# If the start argument is omitted, it defaults to 0
# >>> range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> range(1, 11)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> range(0, 30, 5)
# [0, 5, 10, 15, 20, 25]
# >>> range(0, 10, 3)
# [0, 3, 6, 9]
# >>> range(0, -10, -1)
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# >>> range(0)
# []
# >>> range(1, 0)
# []

# for more operations on lists go to:
# https://docs.python.org/2/tutorial/datastructures.html

# How do you make a 2-dimensional (2D) list?
# That's a list in a list like this: [[1,2,3],[4,5,6]]
# Aren't lists and arrays the same thing?
# Depends on the language and the implementation. In classic
# terms a list is very different from an array because of how they're
# implemented. In Ruby though they call these arrays. In Python
# they call them lists. Just call these lists for now since that's what
# Python calls them.

# Why is a for-loop able to use a variable that isn't defined yet?
# The variable is defined by the for‐loop when it starts, initializing
# it to the current element of the loop iteration, each time through.

# Why does for i in range(1, 3): only loop two times instead of
# three times?
# The range() function only does numbers from the first to the last,
# not including the last. So it stops at two, not three in the above.
# This turns out to be the most common way to do this kind of loop.

# What does elements.append() do?
# It simply appends to the end of the list. Open up the Python shell
# and try a few examples with a list you make. Any time you run into
# things like this, always try to play with them interactively in the
# Python shell.

#-*-coding:utf8;-*-
#qpy:2
#qpy:console

# 0

i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1 # i += 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num
	
# CTRL C forces the program to abort

# 1. Convert this while-loop to a function that you can 
# call, and replace 6 in the test ( i < 6 ) with a variable.

print "/nConverting while-loop to function drill 1"

def drill_1(n):
	i = 0
	numbers1 = []
	while i < n:
		print "Item: %d" % i
		numbers1.append(1)
		i = i + 1
	print numbers1

# 2. Use this function to rewrite the script to try 
# different numbers.

print "\nUsing drill_1 with n = 3"
drill_1(3)

print "\nUsing drill_1 with n = 4"
drill_1(4)

# 3. Add another variable to the function arguments that you can
# pass in that lets you change the + 1 on line 8 so you can
# change how much it increments by.

print "\nCreating function drill_3 to allow variable step size"
def drill_3(n, s):
	i = 0
	numbers3 = []
	while i < n:
		print "Item: %d" % i
		numbers3.append(i)
		i = i + s
	print numbers3

# 4. Rewrite the script again to use this function to 
# see what effect that has.

print "\nUsing drill_3 with n = 12 and s = 3"
drill_3(12, 3)

# 5. Write it to use for-loops and range. Do you need the
# incrementor in the middle anymore? What happens if you do
# not get rid of it?

print "\ndrill_5 uses a for-loop and range instead"
def drill_5(x, n, s):
	numbers5 = range(x, n, s)
	for i in numbers5:
		print "Item: %d" % i
	print numbers5

drill_5(0, 14, 4)
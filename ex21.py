#-*-coding:utf8;-*-
#qpy:2
#qpy:console

def add(a, b):
	print "ADDING %d + %d" % (a, b) # you actually don't need print anything for this to work.
	return a + b # return creates a value that is assigned to the variable that calls the function «add»

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5) # we call function «add» (with a = 30 and b = 5) which then assigns a value to the variable «age»
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

This = (30 + 5) + ((78 - 4)  - ((90 * 2) * (100 / 2 / 2)))

print "That becomes:", what, "Can you do it by hand?"
print "I think so. Is it", This,"? Yay!"

Result = add(24, subtract(divide(34, 100), 1023))

print "This is the result:", Result,

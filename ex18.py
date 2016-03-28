#-*-coding:utf8;-*-
#qpy:2
#qpy:console

# This one is like your scripts with argv
def print_two(*args): # «def» tells python you want to use a function. The name of the function here is «print_two»
# «*args» is like «argv» for functions; «*args» must go inside «()» of the function
# we end this line with «:» and start identing.
	arg1, arg2 = args # this line unpack the arguments as we do in the scripts
	print "arg1: %r, arg2: %r" % (arg1, arg2) # we print to demonstrate how it works
	
# ok, that *args is actually pointless, we can just to this
def print_two_again(arg1, arg2): # in python we don't have to unpack the arguments
# we can just put the arguments inside «()»
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# A function can't start with a number
# The «*» in «*args» takes all arguments and puts them in args as a list.
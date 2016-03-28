#-*-coding:utf8;-*-
#qpy:2
#qpy:console

formatter = "%r %r %r %r" # this is a variable defined by four %r

print formatter % (1, 2, 3, 4) # this line prints the variable formatter and then defines it
print formatter % ("one", "two", "three", "four") # this line prints the variable formatter and then defines it
print formatter % (True, False, False, True) # this line prints the variable formatter and then defines it
print formatter % (formatter, formatter, formatter, formatter) # this line prints the variable formatter and then defines it
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	) # this line does the same thing with phrases; it shows with ' ' instead of " " because these are strings called with %r instead of %s; and " " are more efficient than ' '
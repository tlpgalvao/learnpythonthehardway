#-*-coding:utf8;-*-
#qpy:2
#qpy:console

x = "There are %d types of people." % 10 # 10 will appear in the place of %d
binary = "binary" # binary will appear when we call for binary
do_not = "don't" # don't will appear when we call for do_not
y = "Those who know %s and those who %s." % (binary, do_not) # the frist %s will be substituted by binary and the second by don't

print x # the above phrase will appear
print y # the above phrase will appear

print "I said: %r." % x # calls for the phrase which describes the x variable
print "I also said: '%s'." % y # calls for the phrase whice describes y variable

hilarious = False # False will appear when the variable hilarious is called
joke_evaluation = "Isn't that joke so funny?! %r" # this phrase will appear when the variable joke_evaluation is called

print joke_evaluation % hilarious # 1) the phrase which describes the joke_evaluation variable will appear; 2) '% hillarious' will appear in the place of %r in the joke_evaluation variable

w = "This is the left side of..." # defines the variable w
e = "a string with a right side." # defines the variable e

print w + e # prints the variable w and then the variable e
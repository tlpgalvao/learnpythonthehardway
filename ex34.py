#-*-coding:utf8;-*-
#qpy:2
#qpy:console

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print 'The first (1st) animal is at 0 and is a bear.'
print 'The second (2nd) animal is at 1 and is a python.'
print 'The third (3rd) animal is at 2 and is a peacock.'
print 'The fourth (4th) animal is at 3 and is a kangaroo.'
print 'The fifth (5th) animal is at 4 and is a whale.'
print 'The sixth (6th) animal is at 5 and is a platypus.'

print 'The animal at 5 is the sixth animal and is a platypus.'

print animals # prints every item
for i in animals: # for every animal in animals, prints every animal one per line
	print i
 
for i in range(len(animals)):
	print "Index %d in the list is %s." % (i, animals[i])

# animals is the list object
# len means lenght
# len goes to the list animals and sees how long it is
# len repeats the process the whole size of the list
# if the size of the list changes, len makes it cange automatically
# range() generates a list of numbers.
# if we put range(animals) instead of range(len(animals))
# it will give a list instead of an argument to the
# function range()

print animals[5]
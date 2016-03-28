#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') # the 'w' inside open() means that you are opening this file in the writing mode
# the 'r' inside open() means you would be opening the file in the read mode
# with 'w+' you would be opening the file in the writing and reading mode
# the open(filename) opens the file in the reading mode by default

print "Truncating the file. Goodbye!"
target.truncate() # You don't need to truncate the file, when you open in the writing mode like you did above
# truncate() stops the file here apparently, however this is not valide for 'w' or 'r'; only for 'a' which is for append

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write('%s\n%s\n%s\n' %(line1,line2,line3))

print "And finally, we close it."
target.close()
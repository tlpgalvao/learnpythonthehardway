#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from sys import argv # these lines use argv to get a filename

script, filename = argv # these lines use argv to get a filename

txt = open(filename) # the command open will be run

print "Here's your file %r:" % filename # this line prints a message
print txt.read() # function read is called on txt

print "Type the filename again:" # prints this message
file_again = raw_input("> ") # this is raw_input which is asked, and then we give it

txt_again = open(file_again) # calls the function open, on the file name that we insert on line 15

print txt_again.read() # function read is called on txt_again, which was defined on lines 15 and 17

# for study drill 6, you should do:
# txt = open("ex15_sample.txt")
# txt.read()

# to open pydoc in windows, you should do
# python -m pydoc    and in front you put the name of the command

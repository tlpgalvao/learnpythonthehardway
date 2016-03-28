#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from sys import argv # it means that we will specify something when we start the script on the command line

script, input_file = argv # script is «ex20.py» and input_file is a file that we have on the directory and we specify

def print_all(f): # this is a function that displays the entire text; the «f» is a variable name for the file
	print f.read() # prints what it reads in file named f
	
def rewind(f):
	f.seek(0) # «seek()» seeks in bytes not in lines; seek(0) seeks byte 0
	# it basically goes to the beggining of the file (byte 0)
	
def print_a_line(line_count, f):
	print line_count, f.readline() # «readline()» reads one lihe at a time of the file «f»; «line_count» is the line number we want to read
	
current_file = open(input_file) # we open «input_file», which is specified when we run ex20.py through «argv», and assign that to variable «current_file»

print "First let's print the whole file:\n" # we print this with a one line break

print_all(current_file) # «print_all» is a function defined above, which display the all text of the «current file» also defined above (line 19)

print "Now let's rewind, kind of like a tape."

rewind(current_file) # uses function «rewind» defined above (line 12) on «current_file» defined in line 19

print "Let's print three lines:"

current_line = 1 # it defines the line number on the function bellow
print_a_line(current_line, current_file) # it uses the function «print_a_line» defined on line 16 on line 1 (according to line 31) and on the current file also defined above

current_line = current_line + 1 # now this is funny, because it uses line 31 to define the line but incrementing it by 1; it is actually called an incrementing function
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# += is a contraction for x = x + y
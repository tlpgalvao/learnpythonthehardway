#-*-coding:utf8;-*-
#qpy:2
#qpy:console

Ex1:
print: displays text in the console

Ex2:
#: you can write a comment withoud disrupting the code

Ex3:
+: plus
-: minus
/: divide
*: multiply
%: Pay attention: The % (modulo) operator yields the remainder from the division of the first argument by the second
Example 1: 6%2 evaluates to 0 because there's no remainder if 6 is divided by 2 (3 times).
Example 2: 7%2 evaluates to 1 because there's a remainder of 1 when 7 is divided by 2 (3 times).
<: less than
>: greater than
<= less or equal than
>= greater or equal than

Ex4:
_: you can use underscores in variables names with two or more words
floating point: numbers with decimals
integer: numbers without decimals

Ex5:
format strings:
%s: puts a value in a strings (for words)
%: provides the value after the string. 
for example: 
a = "apple"
b = "orange"
print "we have an %s, and an %s" % (a, b)
%d: for numbers
%: for 'raw data' (but it prints with quotes 'word')

Ex6:
': single quote
": double quote

Ex7:
+: for joining strings without spaces
,: for joining strings with spaces
example:
one = "This"
two = "is"
three = "fun"
four = "!"
# the comma makes the second line continue on the first line
print one + two, # adds these variables
print three + four # adds these variables to the first printed line

Ex8:
True: it is a boolean value, a keyword that doesn't need quotes
False: works the same way, but with opposite meaning of course

Ex9:
\: backslach, used to escape characters; it doesn't literally print a letter, 
instead that letter will work as a particular command depending on the letter
\n: produces a new line
""": the triple quotes """ set off several lines of text 

Ex10:
\\: if we escape a backslash within a string, it prints a backslash straightforward
\': it escapes a single quote within a string, meaning it prints a single quote
\": it prints a double quote
\r: carriage return within a string
example:
carriage_return = "I will use a carriage\rreturn"
print carriage_return
This actually prints «return use a carriage»; the word «return» goes to the beginning of the string, 
overwriting «I will», which also has 6 letters.
\t: This is a tab within a line
'''several lines'''): Is exactaly the same as """several lines""", also allowing several lines of text within a string

Ex11:
raw_input(): it asks the user to give some input, which can be used like this:
print "How old are you?",
age = raw_input()

Or like this:
print "Write a number that will be converted to a integer",
number_integer = int(raw_input()) # where the fractional number will be converted to an integer

Ex12:
raw_input("Prompt text: "): It is an alternative way to ask a question to the user (prompt the user),
without using print
pydoc: information on the command line about the python keywords;
in windows it is called like this: «python -m pydoc keyword_we_want_to_know_more_about»

Ex13:
arguments: variable values provided by the user
pass: sending info from arguments to variables 
import: bringing addicional features into python
argv: the argument variables
packing/unpacking: to get info in and out of argv
module: the name for the collections of extra code that
can be imported into Python (AKA libraries)
example:
from sys import argv 
script, first, second, third = argv # script is actually the name of the script;
# first, second and third are the remaining variables that the user gives when he calls the script
# like this: «python ex13.py 10 23 15»
# the arguments first = 10, second = 23 and third = 15 can be called latter during the remaining of the script

Ex14:
prompt: 
print "Where do you live %s?" % user_name
lives = raw_input(variable) # the lives variable can be used latter

Ex15:
open(filename): Make a file available to python
.: dot operator to join a function (or command or method) to an object
filename.read(): Read the contents of the file
filename.close(): close the file so that it is no longer available to python

Ex16:
target = open(filename, 'w')
w: write mode
r: read mode
a: append mode
w+: write and read mode
r+: read and write mode
.truncate: delete the contents of file
.write: write information to file
pydoc import: for info on importing
;: semi-colon can separate commands on a single line
len(): command that returns the length of a string

Ex17:
os.path: a library that adapts the file/directory
addressing to the specific requirements of the operating system
example:
from os.path import exists  # exists is another command
exists: a function to determine whether a specific file exists; it yields a boolean True or False

Ex18:
def: to define custom functions
(*args): to refer to a list of arguments in a function (but
better to just list the arguments next to the function name)
: and indent: to set block for function
examples:
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
	
Ex19:

Ex20:
filename.seek(): go to a position within a particular file (in bytes)
.seek(0) goes to the beggining of the file
filename.readline(): reads one line from the file
+=: shortcut for incrementing a variable; += is a contraction for x = x + y

Ex21:
return: 
def add(a, b):
	print "ADDING %d + %d" % (a, b) # you actually don't need print anything for this to work.
	return a + b # return creates a value that is assigned to the variable that calls the function «add»



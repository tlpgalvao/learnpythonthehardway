#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from sys import argv
from os.path import exists  # exists is another command
# the 'import' imports other code that other programmers have written

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read() # to reduce you do: indata = open(from_file).read()
# If you reduce with = open().read() you don't need to close: take out «infile(close)» at the end

print "The input file is %d bytes long" % len(indata) # len() returns the size of the file as a number

print "Does the output file exist? %r" % exists(to_file) # tries to see if the file «to_file» already exists
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata) # you can reduce this like the one above

print "Alright, all done."

out_file.close()
in_file.close()
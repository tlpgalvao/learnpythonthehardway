#-*-coding:utf8;-*-
#qpy:2
#qpy:console

# Symbols

# and
# Logical and
# True and False == False

# as
# Part of the  with-as statement
# with X as Y: pass

# assert
# Assert (ensure) that something is true
# assert False, "Error!"

# break
# Stop this loop right now
# while True: break

# class
# Define a class.
# class Person(object)

# continue
# Don't process more of the loop, do it again
# while True: continue

# def
# Define a function
# def X(): pass

# del
# Delete from dictionary
# del X[Y]

# elif
# Else if condition
# if: X; elif: Y; else: J

# else
# Else condition
# if: X; elif: Y; else: J

# except
# if an exception happens, do this
# except ValueError, e: print e

# exec
# Run a string as Python
# except exec 'print "hello"'

# finally
# Exceptions or not, finally do this no matter what
# finally: pass

# for
# loop over a collection of things
# for X in Y: pass

# from
# Importing specific parts of a module
# import X from Y

# global
# Declare that you want a global variable
# global X

# if
# if condition
# if: X; elif: Y; else: J

# import
# import a module into this one to use
# import os

# in
# part of for-loops. Also a test of X in Y
# for X in Y: pass
# 1 in [1] == True

# is
# Like == to test equality
# 1 is 1 == True

# lambda
# create a short anonymous function
# s = lambda y: y ** y; s(3)

# not
# logical not
# not True == False

# or
# logical or
# True or False == true

# pass
# this block is empty
# def empty(): pass

# print
# print this string
# print 'this string'

# raise
# Raise an excption when things go wrong
# raise ValueError("No")

# return
# Exit function with a return values
# def X(); Return y

# try
# try this block, and if exeption, go to except
# try: pass

# while
# while loop
# while X: pass

# with
# with an expression as a variable do
# with X as Y: pass

# yield
# pause here and return to caller
# def X(): yield Y; X().next()

# Data types

# True
# True boolean values
# True or False == True

# False
# False boolean values
# False and True == False

# None
# represents "nothing" or "no value"
# x = None

# strings
# stores textual information
# x = "hello"

# numbers
# stores integers
# i = 100

# floats
# stores decimals
# i = 10.389

# lists
# stores a list of things
# j = [1,2,3,4]

# dicts
# stores a key=value mapping of things
# e = {'x': 1, 'y': 2}

# String Escape Sequences

# \\
# backslash

# \' 
# single-quote

# \"
# double-quote

# \a
# bell

# \b
# backspace

# \f
# formfeed

# \n
# newline

# \r
# carriage

# \t
# tab

# \v
# vertical tab

# String formats

# %d
# decimal integers (not floating point)
# "%d" % 45 == '45'

# %id
# same as %d
# "%i" % 45 == '45'

# %o
# octal number
# "%o" % 1000 == '1750'

# %u
# unsigned decimal
# "%u" % 1000 == '-1000'

# %x
# hexadecimal lowercase
# "%x" % 1000 == '3e8'

# %X
# hexadecimal uppercase
# "%X" % 1000 == '3E8'

# %e
# Exponential notation, uppercase 'e'
# "%e" % 1000 == '1.000000E+03'

# %E
# Exponential notation, uppercase 'E'
# "%E" % 1000 == '1.000000E+03'

# %f
# floating point real number
# "%f" % 10.34 == '10.340000'

# %F
# same as %f
# "%F" % 10.34 == '10.340000'

# %g
# either %f or %e, whichever is shorter
# "%g" % 10.34 == '10.34'

# %G
# same as %g but uppercase
# "%G" % 10.34 == '10.34'

# %c
# character format
# "%c" % 34 == '"'

# %r
# repr format (debugging format)
# "%r" % int == "<type'int'>"

# %s
# string format
# "%s there" % 'hi' == 'hi there'

# %%
# a percent sign
# "%g%%" % 10.34 == '10.34%'

# +
# addition
# 2 + 4 == 6

# -
# subtration
# 2-4 == -2

# *
# multiplication
# 2 * 4 == 8

# **
# power of
# 2 ** 4 == 16

# /
# division
# 2 / 4.0 == 0.5

# //
# floor division
# 2 // 4.0 == 0.0

# %
# string interpolate or modulus
# 2 % 4 == 2

# <
# less than
# 4 < 4 == False

# >
# greater than
# 4 > 4 == False

# <=
# less than equal
# 4 <= 4 == True

# >=
# greater than equal
# 4 >= 4 == True

# ==
# equal
# 4 == 5 == False

# !=
# not equal
# 4 != 5 == True

# <>
# not equal
# 4 <> 5 == True

# ()
# parenthesis
# len('hi') == 2

# []
# list brackets
# [1,2,3]

# {}
# dict curly braces
# {'x': 5, 'y': 10}

# @
# at (decorators)
# @classmethod

# ,
# comma
# range(0, 10)

# :
# colon
# def X():

# .
# dot
# self.x = 10

# =
# assign equal
# x = 10

# ;
# semi-colon
# print "hi"; print "there"

# x=
# add and assign
# x = 1; x += 2

# -=
# subtract and assign
# x = 1; x -= 2

# *=
# multiply and assign
# x = 1; x *= 2

# /=
# divide and assign
# x = 1; x /= 2

# //=
# floor divide and assign
# x = 1; x //= 2

# %=
# modulus assign
# x = 1; x %= 2

# **=
# power assign
# x = 1; x **= 2
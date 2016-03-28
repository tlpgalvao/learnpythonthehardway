#-*-coding:utf8;-*-
#qpy:2
#qpy:console

tabby_cat = "\tI'm tabbed in." # \t is like tab on the keyboard
persian_cat = "I'm split\non a line." # \n is a line 
backslash_cat = "I'm \\ a \\ cat." # \\ results in one \

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# """ Allows to write multiple lines 
# \t produces a tab
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

backslash = "backslash \\"
print backslash

single_quote = "single-quote \'"
print single_quote

double_quote = "double-quote \""
print double_quote

ASCII_bell = "ASCII bell \a"
print ASCII_bell

ASCII_backspace = "ASCII backspace \b"
print ASCII_backspace
 
ASCII_formfeed = "ASCII formfeed \f"
print ASCII_formfeed

ASCII_linefeed = "ASCII linefeed \n"
print ASCII_linefeed

character_named_name_unicode = "character named name in unicode \N{name}"
print character_named_name_unicode

carriage_return = "carriage return \r ASCII"
print carriage_return

horizontal_tab = "horizontal tab \t ASCII"
print horizontal_tab

character_16_bit = "character 16 bit \uxxxx"
print "%r" % character_16_bit
print "%s" % character_16_bit

# how does unicode work?

character_32_bit = "character 32 bit \uxxxxxxxx"
print character_32_bit

ASCII_vertical_tab = "ASCII vertical tab \v"
print ASCII_vertical_tab

character_octal_value = "character with octal value ooo \ooo"
print character_octal_value

# character_hex_value = "character with hex value hh \xhh"
# print character_hex_value

# why doesn't this work?

# new piece of code
# while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,
		









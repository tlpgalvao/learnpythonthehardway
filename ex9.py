#-*-coding:utf8;-*-
#qpy:2
#qpy:console

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # the \n don't work with %r; but work with %s

print "Here are the days: ", days # «print "Here are the days: %s" % days» and «print "Here are the days: %r" % days» also work; don't forget to take out the coma
print "Here are the months: ", months # «print "Here are the months: %s" % months» also work; «print "Here are the months: %r" % months» doesn't work

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" # " " " doesn't work, you can't leave any spaces
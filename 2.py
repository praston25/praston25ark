import sys
import re

string = input()
pattern = re.compile('^[a-z0-9._!]{0,12}')
x = bool(pattern.match(string))
print (x)

exit()

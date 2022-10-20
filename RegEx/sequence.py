# metacharacter

import re

txt = "hello planet"

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

a = re.findall("he.*o", txt)
print(a)

# Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

b = re.findall("he.+o", txt)
print(b)

# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

c = re.findall("he.?o", txt)
print(c)

# This time we got no match, because there were not zero, not one,
# but two characters between "he" and the "o"

# Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

d = re.findall("he.{2}o", txt)
print(d)

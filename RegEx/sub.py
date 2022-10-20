# metacharacter

import re

# Replace all white-space characters with the digit "$":

txt = "The rain in Spain"
x = re.sub("\s", "$", txt)
print(x)

# Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "$", txt, 2)
print(x)

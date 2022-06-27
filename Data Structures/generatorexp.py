# To generate a large amount of data, it might takes a lot of memories
# In this case, we have to use from ... import ...
# output will show the number of bytes memory takes

from sys import getsizeof

values = (x * 2 for x in range(100000))
print("Gen:", getsizeof(values))    # Tuple takes few bytes
values = [x * 2 for x in range(100000)]
print("List:", getsizeof(values))   # List takes a lot of bytes

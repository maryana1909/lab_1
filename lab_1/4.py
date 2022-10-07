import math
import random
str = kort = tuple([random.randint(0, 9) for _ in range(10)])

print(str)
clovar={i:str.count(i) for i in str}
print(clovar)
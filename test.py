import math

sum = 0
for i in range(0, 361):
    sum += math.cos(math.pi * i / 180)
    
print(sum) 
print(math.cos(math.pi / 2))
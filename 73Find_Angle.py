import math
AB = int(input())
BC = int(input())
angle = math.degrees(math.atan2(AB,BC))
degree = int(round(angle))
print(str(degree)+ '\u00B0')

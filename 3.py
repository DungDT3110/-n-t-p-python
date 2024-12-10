import math
a, b, c = map(int, input().split())
delta = b * b - 4 * a * c
if delta > 0:
   x1 = (-b + math.sqrt(delta))/(2 * a)
   x2 = (-b - math.sqrt(delta))/(2 * a)
   print(f"x1 = {x1}, x2 = {x2}")
elif delta == 0:
   x = - b / (2 * a)
   print(f"x = {x}")
else:
   print("VN")


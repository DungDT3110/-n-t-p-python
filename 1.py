a, b = map(int, input().split())
if a != 0:
   x = - b / a
   print(f"{x}")
elif b == 0:
   print("VSN")
else:
   print("VN")

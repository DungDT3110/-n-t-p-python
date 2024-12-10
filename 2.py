a, b = map(int, input().split())
if a > 0:
   print(f"x > - {b} / {a}")
elif a < 0:
   print(f"x < - {b} / {a}")
else:
   if b > 0:
       print("VN")
   else:
       print("VSN")

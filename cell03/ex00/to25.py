#!/usr/bin/env python3
n = input("Enter a number less than 25: ")
n = int(n)
if n > 25:
  print("Error")
else:
    while n <= 25:
     print(f"Inside the loop. my variable is {n}")
     n += 1

#!/usr/bin/env python3
a = 0
while a <= 10:
    print(f"Table de {a}:", end=" ")
    b = 0
    while b <= 10:
        print(a * b, end=" ")
        b += 1
    print()
    a += 1

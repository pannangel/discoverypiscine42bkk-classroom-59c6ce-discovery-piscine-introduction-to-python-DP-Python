#!/usr/bin/env python3
import sys
if len(sys.argv) != 3:  
    print("none")
else:
    try:
        start = int(sys.argv[1])  
        end = int(sys.argv[2])    
        result = []
        for i in range(start, end + 1):
            result.append(i)
        print(result)
    except ValueError:
        print("none")
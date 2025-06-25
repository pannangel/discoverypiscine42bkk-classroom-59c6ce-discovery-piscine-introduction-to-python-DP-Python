from numpy import array
a = array([2, 8, 9, 48, 8, 22, -12, 2])
if (a > 5).any(): 
    b = a[a > 5] + 2         
    c = set(b.tolist())      
    print(a)
    print(c)
else:
    print("error")

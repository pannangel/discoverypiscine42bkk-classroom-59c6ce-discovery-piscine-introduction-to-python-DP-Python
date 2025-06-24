first_num = int(input("Enter the first number: "))
sec_num = int(input("Enter the sec number: "))
mult = first_num * sec_num
print(f"{first_num} * {sec_num} = {mult}")
if mult > 0 :
    print("The result is postive")
elif mult < 0 :
    print ("The result is negative")
else:
    print("The result is zero")

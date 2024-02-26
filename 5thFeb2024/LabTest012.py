#Take the 2 numbers from user and add it as sum
#Step 1 = input
#Step 2 = sum

num1 = input("Enter the 1st number")
num2 = input("Enter the 2nd number")
print(num1)
print(num2)
print(type(num1))
#It returns the type as 'str'

num3 = int(num1) + int(num2)
print(num3)
print(type(num3))

#The above sum will be printed combination of both strings like str + str -> concatenation will happen
#num3 = num1 + num2
#To avoid the above problem we need to use int()


num4 = int(input("Enter the 1st number"))
num5 = int(input("Enter the 1st number"))
print(num4)
print(num5)
print(type(num4))
num6 = num4 + num5
print(num6)
print(type(num6))

#above here we will use int() while taking input fromm the user which will be considered as integer

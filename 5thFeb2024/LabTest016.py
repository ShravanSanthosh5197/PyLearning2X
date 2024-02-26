name = "ShraavanSanthosh"
print(len(name))#Length output starts with 1
print(name[5])
print(name[10])
print(name[15])
#print(name[17])#Index Error : string index out of range
print(len(name)-1)
print(name[len(name)-1])

#String - Immutability
#That can't be changed can be modified
String = "Hello"
print(String)
#String[0] = "P" TypeError: 'str' object does not support item assignment

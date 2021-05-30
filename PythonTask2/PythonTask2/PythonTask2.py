string1 = "This is a string."
string2 = " This is another string."
string3 = string1+string2
print(string3)
print(len(string3))
print(string3.lower())
print(string3.upper())
print(string3.title())
print(string3.strip('.'))
d = "qwerty"
ch = d[2]
print(ch)
string4= string3[1:3]
print(string4)
str5=string3[1:] 
str6=string3[:3] 
str7=string3[:]
str8=string3[1:5:2]
print(str5, str6,str7,str8)
a=4
b=5.5
c=a/b
d=b**a
f=b%2
print(c, d,f)
param = "string" + str(15)
print(param)
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)
a = 1/3
print("{:7.3f}".format(a))
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))
list1 = [82,8,23,97,92,44,17,39,11,12]
dir(list1)
#help(list1)

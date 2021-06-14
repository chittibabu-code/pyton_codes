a=1224.9
print(type(a),a)

b=bool(a)
print(type(b),b)

#binary

a=20
print(bin(a))

b='250'

print(int(b,base=10))
print(int(b,base=2))
print(int(b,base=8))
print(int(b,base=16))

name=input('Enter your name')

age=int(input('Enter your age'-2021))

print(name,age)

#operators

a,b=50,20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#comparsions

a,b=50,20
print("a<b:{}".format(a<b))
print("a<b:{}".format(a>b))
print("a<b:{}".format(a<=b))
print("a<b:{}".format(a>=b))
print("a<b:{}".format(a==b))
print("a<b:{}".format(a!=b))

#logicaloperators

a,b=True,False
print("a and b:{}".format(a and b))
print("a and b:{}".format(a not b))
print("a and b:{}".format(a or b))

a,b=25,30
c=a>b and not(a==b)
print(not(c) or a<b)

#assignmentoperators
a=10
a=a+1

print(a)
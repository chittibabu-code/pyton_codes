
#range
lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
for n in range (lower,upper+1):
    if(n%5==0 and n%7==0):
        print(i)




# sum of series
# 2+22+222, ..
import math
 
def sumOfSeries( n ):
    return 0.0246 * (math.pow(10, n) - 1 - (9 * n))

n = 3
print( sumOfSeries(n))

#entercharacher

summ = 0
count = 1
while raw_input("Enter q to quit or any other key to continue") != 'q':
    summ = summ+input()
    count=count+1
print summ/(count*1.0)



#factorial


num = int(input("enter a number: "))
 
fac = 1
i = 1
 
while i <= num:
fac = fac * i
i = i + 1
 
print("factorial of ", num, " is ", fac)


st = 'python is a good programming language'

for i in range(len(st)):
	end_val = '-'
	if st[i] == ' ':
		end_val = '\n'
	if i == len(st)-1:
		end_val = ''
	elif st[i+1] == ' ':
		end_val = ''

	if i%2 == 0:
		print(st[i].upper(), end=end_val)
	else:
		print(st[i].lower(), end=end_val)
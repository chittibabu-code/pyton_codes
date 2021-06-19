#list of numbers


def createList(r1, r2):
    return [item for item in range(r1, r2+1)]
      
r1, r2 = -1, 1
print(createList(r1, r2))

#count of odd and even numbers

list1 = [10, 21, 4, 45, 66, 93, 1]
  
even_count, odd_count = 0, 0
  
# iterating each number in list
for num in list1:
      
    # checking condition
    if num % 2 == 0:
        even_count += 1
  
    else:
        odd_count += 1
          
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)





#min and max

minimum = []
maximum = []

# Defining Stack Class
class Stack:
    def __init__(self) :
        self.items = []

    def push(self, item) :
        self.items.append(item)

    def pop(self) :
        return self.items.pop()

    def access(self, index):
        return self.items[index]

    def isEmpty(self) :
        return (self.items == [])

    def length(self):
        return len(self.items)

def minmax(input_list):
    # make two stacks, one for min and one for max
    min_stack = Stack()
    max_stack = Stack()
    # comparing the first two elements of the list and putting them in appropriate stack
    if input_list[0]<input_list[1]:
        min_stack.push(input_list[0])
        max_stack.push(input_list[1])
    else:
        max_stack.push(input_list[0])
        min_stack.push(input_list[1])

    # Pushing remaining elements of the list into appropriate stacks. 
    for i in range(2, len(input_list)):
        if input_list[i] < min_stack.access(-1):
            min_stack.push(input_list[i])
        else:
            max_stack.push(input_list[i])

    # to find minimum
    minlist = []
    while min_stack.length() > 0:
        minlist.append(min_stack.pop())

    # to find maximum
    maxlist = []
    while max_stack.length() > 0:
        maxlist.append(max_stack.pop())

    if len(minlist) > 1:
        minmax(minlist)
    else:
        minimum.append(minlist)


    if len(maxlist) > 1:
        minmax(maxlist)
    else:
        maximum.append(maxlist)

def main():
    input_list = [2, 0, 2, 7, 5, -1, -2]
    print 'Input List is: ', input_list
    minmax(input_list)

print 'Global Minimum is: ', minimum[0]
print 'Global Maximum is: ', maximum[len(maximum)-1]

if __name__ == "__main__":
    main()








    #pallidrom or not

    number=int(input("Enter any number :"))
#store a copy of this number
temp=number
#calculate reverse of this number
reverse_num=0
while(number>0):
    #extract last digit of this number
    digit=number%10
    #append this digit in reveresed number
    reverse_num=reverse_num*10+digit
    #floor divide the number leave out the last digit from number
    number=number//10
#compare reverse to original number
if(temp==reverse_num):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


    


    #print pallindrome numbers

    def palindromeNumbers(list_a): 
  
    c = 0
  
    # loop till list is not empty 
    for i in list_a:             
  
        # Find reverse of current number 
        t = i 
        rev = 0
        while t > 0: 
            rev = rev * 10 + t % 10
            t = t // 10
  
        # compare rev with the current number 
        if rev == i: 
            print (i) 
            c = c + 1
  
    print()
    print ("Total palindrome nos. are", c )
    print()
  
# Driver code 
def main(): 
  
    list_a = [10, 121, 133, 155, 141, 252] 
    palindromeNumbers(list_a) 
  
    list_b = [ 111, 220, 784, 565, 498, 787, 363] 
    palindromeNumbers(list_b)                     
  
if __name__=="__main__": 
    main()   
def pyramid(word):
    l = 0
    while l < len(word):
        l += 1
        print(word[:l])
        word = word[l:]
    if word:
        print(word + "*" * (l - len(word) + 1))
pyramid('abcdefghhhhhhhhhhhhh')

n=int(input("enter num="))
temp=n
rev=0
while(n>0):
    s=n%10
    rev=rev*10+s
    n=n//10
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")

n=int(input("entre number"))
temp=n
rev=0
while(n>0):
    s=n%10
    rev=rev*10+s
    n=n//10
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")    
    
    
    
    
    
    
    

    
    import math
m= matrix('1 2,3 4,5 6')
print(m)

print(17//10)

a="abcdef" >="abcd"
print(a)


num=int(input("enter number:"))
num=0
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
    else:
        print("prime")
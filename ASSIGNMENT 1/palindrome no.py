n=int(input("Enter a number: "))
temp=n
pal=0
while(n>0):
    digit=n%10
    pal=pal*10+digit
    n=n//10
if(temp==pal):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
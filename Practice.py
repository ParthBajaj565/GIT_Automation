a="5"
print (int(a))

x = "Parth Bajaj"
print(x.split(" "))


y= "parth"[::-1]     #reverse a string
print(y)

z=[2,3,1]
z.sort()          #sort a list
print(z)

z.reverse()      #reverse an array
print(z)

z.remove(2)
print(z)


b=int(input("Enter a number"))
for i in range(2, b):
    if b%i==0:
        print("not prime")
        break
else:
    print("prime")



c=int(input("Enter a number"))   #factoriaL
f=1
for i in range(1,c+1):
    f=f*i

print(f)


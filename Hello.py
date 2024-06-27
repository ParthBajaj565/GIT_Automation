print("Hello")
x="Rohan"
x="Parth"
y=x *  2
print(y)

Name = "Lux"
z= "Hello", Name
print(z)

#a= input("name")
#print(a)

l=[1,2,3]     #List  - you can add, modify, delete and duplicate it
t=(4,5,6)     #Tuple - You cannot modify, add or delete from it
s={7,8,9}     #Sets  - you can add and remove elements but you cannot duplicate it, sets doesn't have orders
l.append("Hello")     #to add an element at the end
l.remove(1)
s.add("World")     #It can add anywhere because sets does not have order
print(l)
print(t[0])
print(s)

b={"Rohan", "Sohan", "Mohan"}
c={"Rohan", "Sohan", "Roshan"}
d=b.difference(c)
e=b.intersection(c)
print(d,e)

print(5==5)        #Comparison, it checks if they are exactly same
d={"Parth" : 26, "Adyy" : 26, "Jatin" : 20}        #Dictionaries has keys and values. Keys can only be string and values can only be numbers
print(d["Parth"])

destructure = ("Parth", 26, "Bajaj")              #destructuring
First_Name, age , Last_Name = destructure
print(First_Name, age , Last_Name)

head, *tail=[1,2,3,4,5,6]    #head for collecting starting number, tail for collecting end numbers
print(head)
print(tail)
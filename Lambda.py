fun = lambda x,y:x+y
sun = lambda a,b:a-b

print(fun(10,9))
print(sun(15,8))


q,w,e = 1,2,"Parth"

print("value is", w)

print(type(q))

values=[1,2,3,"Parth",4]
values.insert(4,"Bajaj")
print(values)

dict={}
dict[1] = "Parth"
dict["Bajaj"] = 2

print(dict)
sun =0
for i in range(1,6):
    sun = sun +i
print(sun)

print("**********************")
it = 10
while it>1:
    if it ==9:
        it = it-1
        continue
    if it ==3:
        break
    print(it)
    it=it-1

    str = "Parth"
    str1 = "Bajaj"

    print(str, str1)

    v= str.split("r")
    print(v)
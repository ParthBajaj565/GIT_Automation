x=5
y=0

try:                            #try to execute it
    print("open")
    print(x/y)
except Exception as e:         #if it is not executable, use except
    print("You cannot divide", e)
finally:                       #if exception is there or not, finally statement will print
    print("Close")


order = 0
#if order !=2:
    #raise Exception("not done")

assert(order==2)
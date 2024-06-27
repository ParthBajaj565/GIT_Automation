class sum:
    def addition(self,x,y):
        result = x+y
        print(result)

a=sum()

a.addition(7,8)

class computer:
    def __init__(self,b,c):
        self.b = b
        self.c = c
        print(self.b + self.c)

com1 = computer(5,7)

#def __str__(self):       easy to print Any string, to turn object into string
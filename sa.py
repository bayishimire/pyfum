class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def Area(self):
        print(f"area is {self.length*self.width} unit")
    def perimeter(self):
         print(f"perimeter is :${2*(self.length+self.width)} units")
number1=int(input("enter numberone:"))
number2=int(input("enter numberone:"))
obj=Rectangle(number1,number2)
obj.Area()
obj.perimeter()

class Rectangle:
    def getData(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        print( a)
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print(p)
ch=0
l=int(input("enter the length"))
b=int(input("enter the breadth"))
obj=Rectangle()
obj.getData(l,b)
while ch!=3:
    print("1.area")
    print("2.perimeter")
    print("3.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        obj.area()
    if ch==2:
        obj.perimeter()
    else:
        print("end")


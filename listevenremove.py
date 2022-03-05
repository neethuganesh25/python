num1=input(" enter the list(space seperated:)")
num=list(map(int,num1.split()))
num=[x for x in num if x%2!=0]
print("list afer removing even  numbers",end="")
print(num)

n=int(input("enter the step sixe"))
for i in range(1,n+1):
    k=i
    for j in range(1,i+1):
        print(k,end='')
        k+=i
    print()

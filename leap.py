print("leap years")
s=int(input("enter start year"))
r=int(input("enter end yer"))
for year in range(s,r):
    if(0==year%4)and(0!=year%180):
        print(year)

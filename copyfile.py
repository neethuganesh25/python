file1=input("enter the source fileto be copied")
file2=input("enter the destination file")
fr=open(file1,"r")
fw=opem(file2,"w")
for line in fr.readlines():
    fw.write(line)
fr.close()
fw.close()
print("1 file copied")

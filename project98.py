def swapFileData():
    file1 = input("enter file 1 name = ")
    file2 = input("enter file 2 name=")

    with open(file1,"r") as a:
        dataA = a.read() 
    with open(file2,"r") as b:
        dataB = b.read()
    with open(file1,"w") as a:
        a.write(dataB)
    with open(file2,"w") as b:
        b.write(dataA)
swapFileData()

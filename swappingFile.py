def swipeFileData ():
    fileName1 = input("Enter name of the 1st file to swap: ")
    fileName2 = input("Enter name of the 2nd file to swap: ")


with open(fileName1, 'r')  as a:
    data_a = a.read()  

with open(fileName2, 'r')  as b:
    data_b = b.read()      
    
with open(fileName1, 'w') as a:
    a.write(data_b)
    
with open(fileName2, 'w') as b:
    b.write(data_a)

swipeFileData()
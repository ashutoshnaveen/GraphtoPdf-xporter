import os
from time import sleep
def clr():
    os.system("cls")
def tdg():
    a=int(input("Number of different graphs: \n"))
    b=int(input("Number of graphs of single type: \n"))

    X=[]
    Y=[]
    f=open('test2.txt','w')
    f.write('')
    for i in range(a):
        for j in range(b):
            x=map(str,str(input("")).strip().split())
            y=map(str,str(input("")).strip().split())
            f.write(' '.join(x)+'\n')
            X.append(x)
            Y.append(y)
            f.write(' '.join(y)+'\n')
            
    f.close()
    return X,Y
def functionality():
    clr()
    a=ord(input("would you like to enter data in text file: "))
    if a==98 or a==121:
        text_flag=True
        clr()
        return text_flag
    else:
        if a==110 or a==78:
            text_flag=False
            return text_flag
        else:
            print("\t\t\t\tWrong Input!\n\t\t\t\tTry again")
            sleep(0.5)
            functionality()


        
    
    
    

#calculator using if-else 

print("1.Addition\n2.subtrction\n3.multification\n4.divition\n5.module[%]\n6.Exponential(**)\n7.Floor Division(//)")
x=int(input("Enter you choose from following:-"))
y=int(input("Enter first number:"))
z=int(input("Enter second number:"))

if(x==1):
    print("Addition of tow numbres is :",y+z)
elif(x==2):
    print("Subtrction of tow numbres is :",y-z)
elif(x==3):
    print("Multification of tow numbres is :",y*z)
elif(x==4):
    print("Division of tow numbres is :",y/z)
elif(x==5):
    print("Modul of tow numbres is :",y%z)    
elif(x==6):
    print("Exponential of tow numbres is :",y**z)
elif(x==7):
    print("Floor Division of tow numbres is :",y//z)
else:
    print("Enter valid choose FIRST !!!")    

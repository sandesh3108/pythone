x=int(input("Enter the marks of 'DS' out of 25: "))
y=int(input("Enter the marks of 'AT' out of 25: "))
z=int(input("Enter the marks of 'CN' out of 25: "))
w=int(input("Enter the marks of 'DSM' out of 25: "))
t=x+y+z+w
print("Total marks out of 100 is: ",t)

# <,>,==,!=,<=,>= are the conditional opretors

if(t>=90 and t<=100):                  #if more then one condition is present in one if stetment then we use "and"
    print("you pass the exam with \'A' class")
elif(t>=80 and t<90):                  #if more then tow condition is present then we use "elif"  
    print("you pass the exam with \'B' class")
elif(t>=70 and t<80):
    print("you pass the exam with \'C' class")
elif(t>=60 and t<70):
    print("you pass the exam with \'C-' class")
elif(t>=50 and t<60):
    print("you pass the exam with \'D' class")        
elif(t>=40 and t<50):
    print("you pass the exam with \'D-' class")        
else:
    print("you are FAIL in exam...!")
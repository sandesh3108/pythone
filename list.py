l=[1,2,3,4,5,6]  #list 1st
print(l)
print(l[::2])
lm=[i+i for i in range(10) if i%2==0] #list 2nd
print(lm)

m=[1,2,"ram",True]  #list 3rd
print(m)
if "ram" in m:
    print(True)
else:
    print(False)

s=[5,66,3,9,0,5,1,2]
print("unsorted list=",s)
s.sort() #this function is used to sort the list 
print("sorted list=",s)
s.sort(reverse=True)
print("sorted list 2nd=",s)

s.reverse()  #this functon is used to reverse the list
print("reverse the 2nd list",s)

print("how many time element 5 comes in list",s.count(5))

a=s.copy() #this function copy the list without changing the list 
a[1]=10
print("a=",a)
print("s=",s)

a.insert(2,20)
print("a after insert 20 in 2nd index=",a)

s.extend(l)  #this function combine 2 list 
print(s)
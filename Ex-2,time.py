import time                
#"import time" this is used to import cruut time in progrme
# "time.strftimeS(%H)" is used to import hours 
# "time.strftime(%M)" is used to import minitue
# "time.strftime(%S)" is used to import sec

t=time.strftime("%H:%M:%S")
print("Time=",t)
h=float(time.strftime("%H"))
print(h)
if(h>=5 and h<12):
    print("Good Morning To All")
elif(h>=12 and h<=18):
    print("Good Afternoon To All")
else:
     print("Good Evening To All")
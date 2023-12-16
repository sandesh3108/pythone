a="sandeshpatil"
b=''' 
      sam:hi,
      suny:hello
      sam:how are you?
      suny:I'm fine,what about you?
      sam:I'm also fine'''

print("string a is :",a,"\nstring b is :",b)
print("\nstring a is divide in parts:" ,a[0:7],a[7:12]) #it consider "0" but dose not "7" in first part 
print("\nLength of string a is :",len(a)) #len() this function is used to find the length of string
print("\nLength of string b is :",len(b)) 
print("\nstring a is printed using negation sing:",a[-5:12]) 
#"-5"means it substrct 5 from lenth of string(12-5=7 string print from index 7)
print("________________________________________________")
print("STRING METHODES GIVEN BELOW:-")

x="python"
y="JAVA"
z="coding!!!"
w="my name is ram."

print("\nMain strins are:\n\nx=",x,"\ny=",y,"\nz=",z,"\nw=",w)

print("\n1.string to upper case=",x.upper()) #this covet variable to upper case
print("2.string to lower case=",y.lower()) #this covet variable to lower case
print("3.! removed from string z=",z.rstrip("!")) #this remove a particuler variable from end
print("4.p is replaced by s from string x=",x.replace("p","s")) #this replace a particuler variable to other
print("5.spilt string w from space =",w.split(" ")) #this separet a string fome a particuler part
print("6.corret the string =",x.capitalize()) #p is capitalazed because it is first letter of line
print("7.string is centered=",y.center(50)) #give the space bar in star & end of string
print("8.check the string z is ending with !=",z.endswith("!"))
print("9.Find the index of\'is'=",w.find("is"))
#index() is same as find
print("10.check string y contain only alphbet or number=",y.isalnum())
print("11.check string y contain only alphbet =",y.isalpha())
print("12.string x contain only lower case=",x.islower())
print("13.string y contain only upper case=",y.isupper())
print("14.string z contain only printable charector(not like blacklash n or etc)=",z.isprintable())
print("15.string w contain white space=",w.isspace())#this function give True only when string contain space 
print("16.string w contain first letter as upper case=",w.istitle())
print("17.check start of string z is from c or not=",z.startswith("c"))
print("18.chang the caseting of all variable=",w.swapcase())
print("19.covert the first letter of each word to upper case=",w.title())
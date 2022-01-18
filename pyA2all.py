#Deepak Gupta
#21103086
#Assignment 2

inject=''
#ques1
print("Question 1:")
string="Python is a case sensitive language" 
#a part
print("Length of string =",len(string))
#b part
print("String after reversing the order :",string[35::-1])
#c part
slice_str=string[10:26]
print("Sliced string :",slice_str)
#d part
new_string = string.replace("a case sensitive","object oriented")
print("New String :",new_string)
#e part
print("Index of given substring =",string.index("a"))
#f part
print("String after removal of white spaces :",string.replace(" ",""))

#----------------------------------------------------------
#ques2
print("\nQuestion 2:")
name = "Deepak Gupta"
SID = 21103086
CGPA = 10
deptt = "CSE"
print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %.1f"%(deptt,CGPA))

#----------------------------------------------------------
#ques3
print("\nQuestion 3:")
a=56
b=10
#a part
print("a&b =",a&b)
#b part
print("a|b =",a|b)
#c part
print("a^b =",a^b)
#d part
print("a<<2 =",a<<2,"and b<<2 =",b<<2)
#e part
print("a>>2 =",a>>2,"and b>>4 =",b>>4)

#--------------------------------------------------------
#ques4
print("\nQuestion 4:")
A=float(input("Enter 1st number : "))
B=float(input("Enter 2nd number : "))
C=float(input("Enter 3rd number : "))
if(A>B):
    if(A>C):
        print(A,"is the largest number")
    else:
        print(C,"is the largest number")
else:
    if(B>C):
        print(B,"is the largest number")
    else:
        print(C,"is the largest number")

#--------------------------------------------------------
#ques5
print("\nQuestion 5:")
string=input("Input you string : ")
if("name" in string):
    print("Yes")
else:
    print("No")

#--------------------------------------------------------
#ques6
print("\nQuestion 6:")
s1=int(input("Enter 1st side : ")) 
s2=int(input("Enter 2nd side : "))
s3=int(input("Enter 3rd side : "))

if((s1>s1+s2)|(s2>s1+s3)|(s3>s1+s2)):
    print("No")
else:
    print("Yes")


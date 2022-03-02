#Assignment4

#ques1
#(Tower of Hanoi)
#we have 3 discs(of diff. size) in A peg(source) and transfer them to C peg(destination) one by one
#such that a larger disc should never be on top of smaller one(B is Auxiliay peg)

def tower_of_Hanoi(n,source,aux,dest):       #aux=auxiliary peg  dest=destination peg
    if(n>0):                                 #base condition is n=1(because after that n will be <0)
        tower_of_Hanoi(n-1,source,dest,aux)
        print("Tranfer disc %d from %s peg to %s peg"%(n,source,dest))
        tower_of_Hanoi(n-1,aux,source,dest)
    
tower_of_Hanoi(3,'A','B','C')
print("Transfer complete")
#---------------------------------------------------------------------
#ques2
#Pascal's triangle

from math import factorial

#using iteration
print("i)Using iteration : ")

#making nCr function
def nCr(n,r):
    x=factorial(n)/(factorial(n-r)*factorial(r))
    return int(x)    

row=int(input("Enter no. of rows : "))
i=1
while i<=row:
    print(" "*(row-i),end="")
    j=0
    while j<i:
        print(nCr(i-1,j),end=" ")
        j+=1
    print("")
    i+=1

#using recursion
print("\nii)Using recursion : ")
def pascals_triangle(n,s,m):
    if n==0:
        print(" "*(s-1),1)
        return pascals_triangle(n+1,s,m)
    elif n==m:
        print("Done!")
        n=-1  
    else:
        print(" "*(s-n),end="")
        x=0
        while x<=n:
            print(nCr(n,x),end=" ")
            x+=1
        print("")
        if n==m:
            print("Done!")
            n=-2
        return pascals_triangle(n+1,s,m)
    
        
m=int(input("Enter no. of rows : "))
n=0
s=m*2
pascals_triangle(n,s,m)

#-----------------------------------------------------------------------------
#ques3

int1=int(input("Enter first number : "))
int2=int(input("Enter second number : "))
Quotient = int1 // int2
Remainder = int1 % int2

#part(a)---------------------------------------------
print("a) Checking if the quotient and remainder is a callable value or not:")
print("Is Quotient is callable :",callable(Quotient))
print("Is Quotient is callable :",callable(Remainder))

#part(b)----------------------------------------------
if (Quotient == 0):
    print("b) Only quotient is zero")
if (Remainder == 0):
    print("b) Only reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("b) All the values are non zero")

#part(c)------------------------------------------------
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"c) Filtered out numbers that are greater than 4 are : {result}")

#part(d)------------------------------------------------
setresult = set(result)
print("d) Set : ",setresult)

#part(e)------------------------------------------------
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("e) Immutable set:",immutableSet)

#part(f)------------------------------------------------
print("f) Hash value of the max value from the above set:", hash(max(immutableSet)))

#------------------------------------------------------------------------------------
#ques4

class Student:
    def __init__(self,name,roll_no):    #constructor
        self.name = name
        self.roll_no = roll_no

    def print_details(self):
        print("Name of student is",self.name,"and Roll no. is",self.roll_no) 

    #deleting(destructor)
    def __del__(self):
        print("object deleted")

first=Student("Deepak",21103086)
second=Student("Pratham",21103099)
third=Student("Harsh",21103096)

first.print_details()
second.print_details()
third.print_details()

del first
del second
del third

#-----------------------------------------------------------------------------------
#ques5

class Employee:
    def __init__(self,name,salary):
        #self.serial_no =  serial_no
        self.name      =  name
        self.salary    =  salary

    def print_details(self):
        print("Name of Employee is",self.name,"and Salary is",self.salary) 

    def __del__(self):
        print("Data of %s is successfully deleted"%(self.name))

first=Employee("Mehak",40000)
second=Employee("Ashok",50000)
third=Employee("Viren",60000)

print("Details:")                          
first.print_details()
second.print_details()
third.print_details()

#a)part
first.salary = 70000
print("\na) Update salary of Mehak to 70000\nUpdated details:")
first.print_details()
second.print_details()
third.print_details()

#b)part
print("\nb) Delete data of Viren")
del third

#---------------------------------------------------------------------------------
#ques6

g_word =input("Enter the word said by George : ")
g_word=g_word.lower()
sorted_chars1=sorted(g_word)
g_word="".join(sorted_chars1)

b_word = input("Enter the word said by Barbie using the exact same letters : ")
b_word=b_word.lower()
sorted_chars2=sorted(b_word)
b_word="".join(sorted_chars2)

if(g_word==b_word):
    print("Friendship is real")
else:
    print("Friendship is fake")



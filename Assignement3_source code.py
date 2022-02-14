#Assignment-3
#ques1
string1=input("Enter a string :")
list1=[]
list2=string1.split()
d=dict()

if len(list2)==1:          #this is for 1 word
    for i in string1:      
        list1.append(i)
    for j in list1:        #all unique keysget value 1 and 
        if j in d:         #when a key repeats it increases value by 1
            d[j]=d[j]+1    
        else:
            d[j]=1
    print(d)        
else:
    for i in list2:        #this is for multiple words
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)
#-------------------------------------------------------------------------------
#ques2
day=int(input("Enter Day :"))
month=int(input("Enter Month :"))
year=int(input("Enter Year :"))

if(1800<=year<=2025):
    if(year%4!=0):
        dict={year:"not leap year"}
    elif(year%4==0):              #to check leap year
        if(year%100==0):
            if(year%400==0):      #to check if century year is leap year
                dict={year:"leap year"}
            else:
                dict={year:"not leap year"}
        else:
            dict={year:"leap year"}
else:
    print("*Error : not in range*")
        
if(month in[1,3,5,7,8,10,12]):
    if(1<=day<31):
        print("Next Date is: %d/%d/%d"%(day+1,month,year))
    elif(day==31):
        if(month==12):
            print("Next Date is: 0%d/0%d/%d"%(1,1,year+1))
        else:
            print("Next Date is: 0%d/%d/%d"%(1,month+1,year))
elif(month in[4,6,9,11]):
    if(1<=day<30):
        print("Next Date is: %d/%d/%d"%(day+1,month,year))
    elif(day==30):
        print("Next Date is: 0%d/%d/%d"%(1,month+1,year))
elif(month==2):                 #we have to check leap year only if month==2
    if(dict[year]=="leap year"):
        if(1<=day<29):
            print("Next Date is: %d/%d/%d"%(day+1,month,year))
        elif(day==29):
            print("Next Date is: 0%d/%d/%d"%(1,month+1,year))
    else:
        if(1<=day<28):
            print("Next Date is: %d/%d/%d"%(day+1,month,year))
        elif(day==28):
            print("Next Date is: 0%d/%d/%d"%(1,month+1,year))

#-------------------------------------------------------------------------------
#ques3
list1=[1,5,7,9,10,14]   #Initilisation of list
list_of_squares=[]

for i in list1:
    list_of_squares.append((i,i**2))
print(list_of_squares)

#-------------------------------------------------------------------------------
#ques4
dict1={4:('D','Poor'),5:('C','Below Average'),6:('C+','Average'),7:('B','Good'),8:('B+','Very Good'),9:('A','Excellent'),10:('A+','Outstanding')}
grade_pt=int(input("Enter Grade point :"))
if (grade_pt in range(4,11)):
       grade,perform=dict1[grade_pt]
       print("Your Grade is '%s' and %s Performance"%(grade,perform))
else:
    print("*Error : Entered Grade point not in range*")
    
#-------------------------------------------------------------------------------
#ques5
string="ABCDEFGHIJK"
i=len(string)
while(i>0):
    print(" "*((12-i)//2)+string[:i])   #here 12 is len(string)
    i=i-2
    
#-------------------------------------------------------------------------------
#ques6

student_info=dict()
n="Y"
sid_list=[]

while(n=='Y'):                      #It asks sid and names repeatedly and adds them to dictionary
    sid=int(input("Enter SID of the student :"))
    name=input("Enter name of the student :")
    student_info[sid]=name
    n=input("To enter more data press Y or press N to stop     ")
    sid_list.append((sid,name))

#(a)
print("\na)Dictionary with student details :\n",student_info)

#(b)---------------------------------------------
#to sort our dictionary based to names reverse the key value pair and we will form a list
#which can be sorted and converted back to dictionary hence we get the required dictionary

newdict=dict()                        #now we exchange the key value pair and make a new dictionary and a new list
name_list=[]

for (k,v) in student_info.items():    #k for key(SID here) and v for value(name here)
    newdict[v]=k
    name_list.append((v,k))           #exchanged the key value pair but its not sorted yet

name_list.sort()                      #to sort the list
sorted_dict_name=dict(name_list)      #create a sorted dictionary from sorted list

#now exchange the key value pair of the sorted_dict_name to get our required dictionary
required_dict_name=dict()
for (k,v) in sorted_dict_name.items():
    required_dict_name[v]=k
print("\nb) Dictionary sorted on the basis of name :\n",required_dict_name)

#(c)---------------------------------------------
#sort the dictionary on the basis of sid
#we will first sort the list and then convert it into dictionary 
sid_list.sort()
sorted_dict_sid=dict(sid_list)
print("\nc)Dictionary sorted on the basis of SID :\n",sorted_dict_sid)

#(d)---------------------------------------------
#search a student's Details by his/her SID       
searchSID=int(input("\nd) Enter SID of student you want to search :"))
if(searchSID in student_info):
    print("The name of the student with the entered SID is :",student_info[searchSID])    
else:
    print("Not found")

#-------------------------------------------------------------------------------
#ques7
#fibonacci sequence is {An}=0,1,1,2,3,5,8,13,.....
#i.e. n0=0,n1=1 and next all terms are sum of previous two

n=int(input("Enter the index(n>=2) upto which you want the fibonacci sequence :"))
n0=0;n1=1       #intialise n0=0,n1=1

f=[n0,n1]     
sum=n0+n1

print("Resultant Fibonacci sequence is : 0 1 ",end="")
for i in range(2,n+1):
    f.append(f[i-1]+f[i-2])
    sum = sum + f[i]
    print(f[i],"",end="")
print("\nAverage of this series = %.2f"%(sum/(n+1)))

#-------------------------------------------------------------------------------
#ques8
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

print("Set1 =",Set1);print("Set2 =",Set2);print("Set3 =",Set3)
#(a)-------------------------------
print("a)Elements that are in Set1 and Set2 but not in both :",end=" ")
new_Set = Set1^Set2
print(new_Set)
#(b)-------------------------------
print("b)Elements that are in only one of Set1,Set2 and Set3 :",end=" ")
new_Set = Set1^(Set2^Set3)
print(new_Set)
#(c)-------------------------------
print("c)Elements that are in exactly two of the sets Set1,Set2 and Set3 :",end=" ")
new_Set = (Set1&Set2)|(Set2&Set3)|(Set1&Set3)
print(new_Set)
#(d)-------------------------------
print("d)Integers that are in range 1 to 10 but not in Set1 :",end="\t")
Int_Set = {1,2,3,4,5,6,7,8,9,10}
new_Set = Int_Set-Set1
print(new_Set)
#(e)-------------------------------
print("e)Integers that are in range 1 to 10 but not in Set1,Set2 and Set3 :",end=" ")
new_Set = Int_Set-(Set1|Set2|Set3)
print(new_Set)

#-------------------------------------------completed-----------------------------------------------


    

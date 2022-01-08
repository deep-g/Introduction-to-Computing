#Question3: Prog to store different data type values into a list
#SOURCE CODE

name=input("Enter your Name : ")
sid=int(input("Enter Student Id : "))
gender=str(input("Enter your Gender : "))
course=input("Enter the name of your Course : ")
cgpa=float(input("Enter your CGPA : "))
print("")
print("*****STUDENT DATA*****")
student_data = [name , sid , gender , course , cgpa]
print(student_data)

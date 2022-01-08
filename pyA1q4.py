#Ques4: Make list of marks of 5 students and show them in sorted manner
std1_marks=float(input("Enter marks of 1st student : "))
std2_marks=float(input("Enter marks of 2nd student : "))
std3_marks=float(input("Enter marks of 3rd student : "))
std4_marks=float(input("Enter marks of 4th student : "))
std5_marks=float(input("Enter marks of 5th student : "))

marks_list=[std1_marks,std2_marks,std3_marks,std4_marks,std5_marks]
#sorting in decreasing order
marks_list.sort(reverse=True)
print("Sorted List:",marks_list)

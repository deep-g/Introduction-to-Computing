#Ques5:a)print a list and then remove 4th element from the list and let it print new list
      #b)remove'Black' and 'Pink' from the list and replace it with 'Purple'

my_list=['Red','Green','White','Black','Pink','Yellow']
#a)part
print(my_list)
#remove 4th term(i.e.Black)
my_list.remove('Black')
print("(a)=",my_list)

my_list=['Red','Green','White','Black','Pink','Yellow']
#b)part
print("\n",my_list)
#to replace nth term write my_list[n-1]='New Value'
my_list[3]='Purple'
my_list[4]='Purple'
print("(b)=",my_list)

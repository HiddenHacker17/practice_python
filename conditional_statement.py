#language=("java")
#if language == "python" :
#    print("ok it is true")
#elif language =="java":
 #   print("ok it is java")
#else :
 #   print("not ok")

    # we can also use and , or AND not operator in conditional statement
user = "Admin"
login=True
#if user =="Admin" or login:
#    print("welcome admin")
#else :
 #   print("Wrong info")
#if not login: # not give true to false and false to true
#    print("plese login")
#else:
 #   print("Welcome")    


list1= [1,2,3,4,5]
list2= [1,2,3,4,5]
#print(list1==list2) # this will give true bcz list1 and list2 have same value
print(list1 is list2) # this will give false bcz list1 and list2 are different object in memory
print(id(list1)) #for memory adress of a list in this case list 1
print(id(list2))

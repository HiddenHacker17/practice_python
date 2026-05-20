#functions are baisically some instructions which we can reuse again and again
#def fun():  # def stand for define and fun is the name of the function
    #pass # we cant leave a function completely empty so we use this pass keyword  #def stand for define and fun is the name of the function
    #print("hello World") #function body
 #   return "hello world" # we can also return some value from function

# fun()
# fun()
# fun()
#this is called DRY code which stands for dont repeat yourself
#it allows us to reuse the code again again and again without writting the same code again and again


#Executing  functions

#print(len("hello World"))
#print(fun().upper())

#def greet(name="Rishu",address = "noida"):
  #  return " Hello {}! from {}".format (name,address)
#3print (greet("Hidden","Delhi"))

#positional argument and keyword argument
#def student_info(*args,**kwargs):#*args is used to pass variable number of non keyword argument and **kwargs is used to pass variable number of keyword argument
   # print(args)  #this give a tuple
   # print(kwargs) #thus give a dictionary
#student_info("math","Arts","science",name="Rishu",age=20)
#courses = ['math', 'Arts', 'science'] 
#info={'name': 'Rishu', 'age': 20}
#student_info(*courses,**info) #this will unpack the tuple and dictionary and pass to the function as positional arg and keyword arg respectievly 



#Example

#numeber of days in months and first value is place holder for indexing purpose
months_days =[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap_year(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)
"""return true if the year is leap year and false if it is not leap year""" #>this is called docstring which use dto describe the function

def days_in_month(year,month):
    """return number of days in the month for the given year and month"""
    if not 1<= month <=12:
        return "it is a invalid month"
    if month ==2 and is_leap_year(year):
        return 29
    return months_days[month]

print(days_in_month(2020,2))





#functions are baisically some instructions which we can reuse again and again
def fun():  # def stand for define and fun is the name of the function
    #pass # we cant leave a function completely empty so we use this pass keyword  #def stand for define and fun is the name of the function
    #print("hello World") #function body
    return "hello world" # we can also return some value from function

# fun()
# fun()
# fun()
#this is called DRY code which stands for dont repeat yourself
#it allows us to reuse the code again again and again without writting the same code again and again


#Executing  functions

#print(len("hello World"))
#print(fun().upper())

def greet(name):
    return f"Hello {name}!.welcome to python"
print (greet("Hidden"))
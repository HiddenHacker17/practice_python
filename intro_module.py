#from my_module import find_index as fi
import random
#from my_module import * #import all the function from my_module.py file but it is not recommended because it can create problem if we have same function name in both file then it will create problem for us to know which function we are using

courses=["math","history","physics","compSci"]
#index=find_index(courses,"compSci")
#print(index)
#print(sys.path) #to see the path where python is looking for the module to import it
random_course=random.choice(courses) #to get random element from the list
print(random_course)
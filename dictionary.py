#dictionary is a collection of key and value pair
#we use curly braces to define a dict,it is unorder collection of key an value
student={"name": "Rishu", "age": 20, "courses": ["Math", "CompSci"]}
student1={"1": "Rishu", "2": 22}
#print (student)
#print(student1["1"])              #to access the value we use key name in square bracket
#print(student["names"])           #this will give error bcz there is no key name in the dict
#print(student.get("names"))         #this is another way to access the value using get method this will not give error if the key is not present in the dict it will return none
#print(student.get("name"))
#student["phone"] = "9508902743"       #to add new key and value to
#print(student.get("phone"))
#student["name"] ="Rishabh"            #to change the value of existing key   
#del student["age"]                      #to remove the key and value pair from the dict
#pop_value = student.pop("courses")       #this will remove the key and value pair and also return the value of the removed key
#print(pop_value)

#print(student.keys())             #to get all the key from the dict
#print(student.values())           #to get all the value from the dict
#print(student.items())             #to get all the key and value pair from the dict as a tuple in a list


for key,value in student.items() :        #to loop through the dict
    print(key,value)
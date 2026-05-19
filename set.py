courses={"math","history","physics","compSci"} #we use curly braces to define the set and it is unordered collection of unique element
#print(courses)
#unlike our list and tuple set does not maintain the order of the element and it also does not allow duplicate element
#courses.add("art") #to add element to the set
#print(courses)
#major use of set is to find the unique element from the list
courses_list ={"math","history","physics","compSci","math","history"}
subject_list= {"geography","Philosophy","math"}

#print("math" in courses_list)
print(courses_list.intersection(subject_list)) #for common element in both set
print(courses_list.difference(subject_list)) #for element in courses_list but not in subject_list
print(courses_list.union(subject_list)) #for all element in both set except duplicate element

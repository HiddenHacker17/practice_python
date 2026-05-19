courses =['History', 'Math', 'Physics', 'CompSci']
subject =["geography","Philosophy"]
#print(courses)
#print(len(courses))
##print(courses[0])
#print(courses[-1])
#print(courses[8])
#print(courses[0:2])
#print(courses[3:])

#to modifiy the list

#courses.append("Art") #if we want to add the element at the end
#@courses.insert(2, "Arts") #if we want to add the element at any index
#courses.insert(0,subject)  #add whole list to the list 
#courses.extend(subject)    #add element to the new list to last index
courses.remove("History") #to remove the specific element from the list
courses.pop()            #    this only remove the last element from the list 
  
print(courses)

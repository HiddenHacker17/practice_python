courses =['History', 'Math', 'Physics', 'CompSci']
numbers = [2, 3, 5, 7, 11, 13]
#subject =["geography","Philosophy"]
#print(courses)
#print(len(courses))
##print(courses[0])
#print(courses[-1])
#print(courses[8])
#print(courses[0:2])
#print(courses[3:])
#print(courses[-1])

#to modifiy the list

#courses.append("Art") #if we want to add the element at the end
#@courses.insert(2, "Arts") #if we want to add the element at any index
#courses.insert(0,subject)  #add whole list to the list 
#courses.extend(subject)    #add element to the new list to last index
#courses.remove("History") #to remove the specific element from the list
#courses.pop()            #    this only remove the last element from the list 
#popped_value = courses.pop()  # remove the last element and store it in a variable
#print(popped_value)

#sorting our list


#numbers.sort()  #sort the list in ascending order
#numbers.reverse() #sort the list in descending order
#courses.sort()  #sort the list in ascending order
#courses.sort(reverse=True) for decending order , this will alter the original list
#numbers.sort(reverse=True)  this also alter tte original list
#sorted_courses= sorted(courses) #this will not alter the original list

#print (min(numbers))
#print (max(numbers) )
#print (sum(numbers))
#print (sorted_courses)

#finding value

#print(courses.index("Math"))

#looping valuein list

#for item in courses:
   # print(item)


#for index,courses in enumerate(courses,start=1):
 #  print (index,courses)

#spliting and joining list

course_str=" * ".join(courses)
print(course_str)
new_list=course_str.split(" * ")
print(new_list)

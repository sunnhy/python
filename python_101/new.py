##---------------------DATA TYPES----------------------##
#x= 10
#y= 20
#print(type(x)) -----prints type of the character like int, string,float,boolean etc.

#name = "BandiLa Newton"
#print(name[2])   -----you can print a character from a specific position
#print(len(name))  ----lenght of the string

##----------------------STRING METHODS-----------------------##

#print(name.upper())    #printname in uppercacse
#print(name.title())    #print string title, i.e the firstname
#print(name.split())    #prints the splitted strings seperately by a comma

##-------------------------- LISTS ----------------------------##

#numbers = [24, 35, 46, 57]
#print(numbers[0])       #Indexing.1
##print(numbers[-1])      #Indexing.2

#numbers[3] = 54         #Modifying list
#print(numbers)          #prints modified list

#------------- IMPORTANT IN LISTS --------------#

#numbers.append(68)        #adds integer/value at the end
#numbers.insert(5,79)      #adds int/value by a positiion mentioned
#print(numbers)
#numbers.pop()             #removes the last value/int 
#print(numbers)

#for mass in numbers:       # LOOP THROUGH LIST
#   print(mass)


##----------------------DICTIONARIES--------------------------##

#student = {                 #creating dictionary
#    "name": "Newton",
#    "age": 34,
#    "sex": "male"
#}
#print(student)
#print(student["age"])        #accesing value from dictionary

#student["city"]="hyderabad"  #adding new key to the dictionary
#print(student)

#for key,value in student.items():   # LOOP THROUGH DICTIONARY
#    print(key, value)               #uses inbuil items() function in python to print key and values seperately

##------------------------CONDITIONALS-----------------------##

# age = 31

# if age > 35 :                         # multiple conditions with if , else, elif 
#    print("old AF")
# elif age > 30:
#    print("old lady")
# else:
#    print("young babe")

##------------------------LOOPS------------------------##


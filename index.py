def percent(InnerText):
    while True: 
        try:
            name = int(input(InnerText))  
            return name  
        except ValueError:  
            print("Please enter a number")

def calculate(M2, M3, M4, M5):
    total = M2 + M3 + M4 + M5
    percent = (total / 400) * 100
    return percent


M2 = percent("Enter your physics marks\n")
M3 = percent("Enter your computer marks\n")
M4 = percent("Enter your english marks\n")
M5 = percent("Enter your math marks\n")

result = calculate(M2, M3, M4, M5)
print("Your percentage is", result)

if result >= 80:
    print("Your grade is A+")
elif result >= 60:
    print("Your grade is A")
elif result >= 40:
    print("Your grade is B")
elif result >= 30:
    print("Your grade is C") 
else:
    print("You have failed.")    

newlist = ['aarij khan']
list.append("10")
# append don't return any value

result = list.insert(0, 'khan')
# insert don't return any value

result = list.pop()
# pop return the value
result = list.pop(2)
# pop return the value and can delete with index inside paranthesis


# remove don't return any value

result = list.index(10)
# index method return the index of the value
result = list.count(10)
# count return the number of times the value is present in a list
result = list.sort()
# sort don't return any value

result = list.reverse()
# reverse don't return any value

result = list.copy()
# copy return the copy of the list

result = list.extend(newlist)
# extend don't return any value
print(list)
# for loop/////
array = ['aarij', 'khan', 'good', 'boy']
for i,a in enumerate(array)  :
    print(a,i)
# map loop with function

def newFun(thisOne) :
    print('thisOne: ', thisOne)
    return f"hello {thisOne}"    
    
newOne = list(map(newFun,array))    
print('newOne: ', newOne)

# map loop without function
def newFun(thisOne) :
    print('thisOne: ', thisOne)
    return f"hello {thisOne}" 

# map loop without anononus function 
list = [1, 2, 3, 4, 5, 6]
list.remove(4)
print(list)
 
newOne = list(map(lambda x :  f'{x} * 2 = {x * 2}' ,array))    
print('newOne: ', newOne)
array = ["hello", "world", "cat", "python", "AI"]
print('array: ', array[1][0:2])
array2 = list(map(lambda t: t[:3] if len(t) > 4 else t, array))
def newfun(thisOne):
    if len(thisOne) > 2:
        return thisOne[0:3]
    else:
        return thisOne
array3 = list(map(newfun,array))
print('array2:', array3)

# while loop
i = 0
while i < len(array) :
    array2.append(array[i] + 10)
    i += 1
print('array2: ', array2)
students = [
    {
        "name": "Sara Khan",
        "id": 2,
        "grades": {"Math": 88, "English": 90, "Science": 65},
    },
    {
        "name": "Bilal Tariq",
        "age": 21,
        "id": 3,
        "grades": {"Math": 15, "English": 82, "Science": 89},
    },
    {
        "name": "Ayesha Malik",
        "age": 23,
        "id": 4,
        "grades": {"Math": 21, "English": 87, "Science": 43},
    },
   
]

print(students)
id = int(input("enter any student id\n"))
filterStudent = list(filter(lambda x : x['id']==id,students))
if filterStudent:
    print(filterStudent)
else:
    print("student not exist")    

   
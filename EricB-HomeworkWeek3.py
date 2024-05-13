#Python Homework Week 3

#Question 6
#Write a multi-line string with your name, favorite food, and dream job on 3 different lines
quest6 = """
Eric Bast
Nachoes
Data Analytics Team Lead"""
print(quest6)

#Question 7
#Assign 5 different data types to 5 different variables. At least one datatype must be a string
#Print the length of your string
#Print the index value of the 4th character in your string
var1 = "Dragons"
var2 = 365.25
var3 = 42
var4 = False
var5 = ["ducks", "chickens", "swans", "geese"]
str1 = len(var1)
print(str1)
print(var1[3])

#Question 8
#Create a new variable called savvy, and assign it the string with this phrase "Learning Data Analytics and Python is Awesome!"
savvy = "Learning Data Analytics and Python is Awesome!"
#Return a range of characters that slices the above string from the beginning of "ing" up to before "and"
print(savvy[5:23])
#Replace "Awesome" with "great" in the string
savvy2 = savvy.replace("Awesome", "great")
#Test and print the savvy string to see it contains "Python"
print(savvy2)
if "Python" in savvy:
    print(savvy, "See, the string does contain the word Python")


#Question 9
#Create and assign 3 more variables called name, age and length using the multi-variable naming method
name, age, length = "Eric", "42", "77 inches"
#Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."
miniBio = "Hi, my name is {}, I am {} tall and {} years old today"
#Print 'miniBio'
print(miniBio.format(name, length, age))
#Cast and print the age variable to a float 
dec1 = float(age)
print(dec1)

#Question 10
#Create a list of at least 5 elements of mixed data types
dtList1 = ["Dragons", "D20", 42, ["spells", "potions", "elixers"], 365.25]
#Replace a part of it with something else
#Append or insert several more items to the list
dtList1.append("Ents")
dtList1.append("Pixies")
#Find and print the length of the list
dtListlen = len(dtList1)
print(dtListlen)
#Slice a sub-section of the 1st list, and save it to a different 2nd list
dtList2 = dtList1[2:5]
#Print the 2nd list
print(dtList2)
#Extend your original list with the 2nd list sliced above
dtList1.extend(dtList2)
#Create a new list called "simList" containing at least 5 elements of the same data type, either string, integer, float, or Boolean
simList = ["robin", "bluejay", "sparrow", "dove", "mocking bird"]
#Sort "simList", and print the list
simList.sort()
print(simList)
#Copy the "simList" list to another 3rd list
dtList3 = simList.copy()
#Add the 2nd and 3rd lists together into a 4th list
dtList4 = [dtList2 + dtList3]

#Question 11
#Create a tuple of about 5 elements
pracTup1 = ("purple", "green", "red", "blue", "orange")
#Multiply your tuple by 3 and save it to a new 2nd tuple
pracTup2 = pracTup1 * 3
#Access and print the 12th element from the 2nd tuple
tup12 = pracTup2[11]
print(tup12)
#Sort the 2nd tuple and print it
print(sorted(pracTup2))
#Copy 4 specific elements from your 2nd tuple to a new 3nd tuple
pracTup3 = pracTup2[2:6]
#Unpack the 3rd tuple into 4 variables and print these variables
(tomato, cabbage, squash, eggpant) = pracTup3
print(tomato)
print(cabbage)
print(squash)
print(eggpant)
#Create a 4th tuple with single item 50 and print this tuple
pracTup4 = (50,)
print(pracTup4)
#Add the 2nd and 3rd tuple together into a 5th tuple and print the tuple
pracTup5 = pracTup2 + pracTup3
print(pracTup5)

#Question 12
#Create a set of about 3 elements
fruits = {"apples", "grapes", "oranges"}
#Add a list of fruits to the above set and print the result
fruits2 = ["pears", "bananas", "kiwi"]
#Add a car element to your set
fruits.add("cars")
#Create a 2nd set with a few odd items
veggies = {"corn", "green beans", "carrots", "onions"}
#Save the union of 1st set and 2nd set to a 3rd set
grownFoods = fruits.union(veggies)
#Pop an element from the 2nd set, and print the remainder of the set
veggies.pop()
print(veggies)
#Clear the 1st set and print the result
fruits.clear()
print(fruits)
#Discard an element, and remove another element from the 3rd set
grownFoods.discard("green beans")
grownFoods.remove("onions")
#Print the remainder of the 3rd set
print(grownFoods)

#Question 13
#Create a dictionary with at least 5 values of different data types
dndChar1 ={
    "Name": "Shelan",
    "Race": "Elf",
    "Class": "Druid",
    "Age": 123,
    "Weight": 94,
}
#Print out 1 value
print(dndChar1["Race"])
#Replace any one value in your dictionary with your name
dndChar1.update({"Name":"Eric"})
#Add your favorite color to the dictionary
dndChar1.update({"FavColor":"Blue"})
#Add a list, tuple or set to your dictionary
dndChar1.update({"Weapons":["sword", "dagger", "short bow"]})
#Print a list of the dictionary keys
dndKeys = dndChar1.keys()
print(dndKeys)
#Print a list of the dictionary values
dndValues = dndChar1.values()
print(dndValues)
#Copy your 1st dictionary into a 2nd dictionary
dndChar2 = dndChar1.copy()
#Pop an item from the 2nd dictionary, and print the dictionary
dndChar2.pop("Weight")
print(dndChar2)
#Remove all the elements from the 2nd dictionary and print the result
dndChar2.clear()
print(dndChar2)
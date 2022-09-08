# Since variables in python don't need to be assigned a specific data type during declaration
# we can use casting to declare the variable to the data type we need. Python is an object-oriented
# programming language, and thus it uses classes to define its data-types, including its primitive ones.

exampleStr = 50                                       # This initializes the variable exampleStr as an integer.
stringX = str(50)                                     # But if we want the variable to be of the type string specifically we can use the codeword str()
                                                      # and just write the contents we want to assign to it into the constructor ().
stringY = str("50")                                   # It's not necessary to use brackets for this when assigning numerical characters,
stringZ = str("ab$%cd Hello There! 63n3r4l k3n0b1!")  # but for letters or special characters '' or "" have to be used.

exampleFloat = 20.5                   # This initializes the variable exampleFloat as a floating-point primitive.
floatX = float(42)                    # If we want to initialize an integer number as a float, we can either just put a .0 behind it,
                                      # or cast it with float().
floatY = float("40")                  # We can also put a string type into the constructor to cast it into a float type,
                                      # as long as the string contains only a single number, otherwise the method throws an exception.
                                      # It also doesn't matter if the string actually contains a floating-point number or an integer,
                                      # as it specifically assigns a float.
floatZ = float("42.345")

exampleInt = 30         # Initializes the variable exampleInt as an integer primitive.
integerX = int(42.8)    # We can cast a floating-point number as an integer and python removes all content behind the decimal point.
                        # Every number behind the decimal point is just removed, python does not perform any sort of arithmetic rounding
                        # on the resulting integer.
integerY = int("42")    # Like with float casting, it is also possible to cast a string type into an integer with this, the same rules
                        # apply as with casting a string into a float type, but the peculiarity here is that if a decimal point is included
                        # in the string, it will throw an exception like any other special character would (because as I said, the same rules
                        # apply here as with float casting). So an actual float would have to be cast into an integer first for this to work.

print(exampleStr)
print(stringX)
print(stringY)
print(stringZ)
print()
print(exampleFloat)
print(floatX)
print(floatY)
print(floatZ)
print()
print(exampleInt)
print(integerX)
print(integerY)
print()

exampleList = ["apple", "banana", "cherry"]                     # Lists are used to store multiple data points in a single variable, very similar to an array in for example, Java.
                                                                # The list is one of four built in collection types for python. The other 3 are tuple, set, and dictionary.
print(exampleList)                                              # All different collection types come with their own different properties and usages.
print()                                                         # The list has its content ordered, changeable, and allows duplicate entries.

listOne = ["apple", "banana", "cherry", "apple", "cherry"]      # Ordered means the items have their order defined, and the order will not change unless specific list methods are used to do so.
                                                                # Adding a new item will put it at the end of the list.
print(listOne)
print()

print(len(listOne))     # The len() function returns the amount of items in the list as an integer
print()

listTwo = ["apple", 45, 30.345, "banana", True, False]      # Lists allow to store different data types, a single list can also contain multiple different types

print(listTwo)
print()

print(listTwo[-4])                                          # Putting a negative integer will count the index from the end
print()

print(type(listTwo))        # Python defines every list as an object of the class 'list'
print()

listThree = list(("apple", "banana", "orange"))     # Initializing a new list can also be done with the list() constructor

print(listThree)
print()

print(listTwo[3], listTwo[0], listTwo[5], listTwo[4])       # Lists are indexed, and their different items can be accessed individually with putting the integer for the desired item into [] brackets behind the list
print()

print(listTwo[-3], listTwo[-0], listTwo[-5], listTwo[-4])   # Negative indices will do the same counting from the end of the list
print()

print(listTwo[2:5])     # Using two indices separated by a : will access a range of items,
print()                 # in this case it starts with index 2 (and include the item in the selection) and end with index 5, but NOT INCLUDE the item in this position

print(listTwo[:4])      # By leaving out the value for the start the range will begin with the first item. (And also not include the item on position of the specified end index)
print()

print(listTwo[2:])      # By leaving out the end value, the range will go until the end of the list, BUT INCLUDE THE ITEM IN POSITION OF THE START INDEX AGAIN
print()

print(listTwo[-4:-2])   # This can also again be done with negative indices
print()

if "banana" in listTwo:                     # To check if a datapoint is on listTwo
    print("Yes, 'banana' is in listTwo")
print()

listTwo[1] = "watermelon"       # To change an item in the list just assign a new value to a list index
print(listTwo)
print()

listFour = ["Skiing", "Football", "Formula 1", "Boxing", "Climbing", "Hiking"]
print(listFour)
print()

listFour[1:3] = ["Swimming", "Running"]     # Ranges of item values can also be changed
print(listFour)                             # Only putting ONE value can replace two items by just the one
print()

listFour.insert(2, "Diving")        # To insert an item into index 2 of the list and push all other items back, starting with the original item in index 2
print(listFour)
print()

listFour.append("Formula 1")        # To add an item AT THE END of the list
print(listFour)
print()

listFive = ["Football", "Baseball", "Soccer"]
listFour.extend(listFive)       # Lists can be extended with other lists, or any other iterable object, like the other 3 forms of collection in Python
print(listFour)
print()

listFour.remove("Baseball")     # Removes the specified value from the list
print(listFour)
print()

listFour.pop(3)                 # Removes the item in the specified index, if no index is specified pop() removes the last item
print(listFour)
print()

del listFour[3]                 # The same can be done with the del keyword, and if no index is given, it will delete the list completely
print(listFour)
print()

listFive.clear()                # Will empty the entire list, but the list itself will not be deleted
print(listFive)
print()

listFour.sort()                 # Will sort the list alphabetically
print(listFour)
print()

listFour.sort(reverse=True)     # Sorts the list descending
print(listFour)                 # The sort function can also be customized
print()

listSix = listFour.copy()       # Lists can also be copied like any other object in OOP, as listSix = listFour would just reference to the same object,
print(listSix)                  # and any change made in either would also change the other variable name, as the same object in the memory is accessed then.
print()

listSeven = listFour + listSix  # Lists can be joined with the + operator
print(listSeven)
print()





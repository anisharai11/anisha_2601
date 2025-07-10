#String data types
#lists and tuples
#Conditionals

#Slicing
name = "Anisha"
name [0:3]
Print(name[3:6])
print(name[3:len(name)-2])

#length
Print(len(name))

#find and replace
name = "anisha"
print(name.find("g"))
replaced = name.replace("g", "p")
print(replace)

#escape sequence character
text = "My name is Anisha \n and \n i'm 21 years old"
print(text)

text = "My name is Anisha \n\t and \n i'm 21 years old"
print(text)

text = "My name is Anisha \n \'here'\ and \n i'm 21 years old"
print(text)

#Write a program  to detect double spaces in a string.
letter = "Dear Students, This Python course is going well. Thanks!"
text = input("Dear students, This python course is going well. Thanks!")
if "  " in text:
    print ("double space detected!")
else:
    print("No double space found.")
#Replace the double spaces from problem 3 with single spaces.
text = "Dear students, This python course is going well. Thanks!"
corrected = text.replace("Dear students", "  ")
print(corrected)

#Write a program to format the following letter using escape sequence characters.
letter = "Dear Students,\n This python course is going well.\n Thanks!"
print(letter)
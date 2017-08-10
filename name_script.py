#This is a program to say hi to the people in a list of strings
first_names = ["Calder", "Patrick", "Stephanie", "Jahmila"]
theirNames = ["Tracy", "Alex", "Morgan"]
print first_names

for person in first_names:
#Assigns the list of variables as person that I want to loop through
	print "Hi "+person+"!"

for person in first_names + theirNames:
	print "Hi "+person+"!"

#conditional statements: if, elif, else (if... elif... elif... else...)
#input()

name = raw_input("what is your name?")
name = str(name)
print name

location = raw_input("where are you from?")
location =str(location)
print location

if location != "New York":
        print "I can subsidize your flight if you fit our age limit"


#input assumes data types, raw_input assumes its a string

age = raw_input("What is your age?")
age = int(age)
print age

older = age + 1
print older

if age < 10:
        print "You're invited to Blue Ivy's Bday Party! Have Fun!"
elif age >= 10 and age < 18:
        print "Go to Disneyland~"
else:
        print "You're not invited. Sorry you're too old :("

#if, elif and else all have to be aligned        
        

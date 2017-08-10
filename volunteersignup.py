#Volunteer Sign Up Bank
#1 for phonebank, 2 for canvas, 3 for nothing

name = raw_input("What is your name?")
name = str(name)
print name

location = raw_input("Where do you live?")
location = str(location)
print location

age = raw_input("Please enter your age")
age = int(age)
print age

interestlist = ["1. Phonebanking", "2. Canvassing", "3. None"]
print interestlist
interest = raw_input("Which of the following are you interested in?")
interest = int(interest)

if interest == 1:
    print "Congrats you'll be doing phonebanking"
elif interest == 2:
    print "Congrats, we'd love for you to help us canvass"
else:
    print "We don't have any positions available right now that fit your interests. Sorry."
    

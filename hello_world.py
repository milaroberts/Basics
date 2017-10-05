#womenwhocodedc on slack
print "Hello, World!"
#this is a function definition, def creates functions/programs
def print_greeting(name):
	greeting = 'Hello,' +name+ '!'
	print greeting 
#semicolons mean the next line is related to the one above it, as do tabs
#input is a built-in function that takes input from a user's terminal

retrieved_name = raw_input("Please enter your name")
print_greeting(retrieved_name)
print "Script Complete."
#last line makes sure the program is still running

import math

#***************
#  Variables, user input, printing review
#***************

#Declare a variable x, and assign it to 4
x = 4
#Now whenever we use x, Python will see it as a 4
#So this line will print 4 to the user
print(x)

#You can update the value of a variable
x = x + 5
print(x)

x = int(input("Give me a number: "))
x = x + 5
print(x)


#Ask for the user's favorite color and tell them you like that color too.
color = input("What's your favorite color?")
print("Cool! I like", color, "too!")

#What's the issue with this?
color = input("What's your favorite color?")
print("Cool! I like blue too!")

#What's the issue with this?
color = "blue"
print("Cool! I like", color, "too!")


#Define a function that calculates someone's age based on the year they were born.
def age(birth_year):
	age = 2020 - birth_year
	print("You must be about", age, "years old!")

age(1992)

#What's the issue with this?
def age(birth_year):
	age = 2020 - 1992
	print("You must be about", age, "years old!")


#What's the issue with this?
def age(birth_year):
	birth_year = 1992
	age = 2020 - birth_year
	print("You must be about", age, "years old!")


#***************
#  Madlibs
#***************
color = input("Give me a noun: ")
animal = input("Give me an animal: ")
country = input("Give me a country: ")
print("That's silly, there are no", color, animal,"s in",country + "!")



#***************
#  Functions
#***************
#Take parameters
#Return any variable type

def add_two(x):
	return x+2

#What's the issue with this?
def add_two(x):
	return 3+2

def get_color():
	color = input("What is your favorite color?\n")
	return color


def return_true():
	return True


#***************
#  Code blocks
#***************
def pythagorean_theorem(a,b):
	a_square = a*a
	b_square = b*b
	square_sum = a_square + b_square
	c = sqrt(square_sum)
	return c

def print_score(score):
	#Demo what happens when these aren't indented correctly
	print("You've scored", score, "points so far")
	print("Good job!")



#***************
#  Booleans
#***************
#Statements that evaluate to True or False
print(10<2)

result = 10<2
print(result)

name = "Duke"
is_name = "Estephania" == name
print(is_name)
print("Estephania" == name)

is_not_name = not "Angie Rose" == name
is_not_name2 = "Angie Rose" != name
print(is_not_name)
print(is_not_name2)
print("Angie Rose" != name)


#***************
#  If/elif/else
#***************

#Now we can start making decisions with our code.

#If/else statements let us selectively run code based on some condition.

#If the condition is True, run the code block.
#If the condition is False, skip the code block.

x = 9

#The print statement "inside" the if statement block will only run
#	if the condition "x > 4" is True
if x > 4:
	print("x is greater than 4.")

print("Program ended")


#We use an "else" statement to tell the program what to do if
#	the if statement is False.
#Think of "else" like "if all else fails"

#Now, if "x > 4" is False, it will "fall through" to the else statement.
#"Fall through" means "skip"
if x > 4:
	print("x is greater than 4.")
else:
	print("x is not greater than 4.")

print("Program ended")

#Only the if or the else will run.
#If the if statement successfully runs, the program skips the else entirely.


#If you want to check x in more than two conditions,
#	use "elif", meaning "else if"

#If the first "if" condition fails, it will fall through to the elif.
#If the elif condition fails, the code wil fall through to the else.
if x > 2:
	print("x is greater than 4.")
elif x == 2:
	print("x is equal to 4.")
else:
	print("x is less than 4.")

print("Program ended")


#We use an elif when we want the code to be skipped if a previous condition is True.
#Our code will check each elif in order until one is True, the else is reached,
#	or there are no more statements to check.

money = 0
name = "Kadari"

if name == "Robert":
	money = 120

elif name == "Marcos":
	money = 290

elif name == "Jordan":
	money = 175

elif name == "Kadari":
	money = 1000000

else:
	print("Name not found!")
	

#"else" statements never check for a condition.
#	Remember, "else" is what runs "if all else fails"
#		It will only run if all the if/elif conditions fail

#You do not always need an else.
#But, if you have an else, there needs to be an if statement before it.

#There are some more nuances, but you'll pick them up as you go.

#***************
#  Nested code blocks
#***************

def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False

#Nested if statements:

name = "Nelson"
birth_month = 10

if birth_month == 10:
	if name == "Nelson":
		print("Happy birthday, Nelson!")

	elif name == "Hilal":
		print("Happy birthday, Hilal!")

	else:
		print("Who are you?")

else:
	print("Welp, maybe next month")
	

#Zip Zap:
Write a function that takes a number, n
If n is evenly divisible by 5, print "Zip"
If n is evenly divisible by 7, print "Zap"
If n is evenly divisible by both 5 and 7, print "ZipZap"
Otherwise, print the number n

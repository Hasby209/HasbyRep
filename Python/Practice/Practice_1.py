# Practice_1
# Python_Variables



# Example_1
# Multi_Line_Variables
firstVar = "firstVal"
secondVar = "secondVal"
thirdVar = "thirdVal"

print(firstVar)
print(secondVar)
print(thirdVar)



# Example_2
# Single_Line_Variables
fourthVar, fifthVar, sixthVar = "fourthVal", "fifthVal", "sixthVal"

print(fourthVar, fifthVar, sixthVar)



# Example_3
# Unpacking_Variables
Variables = ["seventhVal",  "eighthVal", "ninthVal"]
seventhVar, eighthVar, ninthVar = Variables

print(seventhVar)
print(eighthVar)
print(ninthVar)



# Example_4
# Global_Variables
tenthVar = "tenthVal"

def myfunc() :
	
	print("This is " + tenthVar)

myfunc()



# Example_5
# Local_Variables
eleventhVar = "eleventhVal1"

def myfunc() :
	
	eleventhVar = "eleventhVal2"
	
	print("This is " + eleventhVar)

myfunc()

print("This is " + eleventhVar)



# Example_6
# The_Global_Keyword
def myfunc() :
	
	global twelfthVar
	twelfthVar = "twelfthVal"

myfunc()

print("This is " + twelfthVar)



# Example_7
# Change_A_Global_Variable
ThirteenthVar  = "ThirteenthVal1"

def myfunc() :
	
	global ThirteenthVar
	ThirteenthVar = "ThirteenthVal2"
	
myfunc()

print("This is " + ThirteenthVar)

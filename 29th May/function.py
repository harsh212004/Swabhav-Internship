#Task-1 variables & data type

interger_var = 10
float_var = 1.1
string_var = "Hello World"
boolean_var = True

print(f"Integer Value: {interger_var}, type : {type(interger_var)}")
print(f"Integer Value: {float_var}, type : {type(float_var)}")
print(f"Integer Value: {string_var}, type : {type(string_var)}")
print(f"Integer Value: {boolean_var}, type : {type(boolean_var)}\n")


#Task-2 String Manipulation

text = "Python Programming  is Fun"

uppercase_text = text.upper()
print("Uppercase:",uppercase_text)

replaced_text = text.replace("Fun", "powerful")
print("Replace_text", replaced_text)

slice_text = text[7:18]
print("Sliced Text", slice_text)

print("Length of String is:", len(text))

#Task-3 List and Loops

numbers = [1,2,3,4,5]
print("List of Numbers:")

for num in numbers:
	print(num)

i = 0
total = 0
while i < len(numbers):
	total += numbers[i]
	i += 1
print("Sum of the numbers", total)

#Task-4 Conditions statement

try:
	age = int(input("Enter age:"))
	if age >= 18:
		print("User is a Adult")
	else:
		print("User is not a Adult")
except ValueError:
	print("Invalid Input")
	

#Task-5 Functions

def calculate_area(length,width):
	return length * width

print("Area:",calculate_area(1,2))


#Task-6 Dictionaries

students = {"abc": 70,
            "bcd": 75,
            "qwe": 80,
            "rty": 45,
            "yui": 50
}

students["sdf"] = 55
students["abc"] = 71

print("student score:")
for name,score in students.items():
    print(f"{name} : {score}")
	

#Task-7 File Handling

with open("Students.txt","w") as file:
	file.write("abc\nqwe\nert\nrty\ntyu\n")
	
with open("Students.txt","r") as file:
	content = file.read()
	print("File content", content)
	

#Task-8 Error Handling

try:
	a = float(input("Enter a:"))
	b = float(input("Enter b:"))
	result = a/b
	print("Result:",result)
except ZeroDivisionError:
	print("Cannot Divisible by zero")
except Exception as e:
	print("Unexpected Error")
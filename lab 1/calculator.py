
def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

def modulus(num1,num2):
	return num1 %num2

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n"
		"5. Modulus\n")


select = int(input("Select the option"))

nums1 = int(input("Enter first number: "))
nums2 = int(input("Enter second number: "))

if select == 1:
	print(add(nums1, nums2))

elif select == 2:
	print(subtract(nums1, nums2))

elif select == 3:
	print(multiply(nums1, nums2))

elif select == 4:
	print(divide(nums1, nums2))
	
elif select==5:
	print(modulus(nums1, nums2))
	
else:
	print("Invalid selection")
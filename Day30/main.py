#FileNotFound

# try:
# 	file = open("Day30/data.txt")
# except:
# 	# print("An error occurred.")
# 	file = open("Day30/data.txt", "w")
# 	file.write("Something")
# else:
# 	print(file.read())
# finally:
# 	file.close()
# 	print("File closed.")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
	raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height **2
print(bmi)
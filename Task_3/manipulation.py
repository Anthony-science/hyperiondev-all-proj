str_manip = input("Enter a sentence: ")  # Ask for input
str_len = len(str_manip)  # Determine input length
print(str_len)  # Display length
last_letter = str_manip[-1]  # Find last char
new_str = str_manip.replace(last_letter, "@")  # Replace function executed
print(new_str)  # Check substitution in (new) string
last_three = str_manip[:-4:-1]  # Find last 3 chars in str_manip
print(last_three)  # Output last 3 chars in reverse order
print(str_manip[:3] + str_manip[-2:])
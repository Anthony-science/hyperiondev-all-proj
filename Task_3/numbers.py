# Ask for input, assign each to a variable: num_a, num_b, num_c
num_a = input("Please enter your first number: ")
num_b = input("Please enter your second number: ")
num_c = input("Please enter your third number: ")
# Typecast
num_a = int(num_a)
num_b = int(num_b)
num_c = int(num_c)
# Sum all variables and print
sum_all = num_a + num_b + num_c
print(f"Sum of numbers: {sum_all}")
# num_a - num_b, return and print
a_subtract_b = num_a - num_b
print(f"First number - second number: {a_subtract_b}")
# num_c * num_a
c_times_a = num_c * num_a
print(f"Third number multiplied by first number: {c_times_a}")
# Mean
mean = (num_a + num_b + num_c) / 3
print(f"Mean of all three numbers: {mean}")
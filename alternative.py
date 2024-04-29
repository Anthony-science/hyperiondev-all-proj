# Pass string
orig_string = str(input("Please enter a sentence: "))
cap_letters = ""      # Define new string for letter capitalisation

for i in range (len(orig_string)):
    if i % 2 == 0:      # Determine alternate chars and set upper or lower
        cap_letters += orig_string[i].upper()
    else:
        cap_letters += orig_string[i].lower()
# Output result
print(cap_letters)

    # Function defined for capitalising alternate words
def alternateUppercase(string):
    words = string.split(' ')   # Separate words out
    result = []     # Initialise a new list
    for i, w in enumerate(words):
        if i % 2:
            result.append(w.upper())
        else:
            result.append(w.lower())
    return ' '.join(result)
# Call function
print(alternateUppercase(string=orig_string))

# Pass string
orig_string = "No-one expects the Spanish Inquisition"
cap_text = ""       # Define new str
for i in range (len(orig_string)):
    if i % 2 == 0:      # Determine alternate chars and set upper or lower
        cap_text += orig_string[i].upper()
    else:
        cap_text += orig_string[i].lower()
# Output result
print(cap_text)
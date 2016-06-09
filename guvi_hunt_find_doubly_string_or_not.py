k = raw_input("Enter the string:\n\n")
print k
first_half = k[:len(k)/2]
second_half = k[len(k)/2:]
if first_half == second_half :
    print "\nIt is a doubly string"
else:
    print "\nIt is not a doubly string"

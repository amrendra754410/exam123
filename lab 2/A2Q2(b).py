#Objective No.- 2(b)
# Demonstrate the following functions/methods which operate on strings in Python with
# suitable examples:
# i) len( ) ii) strip( ) iii) rstrip( ) iv) lstrip( ) v) find( ) vi) rfind( ) vii) index( ) viii) rindex() ix)
# count( ) x) replace( ) xi) split( ) xii) join( ) xiii) upper( ) xiv) lower( ) xv) swapcase( ) xvi) title(
# ) xvii) capitalize( ) xviii) startswith() xix) endswith()


string = input("Enter a string: ")
sum = 0
for ch in string:
    if ch.isdigit():
        sum += int(ch)
print("Sum of digits:", sum)




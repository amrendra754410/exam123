#Name- Rishit Swain
#Regd. No.- 24E119F02
#Objective No.- 4

string = input("Enter a string: ")
encrypted_string = ""

for ch in string:
    if ch.isalpha():
        if ch.isupper():
            encrypted_string += chr((ord(ch) - 65 + 3) % 26 + 65)
        else:
            encrypted_string += chr((ord(ch) - 97 + 3) % 26 + 97)
    else:
        encrypted_string += ch

print("Encrypted string:", encrypted_string)




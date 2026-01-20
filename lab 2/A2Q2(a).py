#Name- Amrendra Kumar
#Regd. No.- 24E111B52
#Objective No.- 2(a)
# Write a program to accept some string from the keyboard and display its characters by
# index wise (both positive and negative index).

test_string = "  Hello World  "

print("Original string:", test_string)

print("Length:", len(test_string))
print("strip():", test_string.strip())
print("rstrip():", test_string.rstrip())
print("lstrip():", test_string.lstrip())

print("find('o'):", test_string.find('o'))
print("rfind('o'):", test_string.rfind('o'))
print("index('o'):", test_string.index('o'))
print("rindex('o'):", test_string.rindex('o'))

print("count('l'):", test_string.count('l'))
print("replace('World','Python'):", test_string.replace("World", "Python"))
print("split():", test_string.split())
print("join(['Hi','there']):", " ".join(['Hi', 'there']))

print("upper():", test_string.upper())
print("lower():", test_string.lower())
print("swapcase():", test_string.swapcase())
print("title():", test_string.title())
print("capitalize():", test_string.capitalize())

print("startswith('  He'):", test_string.startswith("  He"))
print("endswith('ld  '):", test_string.endswith("ld  "))




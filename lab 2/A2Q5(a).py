#Name- Rishit Swain
#Regd. No.- 24E119F02
#Objective No.- 5(a)

# Demonstrate the following functions/methods which operate on lists in Python with
# suitable examples.
# i) list( ) ii) len( ) iii) count( ) iv) index ( ) v) append( ) vi) insert( ) vii) extend() viii) remove(
# ) ix) pop( ) x) reverse( ) xi) sort( ) xii) copy( ) xiii) clear( )

my_list = [3, 1, 4, 1, 5, 9, 2]

print("Original list:", my_list)
print("list():", list(my_list))
print("len():", len(my_list))
print("count(1):", my_list.count(1))
print("index(4):", my_list.index(4))

my_list.append(6)
print("append(6):", my_list)

my_list.insert(2, 7)
print("insert(2, 7):", my_list)

my_list.extend([8, 10])
print("extend([8, 10]):", my_list)

my_list.remove(1)
print("remove(1):", my_list)

popped = my_list.pop()
print("pop():", popped)
print("List after pop:", my_list)

my_list.reverse()
print("reverse():", my_list)

my_list.sort()
print("sort():", my_list)

copied_list = my_list.copy()
print("copy():", copied_list)

my_list.clear()
print("clear():", my_list)



# 1. Create a list named my list with items which have different data types and length at least 5.

my_list = ["dog","chicken",20, 'cat', 18, 7]

# 2. Print all items of my list in string line.
for items in range(len(my_list)):
    print(my_list[items])

# 3. Count the number of each items in my_list.
for items in range(len(my_list)):
    print(my_list[items], end = ":")
    print(my_list.count(my_list[items]))
    
# 4. Reverse the order of the items in my_list.
my_list.reverse()
print(my_list)
# 5. Square the numeric items in my_list then print result.
print(my_list*2)

# 6. Add some single values and iterable values to my_list.
my_list.append("fish")
print(my_list)

# 7. Remove values at the end and at the second position of my_list.
my_list.pop(2)
print(my_list)

# 8. Display those items from my_list that  are deivisible by 5.
for items in range(len(my_list)):
    if items % 5 == 0:
        print(my_list[items])

# 9. Calculate the sum of all numeric items in my_list.
count = 0 
for items in my_list:
    if type(items) is int:
        count += items
print(f"SUM = {count}")

# 10. Create a new list named my_list_num from all string items in my_list , then uppercase them.
my_list_str=[]
for item in my_list:
    if type(item) is str:
        my_list_str.append(item.upper())
print(my_list_str)

# 11. Create a new list named my_list_num from all string items in my_list, then sort them
my_list_num=[]
for item in my_list:
    if type(item) is str:
        my_list_num.append(item)
my_list_num.sort()
print(my_list_num)

# 12. Find maximum/minimum values of my_list_num.
print(max(my_list_num))
print(min(my_list_num))

# 13. Remove dupticate values from my_list_num, if have.
for item in my_list_num:
    if my_list_num.count(item) >= 2:
        my_list_num.remove(item)
print(my_list_num)

# 14. Display old and even number of my_list.
num_odd = []
num_even = []
for item in my_list_num:
    if type(item) is int:
        if item % 2==0:
            num_even.append(item)
        else:
            num_odd.append(item)
print(f'num_odd: {num_odd}')
print(f'num_even: {num_even}')
# 1. write a program to read an entire the sample.txt file

f = open('E:\\PYTHON05_VTI\\basic_python05\\Lesson_07\\sample.txt', mode = 'r', encoding='UTF-8')
data = f.read()
print(data)

# 2. Write a program to read an first/last n line of the sample.txt file with n and first/last are arguments come from keyboard.
def read_n_first_last (n , fl):
    f = open('E:\\PYTHON05_VTI\\basic_python05\\Lesson_07\\sample.txt', mode = 'r', encoding='UTF-8')
    if fl == "first":
        data1 = f.readlines()
        print(data1[:n])
    
    if fl == "last":
        data1 = f.readlines()
        print(data1[-n:])
    
    f.close()
read_n_first_last(3,'first')

# 3. Write a program to read line by line os the sample.txt file and store them in a list . Sort the list by length of each line.
def cau3():
    f = open('E:\\PYTHON05_VTI\\basic_python05\\Lesson_07\\sample.txt', mode = 'r', encoding='UTF-8')
    data = f.readlines()
    my_data = sorted(data, key = len)
    print(my_data)
    f.close()
cau3() 


# 4. Write a program to append a line to the sample.txt file with line is argument come from keyboard . print the length of file and
# the line with longest length.

def cau4(add):
    f = open('E:\\PYTHON05_VTI\\basic_python05\\Lesson_07\\sample.txt', mode = 'r', encoding='UTF-8')
    data = f.readlines()
    print(data)
    data.append(add)
    print(len(data))
    print(max(data))

add = "hello everyone"
cau4(add)

# 5. Write a program to count frequency yof each word in the sample.txt file.

# 6. Write a program to store the below content in a file name sample_w.txt. Remove blank line in the file.

#7. Write a program to store the following content in the file name sample_w.txt:

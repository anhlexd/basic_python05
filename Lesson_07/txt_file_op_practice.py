# 1. write a program to read an entire the sample.txt file

with open ('sample.txt', mode = 'r', encoding = 'UTF-8') as f:
    data = f.read()
    print(data)

# 2. Write a program to read an first/last n line of the sample.txt file with n and first/last are arguments come from keyboard.
def read_n_first_last (n , fl):
    with open ('sample.txt', mode = 'r', encoding = 'UTF-8') as f:
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
        with open ('sample.txt', mode = 'r', encoding = 'UTF-8') as f:
            my_data = sorted(data, key = len)
            print(my_data)
        f.close()
cau3() 


# 4. Write a program to append a line to the sample.txt file with line is argument come from keyboard . print the length of file and
# the line with longest length.

def cau4(add):
    with open ('sample.txt', mode = 'r', encoding = 'UTF-8') as f:
        data = f.readlines()
        print(data)
        data.append(add)
        print(len(data))
        print(max(data))

add = "hello everyone"
cau4(add)

# 5. Write a program to count frequency yof each word in the sample.txt file.
#def count_word ():
def count_word():
    with open ('sample.txt', mode = 'r', encoding = 'UTF-8') as f:
        counts = dict()
        for line in f:
            words = line.split()
            print(words)
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1   
    print(counts)    
    f.close()

count_word()
  
# 6. write a program to remove a line which line number is a argument from the keyboard
with open ('sample.txt', mode = 'r', encoding = 'UTF-8') as f:
    my_file = f.readline()
num_line = int(input("Enter line remove: "))
with open ('sample.txt', mode = 'a', encoding = 'UTF-8') as f:
    for i,line in enumerate(my_file):
        if i != (num_line - 1):
            f.write(line)

print(my_file)

# 7. Write a program to store the following content in the file name sample_w.txt:
mess = r'''alo 1 2 3 4 5 6'''
with open ('sample.txt', mode = 'at', encoding = 'UTF-8') as f:
    f.writelines(mess)
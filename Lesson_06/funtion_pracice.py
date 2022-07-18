#1. define a funtion that accepts 2 values and returns its sum, division, sub,multi (use exception for division)

def caculator(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    print("sum = ", sum)
    print("sub = ",sub)
    print("mul = ", mul)
    try:
        div = a/b
        print("div = ", div)
    except:
        print("error!")
caculator(1,4)


#2. define a funtion to check whether a number keyboard is a square number.
def square_number(a):
    for i in range(a/2):
        if i*i == a:
            print(f"{a} is square number ")
            break
    else:
        print(f"{a} is not square number ")

square_number(64)

#3. define a funtion that accept 3 agrument ,then check whether exist a triangle which is created by them . return the result
def check_triangle(a,b,c):
    if a < b + c or b < a + c or c < b + a:
        print(f"{a}, {b}, {c} Forming a triangle. ")
    else:
        print(f"{a}, {b}, {c} don't form a triangle. ")

check_triangle(3,4,5)

#4. define a funtion that accept one string argument and return number of vowels and consonants
def check_vowels(string):
    vowels = 'aeiouAEIOU'
    consonants_string = []
    vowels_string = []
    for ch in string:
        if ch not in vowels and ch not in consonants_string:
            consonants_string.append(ch)
        elif ch not in vowels_string:
            vowels_string.append(ch)
    
    print(consonants_string)
    print(vowels_string)

check_vowels("hello everyone")

#5. define a funtion that accept a number (n )and return n first number of fibonacci sequences 

def number_fibonacci(n):
    if (n < 0):
        print ("Enter a positive number")
    else:
        f1, f2 = 0, 1
        if n == 1:
            print (f1)
        elif n == 2:
            print (f1,f2)
        else:
            print (f1,f2, end = ' ')
            for i in range (3, n+1):
                f3 = f1 + f2
                print (f3, end = ' ')
                f1 = f2
                f2 = f3
number_fibonacci(20)

#6. define a funtion taht accept a radius argument and return area and perimiter 
def area_perimi (radius):
    return print(f"area: {radius * radius * 3.14}, perimiter: {2 * 3.14 * radius}")

# 7. Define a function that accepts 2 arguments: first argument is a list of integers, second argument is a number with default value is 3.
# Repeat the list by the number, then calculate average of all items in the list.
def list_operations(list, n=2):
    list = list * n
    aveg = sum(list) / len(list)
    return aveg

print(list_operations([1,2,3], 2))
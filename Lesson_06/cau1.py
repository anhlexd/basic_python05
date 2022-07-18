def startup_message():
    print("The following instructions for disassembling an Acme laundry dryer")

def step1():
    print("Step 1: Unplug the dryer and move it away from the wall.")

def step2():
    print("Step 2: Remove the six screws from the back of the dryer.")

def step3():
    print("Step 3: Remove the dryer's back panel.")

def step4():
    print("Step 4: Pull the top of the dryer straight up.")

startup_message()
a = input("press Enter to see step 1: ")
a.lower()

if a == "enter" :
    step1()

b = input("press Enter to see step 2: ") 

if b == "enter" :
    step2()

c = input("press Enter to see step 3: ")
c.lower()

if c == "enter" :
    step3()

d = input("press Enter to see step 4: ")
d.lower()

if d == "enter" :
    step4()



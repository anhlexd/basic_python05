print("Get salary: ", end = '')
salary = int(input())

if salary < 30000:
    print("You must earn at least $30000 per year to qualify")
else:
    print("Get years_on_job: ", end ='')
    years_on_job = int(input())

    if years_on_job >= 2:
        print("You qualify for the loan")
    else:
        print("You must have been on your current job for at least two years to qualify")

print("Get the number of hours worked: ")
hour = int(input())
print("Get the hourly pay rate: ")
salary_hour = int(input())
if hour > 40:
    salary = salary_hour * (40 + (salary_hour - 40) * 1.5 )
    
else:
    salary = salary_hour * hour

print("Salary = {} VND".format(salary))
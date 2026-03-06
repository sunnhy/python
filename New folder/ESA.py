## Project - 1 : Employee Salary Analyzer

salaries = [25000, 30000, 28000, 40000, 50000]

Total_salary_expense = sum(salaries)
average_salary = Total_salary_expense / len(salaries)
minimum_salary = min(salaries)
maximum_salary = max(salaries)

def calculate_bonus(salary):
    if salary > 40000:
        return salary * 1.2 
    return salary * 1.1
    
bonus_salaries = [calculate_bonus(s)for s in salaries]
    
print(bonus_salaries)

for b in bonus_salaries:
    print(b)

# employees_g30000 = [salary for salary in salaries if salary > 30000]    #basic structure , not recommneded
# count_employees_g30000 = len(employees_g30000)

# count_of_g30000 = sum(1 for salary in salaries if salary > 30000)         #most advised way to do 
# print(count_of_g30000)

# print(count_employees_g30000)

# print(Total_salary_expense)
# print(average_salary)
# print(minimum_salary)
# print(maximum_salary)
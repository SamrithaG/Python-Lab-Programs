import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR'],
    'Salary': [50000, 60000, 55000, 70000, 52000]
}

df = pd.DataFrame(data)

print("Full DataFrame:\n")
print(df)

high_salary = df[df['Salary'] > 55000]
print("\nEmployees with Salary > 55000:\n")
print(high_salary)

it_department = df[df['Department'] == 'IT']
print("\nEmployees in IT Department:\n")
print(it_department)

it_high_salary = df[(df['Department'] == 'IT') & (df['Salary'] > 55000)]
print("\nIT Employees with Salary > 55000:\n")
print(it_high_salary)

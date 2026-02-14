name = input("Enter Employee Name: ")
hours = float(input("Enter total work hours: "))
rate = float(input("Enter hourly pay rate: "))

if hours <= 40:
    pay = hours * rate
    print(f"\nEmployee: {name}")
    print(f"Regular Hours Worked: {hours}")
    print(f"Pay: ${pay:.2f}")
else:
    regular_hours = 40
    overtime_hours = hours - 40
    overtime_rate = rate * 1.5
    regular_pay = regular_hours * rate
    overtime_pay = overtime_hours * overtime_rate
    total_pay = regular_pay + overtime_pay
    
    print(f"\nEmployee: {name}")
    print(f"Regular Hours: {regular_hours} | Overtime Hours: {overtime_hours}")
    print(f"Regular Pay: ${regular_pay:.2f}")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Total Pay: ${total_pay:.2f}")

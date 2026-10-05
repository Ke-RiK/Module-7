# Kirill Kaminskyi M7P4.py 10/5/2026

employee_count = 0
total_gross_pay = 0
#input
do_program = input("Do you want to do this program? ")

#process
do_program = do_program.lower()

while do_program == "yes":
    last_name = input("Enter your last name: ")
    hours_worked = int(input("Enter your hours worked: "))
    pay_rate = float(input("Enter your pay rate: "))


    if hours_worked > 40:
        gross_pay = (40 * pay_rate) + (hours_worked - 40) * (pay_rate * 1.5)
    else :
        gross_pay = hours_worked * pay_rate

    employee_count = employee_count + 1
    total_gross_pay = total_gross_pay + gross_pay


    print(f"Last Name: {last_name}")
    print(f"Gross pay: ${gross_pay:,.2f}")

    do_program = input("Do you want to do this program? ")
    do_program = do_program.lower()


average_pay  = total_gross_pay / employee_count

print (f"Employee Count: {employee_count}")
print (f"Total gross pay: {total_gross_pay:,.2f}")
print (f"Average pay: {average_pay:,.2f}")
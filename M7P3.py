# Kirill Kaminskyi M7P3.py 10/5/2026

student_count = 0
#input
continue_program = input("Do you want to continue? ")

#process
continue_program = continue_program.lower()

while continue_program == "yes":
    last_name = input("Enter your last name: ")
    exam_one = int(input("Enter your exam one score: "))
    exam_two = int(input("Enter your exam two score: "))
    average_score = (exam_one + exam_two) /2

    print (f"Last Name: {last_name}")
    print (f"Average score: %{average_score:,.2f}")

    student_count += 1

    continue_program = input("Do you want to continue? ")
    continue_program = continue_program.lower()

print (f"Student Count: {student_count}")





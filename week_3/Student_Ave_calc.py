while True:
    print("Student Average Mark Calculator")

    quiz1 = float(input("Enter first quiz mark: "))
    quiz2 = float(input("Enter second quiz mark: "))
    quiz3 = float(input("Enter third quiz mark: "))

    average = (quiz1 + quiz2 + quiz3) / 3

    print("Average mark:", average)

    if average >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

    another_student = input("Do you want to enter another student's marks? (yes/no): ")

    if another_student.lower() != "yes":
        print("Program ended.")
        break
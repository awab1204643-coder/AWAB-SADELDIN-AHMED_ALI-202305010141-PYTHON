def create_ticket():
    print("=== IT Helpdesk Ticket ===")

    student_name = input("Student Name: ")
    student_id = input("Student ID: ")
    issue = input("Issue: ")
    location = input("Location: ")
    priority = input("Priority (High/Medium/Low): ")

    if priority.lower() == "high":
        technician = "jibrel"
    elif priority.lower() == "medium":
        technician = "sami"
    elif priority.lower() == "low":
        technician = "izzad"
    else:
        print("Please choose a valid priority (High/Medium/Low).")
        return None

    status = "Pending"

    return (
        student_name,
        student_id,
        issue,
        location,
        priority,
        technician,
        status
    )

while True:
    student_name = input("Student Name: ")

    if student_name.replace(" ", "").isalpha() and len(student_name) >= 2:
        break
    else:
        print("Invalid name! Please enter your full name.")
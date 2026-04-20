


student_name = input("Enter student name: ")
course = input("Enter course: ")

total_classes = int(input("Enter total classes held: "))
attended_classes = int(input("Enter classes attended: "))


if total_classes <= 0:
    print("Total classes must be greater than 0")
elif attended_classes < 0 or attended_classes > total_classes:
    print("Invalid number of attended classes")
else:
   
    attendance_percentage = (attended_classes / total_classes) * 100

   
    print("\nAttendance Report")
    print("Name:", student_name)
    print("Course:", course)
    print("Attendance:", round(attendance_percentage, 2), "%")

    
    if attendance_percentage >= 75:
        print("Status: Allowed for exam")
    else:
        print("Status: Not allowed for exam")

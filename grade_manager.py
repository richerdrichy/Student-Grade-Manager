
# 1. Student storage
students = []


# 2. Calculate grade
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# 3. Add student
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    while True:
        try:
            mark = float(input("Enter mark (0-100): "))

            if 0 <= mark <= 100:
                break

            print("Mark must be between 0 and 100.")

        except ValueError:
            print("Invalid input! Enter a number.")

    grade = get_grade(mark)

    students.append({
        "name": name,
        "mark": mark,
        "grade": grade
    })

    print("Student added successfully!")


# 4. Show results
def show_results():
    if not students:
        print("No students added yet.")
        return

    print("\n" + "=" * 40)
    print("{:<20} {:<10} {:<10}".format(
        "NAME", "MARK", "GRADE"
    ))
    print("-" * 40)

    for student in students:
        print("{:<20} {:<10.2f} {:<10}".format(
            student["name"],
            student["mark"],
            student["grade"]
        ))

    marks = [student["mark"] for student in students]

    print("=" * 40)
    print(f"Class Average: {sum(marks) / len(marks):.2f}")
    print(f"Highest Mark: {max(marks):.2f}")
    print(f"Lowest Mark:  {min(marks):.2f}")
    print(f"Total Students: {len(students)}")


# 5. Menu loop
while True:
    print("\n===== STUDENT GRADE MANAGER =====")
    print("1. Add Student")
    print("2. Show Results")
    print("3. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        show_results()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose 1, 2, or 3.")

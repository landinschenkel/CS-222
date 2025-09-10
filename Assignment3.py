def load_students(filename):
    """Load student data from a file into a dictionary."""
    students = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    studentId, lastName, firstName, major, gpa = line.split(',')
                    students[studentId] = [lastName, firstName, major, gpa]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)
    return students

def search_by_last_name(students, last_name):
    """Search students by last name and print matching records."""
    found = False
    for studentId, info in students.items():
        if info[0].lower() == last_name.lower():
            print(f"{studentId}, {info[0]}, {info[1]}, {info[2]}, {info[3]}")
            found = True
    if not found:
        print("No students found with that last name.")

def search_by_major(students, major):
    """Search students by major and print matching records."""
    found = False
    for studentId, info in students.items():
        if info[2].lower() == major.lower():
            print(f"{studentId}, {info[0]}, {info[1]}, {info[2]}, {info[3]}")
            found = True
    if not found:
        print("No students found with that major.")

def main():
    filename = "students.txt"
    students = load_students(filename)

    while True:
        print("\nChoose an option:")
        print("1) Search by Last Name")
        print("2) Search by Major")
        print("3) Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            last_name = input("Enter last name to search for: ")
            search_by_last_name(students, last_name)
        elif choice == '2':
            major = input("Enter major to search for: ")
            search_by_major(students, major)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

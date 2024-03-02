class Student:
    # object
    def __init__(self, name, stu_num, num_courses):
        self.name = name
        self.stu_num = stu_num
        self.num_courses = num_courses

    # udpates to new student
    def update_name(self, updated_s_name):
        self.name = updated_s_name

    # prints student info
    def print_student(self):
        print("Student:")
        print(f"Name: {self.name}")
        print(f"Student Number: {self.stu_num}")
        print(f"Number of Courses: {self.num_courses}")

if __name__ == "__main__":
    # first input
    name = input("Enter student name: ")
    stu_num = input("Enter student number: ")
    num_courses = int(input("Enter number of courses: "))

    # student object
    student_object = Student(name, stu_num, num_courses)

    while True:
        print("\nCurrent Student:")
        student_object.print_student()

        # input for case switch
        print("Options: ")
        print(" ")
        print("1. Update Name")
        print("2. Exit")

        # user choice
        user_choice = input("Enter your choice 1 or 2): ")

        if user_choice == "1":
            updated_s_name = input("Enter new student name: ")
            student_object.update_name(updated_s_name)
            
        elif user_choice == "2":
            print("Done")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

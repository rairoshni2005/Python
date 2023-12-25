class Student:
    # Class variable to keep track of the total number of students
    total_students = 0

    def __init__(self, name, department):
        self.name = name
        self.department = department

        # Increment the total_students count when a new student is created
        Student.total_students += 1

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Department: {self.department}")
        print()

# Example usage:
# Create instances of Student class for different students
student1 = Student(name="John Doe", department="PGDM")
student2 = Student(name="Jane Smith", department="BTech")
student3 = Student(name="Alice Johnson", department="BTech")

# Display details of each student
print("Details of Admitted Students:")
student1.display_details()
student2.display_details()
student3.display_details()

# Display the total number of students
print(f"Total Students Admitted: {Student.total_students}")

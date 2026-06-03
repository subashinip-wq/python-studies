def get_details():
    student_name = input("Enter Student Name: ")
    course = input("Enter Course Name: ")
    city = input("Enter City: ")

    return student_name, course, city


def print_details(student_name, course, city):
    print("\n--- Admission Details ---")
    print(f"Student Name : {student_name}")
    print(f"Course       : {course}")
    print(f"City         : {city}")


student_name, course, city = get_details()
print_details(student_name, course, city)

EXERCISE 1:

name = "Ravi Kumar"
area = "Chennai"
course = "BCA"

print(f"Admission: {course} in {area} by {name}")

EXERCISE 2:

def check_marksheet_uploaded(marksheet_uploaded):
    if marksheet_uploaded:
        print("Marksheet attached ✓")
    else:
        print("No marksheet — please upload one")

check_marksheet_uploaded(True)
check_marksheet_uploaded(False)

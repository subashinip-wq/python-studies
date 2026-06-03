def validate_admission(name, city, course):
    if name == "" or city == "" or course == "":
        print("Error: All fields are required!")
        return False

    print("Admission form is valid.")
    return True

validate_admission("suba", "Chennai", "AIML")   # valid
validate_admission("", "Chennai", "BCA")       # invalid

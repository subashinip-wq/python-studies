ADDING A ITEMS:

patients = ["jeevi"]
patients.append("kanya")
patients.insert(0, "karthika")

print(patients)

FUNCTION WITH LIST:
def show_patients(patient_list):
    print("Total Patients:", len(patient_list))

    for patient in patient_list:
        print("-", patient)

my_patients = ["Priya", "Ravi", "Kiran"]

show_patients(my_patients)

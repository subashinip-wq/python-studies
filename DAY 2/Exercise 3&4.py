EXERCISE 3:

pending_patients = []
pending_patients.append("Priya")
pending_patients.append("Ravi")
pending_patients.append("Kiran")

print("Total Patients:", len(pending_patients))
pending_patients.pop(1)
print(pending_patients)

EXERCISE 4:

patients = [
    {"city":"Chennai","name":"Priya"},
    {"city":"Madurai","name":"Ravi"},
    {"city":"Chennai","name":"Kiran"}
]
for patient in patients:
    if patient["city"] == "Chennai":
        print(patient["name"])

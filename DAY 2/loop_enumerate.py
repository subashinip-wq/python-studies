loop:

patients = ["Priya", "Ravi", "Kiran"]

for patient in patients:
    print("Patient:", patient)

ENUMERATE:

patients = ["Priya", "Ravi", "Kiran"]

for index, patient in enumerate(patients, start=1):
    print(f"{index}. {patient}")

WHILE LOOP:
count = 0
max_patients = 3

while count < max_patients:
    print(f"Registering Patient #{count+1}")
    count += 1

print("Registration Closed")

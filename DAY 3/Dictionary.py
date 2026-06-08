patient = {
    "patient_name": "Priya",
    "age": 25,
    "hospital": "City Hospital",
    "disease": "Fever",
    "admitted": False
}

print(patient)

Accessing Values:

print(patient["patient_name"])      # Priya
print(patient["disease"])           # Fever
print(patient.get("room", "Not Assigned"))

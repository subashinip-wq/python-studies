patients = [
    {"id": 1, "name": "Priya", "disease": "Fever"},
    {"id": 2, "name": "Ravi", "disease": "Cough"},
    {"id": 3, "name": "Kiran", "disease": "Cold"}
]

for p in patients:
    print(f"[{p['id']}] {p['name']} - {p['disease']}")

Function Returning a Dictionary:

def register_patient(name, age, disease):
    return {
        "name": name,
        "age": age,
        "disease": disease
    }

patient = register_patient("Anbu", 22, "Headache")

print(patient)

def register_patient(name, age, disease):
    return {
        "name": name,
        "age": age,
        "disease": disease
    }

patient = register_patient("Anbu", 22, "Headache")

print(patient)

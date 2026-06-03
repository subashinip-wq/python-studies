def create_student_id(name, course):
    student_id = name[:3].upper() + "_" + course[:3].upper()
    return student_id

id1 = create_student_id("Ravi Kumar", "BCA")
id2 = create_student_id("Priya", "BSc")

print(id1)   # RAV_BCA
print(id2)   # PRI_BSC

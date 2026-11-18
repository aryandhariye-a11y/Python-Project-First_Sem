def display_menu():
    print("\n--- Hospital Management System ---")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient by ID")
    print("4. Update Patient Details")
    print("5. Delete Patient")
    print("6. Exit")

def add_patient(patients, next_id_num):
    patient_id = f"P{next_id_num:03d}"
    
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty. Patient not added.")
        return next_id_num

    age_input = input("Age: ").strip()
    try:
        age = int(age_input)
        if age < 0 or age > 120:
            print("Invalid age. Enter a number between 0 and 120.")
            print("Patient not added.")
            return next_id_num
    except ValueError:
        print("Invalid age. Enter a number between 0 and 120.")
        print("Patient not added.")
        return next_id_num

    disease = input("Disease: ").strip()
    doctor = input("Doctor: ").strip()

    patients[patient_id] = {
        "Name": name,
        "Age": age,
        "Disease": disease,
        "Doctor": doctor
    }

    print(f"Patient added. ID: {patient_id} | {name} | {age} | {disease} | {doctor}")
    return next_id_num + 1

def view_patients(patients):
    if not patients:
        print("No patient records found.")
        return
    
    for pid, details in patients.items():
        print(f"ID: {pid} | {details['Name']} | {details['Age']} | {details['Disease']} | {details['Doctor']}")

def search_patient(patients):
    patient_id = input("Enter Patient ID to search: ").strip()
    if patient_id in patients:
        details = patients[patient_id]
        print(f"ID: {patient_id} | {details['Name']} | {details['Age']} | {details['Disease']} | {details['Doctor']}")
    else:
        print(f"Patient ID {patient_id} not found.")

def update_patient(patients):
    patient_id = input("Enter Patient ID to update: ").strip()
    if patient_id not in patients:
        print(f"Patient ID {patient_id} not found.")
        return

    print("Leave field blank if you do not want to change it.")
    
    name = input(f"New Name [{patients[patient_id]['Name']}]: ").strip()
    if name:
        patients[patient_id]['Name'] = name

    age_input = input(f"New Age [{patients[patient_id]['Age']}]: ").strip()
    if age_input:
        try:
            age = int(age_input)
            if 0 <= age <= 120:
                patients[patient_id]['Age'] = age
            else:
                print("Invalid age range. Age not updated.")
        except ValueError:
            print("Invalid age format. Age not updated.")

    disease = input(f"New Disease [{patients[patient_id]['Disease']}]: ").strip()
    if disease:
        patients[patient_id]['Disease'] = disease

    doctor = input(f"New Doctor [{patients[patient_id]['Doctor']}]: ").strip()
    if doctor:
        patients[patient_id]['Doctor'] = doctor

    details = patients[patient_id]
    print(f"Patient {patient_id} updated. Disease: {details['Disease']}")

def delete_patient(patients):
    patient_id = input("Enter Patient ID to delete: ").strip()
    if patient_id in patients:
        del patients[patient_id]
        print(f"Patient {patient_id} deleted. Total patients: {len(patients)}")
    else:
        print(f"Patient ID {patient_id} not found.")

def main():
    patients = {}
    next_id_num = 101  # Patient IDs start from P101

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            next_id_num = add_patient(patients, next_id_num)
        elif choice == '2':
            view_patients(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            update_patient(patients)
        elif choice == '5':
            delete_patient(patients)
        elif choice == '6':
            print("Exiting Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
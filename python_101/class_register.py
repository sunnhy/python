
students = {}
while True:
    print(f"1.Add Student")
    print(f"2. View Students")
    print(f"3. Remove Student")
    print(f"4.Exit")
    choice = input("\nEnter choice number: ")
    if choice == "1":
        name = input("Enter the name of the student: ")
        if name in students:
            print(f"Student Already exist!")
        else:
            students[name] = True
            print(f"Students name added succesfully.")
    elif choice == "2":
        print(f"\n2025th batch:")
        if not students:
            print("No students found.")      
        else:
            for name in students:
                print(name)
    elif choice == "3":
        name = input("\nEnter the student name to remove: ")
        if name in students:
            del students[name]
            print(f"\nStudent removed successfully!!")
        else:
            print(f"\nStudent not found")
    elif choice == "4":
        print(f"\nExiting the program")
        break
    else:
        print(f"\nInvalid Choice")


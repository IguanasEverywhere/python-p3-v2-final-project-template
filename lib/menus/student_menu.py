def student_menu():
    active = True
    while active:
        print("Student options...")
        choice = input(">> ")
        if choice == "0":
            active = False
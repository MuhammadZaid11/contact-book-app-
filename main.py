contacts = {}
while True:
    print("\n Create Book App")
    print("1. create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. count contact")
    print("7. Exit")

    choice = int(input("Enter your choice = "))

    if choice == 1:
        name = input("Enter the Name = ")
        if name in contacts:
            print(f"contect name {name} already exists ! ")
        else:
            age = input("Enter age = ")
            Email = input("Enter Email = ")
            Mobile = input("Enter Mobile number = ")
            contacts[name] = {"Age":int(age),"email":Email,"mobiel number":Mobile}
            print(f"conter name {name} has been created successuflly !")

    elif choice == 2 :
        name = input("Enter the name to view = ")
        if name is contacts:
            contacts = contacts[name]
            print(f"Name : {name}, age : {age} , Mobile Number : {Mobile}")
        else:
            print("contact not found!")

    elif choice == 3:
        name = input("Enter the name to update contact =")
        if name in contacts:
            age = input("Enter age = ")
            Email = input("Enter Email = ")
            Mobile = input("Enter Mobile number = ")
            contacts[name] = {"Age":int(age),"email":Email,"mobiel number":Mobile}
        else:
            print("contact not found!")
    elif choice == 4 :
        name = input("Enter the name to deleted contact =")
        if name in contacts:
            del contacts[name]
            print(f"contact name {name} has been deleted successfully!")
        else:
            print("contact not found!")

    elif choice == 5 :
        search_name = input("enter the contacts name to search = ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"found -name {name},age :{age}, mobile number :{Mobile},email:{Email}")
                found = True
            if not found:
                print("no contact found with that name")

        
    elif choice == 6 :
        print(f"Total contacts in your book : {len(contacts)}")

    elif choice == 7 :
        print("Good bye ... closibg the program")

        break

    else:
        print("Invalid input")

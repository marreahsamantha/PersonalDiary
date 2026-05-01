# Task A - Create
def create_file():
    try:
        file = open("Diary.txt", "x")
        print("File Created Successfully!!!")
        file.close()
    except FileExistsError:
        print("File already Exist")

# Task B - Append
def append_entry():
    try:
        date = input("Enter date: ")
        entry = input("Write your diary entry: ")

        file = open("diary.txt", "a")
        file.write(f"[{date}] {entry}\n")
        file.close()

        print("Entry added!")

    except Exception as e:
        print("Error:", e)

# Task C - Read
def read_entries():
    try:
        file = open("diary.txt", "r")
        lines = file.readlines()

        print("\n--- Diary Entries ---")
        for line in lines:
            print(line.strip())

        print(f"\nTotal entries: {len(lines)}")
        file.close()

    except FileNotFoundError:
        print("Diary file not found.")
    except Exception as e:
        print("Error:", e)

# Task D - Update
def update_entry():
    try:
        date_to_update = input("Enter date to update: ")
        file = open("diary.txt", "r")
        lines = file.readlines()
        file.close()
        file = open("diary.txt", "w")

        found = False
        for line in lines:
            if date_to_update in line:
                new_entry = input("Enter new entry: ")
                file.write(f"[{date_to_update}] {new_entry}\n")
                found = True
            else:
                file.write(line)

        file.close()

        if found:
            print("Entry updated!")
        else:
            print("Date not found.")

    except FileNotFoundError:
        print("Diary file not found.")
    except Exception as e:
        print("Error:", e)

#Search
def search_entry():
    try:
        keyword = input("Enter keyword/date to search: ")
        file = open("diary.txt", "r")
        found = False

        for line in file:
            if keyword.lower() in line.lower():
                print("Found:", line.strip())
                found = True

        if not found:
            print("No entry found.")
        file.close()

    except FileNotFoundError:
        print("Diary file not found.")
    except Exception as e:
        print("Error:", e)

#Delete
def delete_entry():
    try:
        date_to_delete = input("Enter date to delete: ")

        file = open("diary.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("diary.txt", "w")

        found = False
        for line in lines:
            if date_to_delete not in line:
                file.write(line)
            else:
                found = True

        file.close()

        if found:
            print("Entry deleted!")
        else:
            print("Date not found.")

    except FileNotFoundError:
        print("Diary file not found.")
    except Exception as e:
        print("Error:", e)


#Main Menu
create_file()


while True:
    print("\n==== PERSONAL DIARY MENU ====")
    print("1. Append Entry")
    print("2. Read Entries")
    print("3. Update Entry")
    print("4. Search Entry")
    print("5. Delete Entry")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        append_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        update_entry()
    elif choice == "4":
        search_entry()
    elif choice == "5":
        delete_entry()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")

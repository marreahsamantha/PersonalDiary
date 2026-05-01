def x_mode():
    try:
        file = open("Diary.txt", "x")
        print("File Created Successfully!!!")
        file.close()
    except FileExistsError:
        print("File already Exist")

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


# ---------- MAIN MENU ----------
create_file()

while True:
    print("\n==== PERSONAL DIARY MENU ====")
    print("1. Write (Overwrite)")
    print("2. Append Entry")
    print("3. Read Entries")
    print("4. Update Entry")
    print("5. Search Entry")
    print("6. Delete Entry")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        write_entry()
    elif choice == "2":
        append_entry()
    elif choice == "3":
        read_entries()
    elif choice == "4":
        update_entry()
    elif choice == "5":
        search_entry()
    elif choice == "6":
        delete_entry()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")
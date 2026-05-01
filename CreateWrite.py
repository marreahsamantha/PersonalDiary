def x_mode():
    try:
        file = open("Diary.txt", "x")
        print("File Created Successfully!!!")
        file.close()
    except FileExistsError:
        print("File already Exist")

def a_mode():
    try:
        date = input("Enter date: ")
        entry = input("Write your diary entry: ")

        file = open("diary.txt", "a")
        file.write(f"[{date}] {entry}\n")
        file.close()

        print("Entry added!")

    except Exception as e:
        print("Error:", e)
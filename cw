#Create
def create_file():
    try:
        file = open("Diary.txt", "x")
        print("File Created Successfully!!!")
        file.close()
    except FileExistsError:
        print("File already Exist")

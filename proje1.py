student = {}

while True:
    print("1) Add student")
    print("2) Show all students")
    print("3) Show score of one student")
    print("4) Remove student")
    print("5) Show average scores")
    print("0) Exit")

    print("_" * 20)

    option = input("Enter Your Option : ")

    print("_" * 20)

    match option:
        case "1":
            name = input("Enter student name: ")
            score = int(input("Enter student score: "))
            student[name] = {
                "name" : name,
                "score" : score
            }
            print("Student successfully added")
        case "2":
            for name in student:
                info = student[name]
                print(f"name:{name} : score:{info['score']}")
        case "3":
            student_name = input("Enter student name: ")
            if student_name in student:
                print(f"name:{student_name} : score:{student[student_name] ['score']}")
            else:
                print("Student not found")
        case "4":
            remove = input("Enter student you like to remove: ")
            if remove in student:
                del student[remove]
                print(f"Student {remove} successfully removed")
            else:
                print("Student not found")

        case "5":
            if len(student) > 0:
                total = 0
                for info in student.values():
                    total += info["score"]
                count = len(student)
                average = total / count
                print(f"Average score: {average}")
            else:
                print("not student in the list to calculate average score")
        case "0":
            break
        case _:
            print("Error: Invalid Option")
    print("_" * 20)
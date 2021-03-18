"""
This file is used to read and write data to pickle file
"""

__all__ = ["storeData", 'loadData']


import pickle


def storeData():
    try:
        with open("students_data.pkl", 'rb') as student_data:
            students = pickle.load(student_data)

    except FileNotFoundError:
        # creating a new dict if file is doesn't exist
        students = dict()

    name = input("\nEnter Student's Name: ")
    f_name = input("Enter Student's Father Name: ")
    roll_no = input("Enter Student's Roll No: ")
    maths = int(input("Enter Student's Mathematics marks: "))
    english = int(input("Enter Student's English marks: "))
    science = int(input("Enter Student's Science marks: "))

    total = int(english) + int(maths) + int(science)
    percentage = round(int(total) / 3, 2)

    if roll_no in students:
        print("Editing previous data")
        students[roll_no] = [name, f_name, maths, english, science, total, percentage]

    else:
        students[roll_no] = [name, f_name, maths, english, science, total, percentage]

    with open("students_data.pkl", 'wb') as student_data:
        students = {key: value for key, value in
                    sorted(students.items(), key=lambda item: item[1][-1], reverse=True)}

        pickle.dump(students, student_data)


def loadData(entity):
    with open("students_data.pkl", 'rb') as student_data:
        students = pickle.load(student_data)

        students = list(students.items())

        for i in range(len(students)):
            if entity == students[i][0] or entity.upper() == students[i][1][0].upper():
                print("\n")
                print("=" * 50)
                print("Ethans Public School".center(50))
                print("=" * 50)
                print("Student Name : ", students[i][1][0])
                print("Father Name  : ", students[i][1][1])
                print("Roll Number  : ", int(students[i][0]))
                print('-' * 50)
                print("English      : ", students[i][1][2])
                print("Maths        : ", students[i][1][3])
                print("Science      : ", students[i][1][4])
                print("-" * 50)
                print("Total Marks  : ", students[i][1][5])
                print("Percentage   : ", students[i][1][6])
                print("Rank         : ", i+1)
                break
        else:
            print("Data not Found")
            close = input("\nPress Q to exit.")
            exit()

"""
This file is used to read and write data to csv file
"""

__all__ = ["storeData", 'loadData']


import csv


def storeData():
    with open("Data.csv", 'a') as data:
        name = input("Enter Student's Name: ")
        f_name = input("Enter Student's Father Name: ")
        roll_no = input("Enter Student's Roll No: ")
        maths = input("Enter Student's Mathematics marks: ")
        english = input("Enter Student's English marks: ")
        science = input("Enter Student's Science marks: ")

        student = {'Name': name, 'F_name': f_name, "Roll_no": roll_no,
                   'Maths': maths, 'English': english, 'Science': science}

        fields = ['Name', 'F_name', "Roll_no", 'Maths', 'English', 'Science']

        writer = csv.DictWriter(data, fieldnames=fields)

        # writer.writeheader()
        
        writer.writerow(student)


def loadData(entity):
    with open("Data.csv", 'r') as data:
        reader = csv.DictReader(data)
        for student in reader:
            if student['Roll_no'] == entity or student['Name'].upper() == entity.upper():
                print("=" * 50)
                print("Ethans Public School".center(50))
                print("=" * 50)
                print("Student Name : ", student['Name'])
                print("Father Name  : ", student['F_name'])
                print("Roll Number  : ", student['Roll_no'])
                print('-' * 50)
                print("English      : ", student['English'])
                print("Maths        : ", student['Maths'])
                print("Science      : ", student['Science'])
                print("-" * 50)
                total = int(student['English']) + int(student['Maths']) + int(student['Science'])
                print("Total Marks  : ", total)
                print("Percentage   : ", round(int(total) / 3, 2))
                print("Rank         : ",)
                break
        else:
            print("Data not Found")
            exit()

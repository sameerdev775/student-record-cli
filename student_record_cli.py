def add_student(student,math,english,phy):
    total_marks1 = (math+english+phy)
    percentage = round((total_marks1*100)/300 , 2)

    if percentage>=90:
            grade = "A"

    elif 90>percentage>=75:
            grade = "B"

    elif 75>percentage>=60:
            grade = "C"

    elif percentage<60:
            grade = "F"

    with open("record4.txt","a") as f1:
        f1.write(f"{student},{math},{english},{phy},{percentage},{grade}\n")

    print("\n")
    return

def view_student():
    with open("record4.txt","r") as f2:
        data = f2.readlines()
        a=1
        for i in data:
                i2 = i.replace(","," ").split()
                print(f"{a}. {i2[0]} -> {i2[4]} -> {i2[5]}")
                a+=1
    print("\n")

while True:
    data = (input("1. Add student\n2. View students\n3. Exit\n\nChoose your option:"))

    try:
        num = int(data)
        if num==1:
            student = input("Enter the name:")
            math = int(input("Enter the marks:"))
            english = int(input("Enter the marks:"))
            phy = int(input("Enter the marks:"))
            add_student(student,math,english,phy)

        elif num==2:
            view_student()
        elif num==3:
            break
        else:
            print("Pls enter a given option\n")

    except ValueError as e:
        print("You entered a wrong option\n")

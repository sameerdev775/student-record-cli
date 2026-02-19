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
        f1.write(f"\n{student},{math},{english},{phy},{percentage},{grade}")

    print("\n")
    return

def view_student():
    with open("record4.txt","r") as f2:
        data = f2.readlines()
        a = 1 
        for i in data:
          i2 = i.replace(","," ").split()
          priniting(a,i2)
          a+=1
        else: 
             print("\n")
        


def data_collection():
     with open("record4.txt","r") as f2:
        data = f2.readlines()
        list1 = []
        for i in data:
                i2 = i.replace(","," ").split()
                i3 = []
                # for j in i2:
                #      if j.isalpha():
                #           i3.append(j)

                #      elif j.isnumeric():
                #           i3.append(int(j))

                #      else:
                #           try:
                #                i3.append(float(j))

                #           except ValueError as e:
                #                continue

                i3.append(i2[0])
                i3.append(int(i2[1]))
                i3.append(int(i2[2]))
                i3.append(int(i2[3]))
                i3.append(float(i2[4]))
                i3.append(i2[5])
                          
                     
                list1.append(i3)
        return list1
     
def find_student(student):
    student_details = data_collection()
    flag = False
    
    for i in student_details:
        if student in i:
            priniting(1,i)
            flag = True

    if flag==False:
         print("Student Not Found")

    else:
        print("\n")

def topper():
     data = data_collection()
     percent_list = []

     for i in data:
        percent_list.append(i[4])

     greatest = percent_list[0]
     for j in percent_list:
          if j>greatest:
               greatest=j
     a = 1
     for m in data:
          if greatest in m:
               priniting(a,m)
               a+=1

     else:
          print("\n")

def priniting(a,data):
        print(f"{a}. {data[0]} -> {data[4]} -> {data[5]}")

def delete(student):
     data = data_collection()

     new_data = []   
     for i in data:
          if student in i:
               continue
          else:
               new_data.append(i)

     with open("record4.txt","w") as f:
          for j in new_data:
               f.write(f"{ ",".join(str(item) for item in j)}")

               if j==new_data[-1]:
                    continue
               else:
                    f.write("\n")

while True:
    data = (input("1. Add student\n2. View students\n3. Exit\n4. Search a Student\n5. Find the Topper\n6. Delete a student\n\nChoose your option:"))

    try:
        num = int(data)
        if num==1:
            student = input("Enter the name:")
            math = int(input("Enter the marks:"))
            english = int(input("Enter the marks:"))
            phy = int(input("Enter the marks:"))
            add_student(student,math,english,phy)

        elif num==2:
            print("\n")
            view_student()
        elif num==3:
            break
        elif num==4:
             student = input("Enter the name:")
             find_student(student)
        elif num==5:
             topper()
        elif num==6:
             student = input("Enter the name:")
             delete(student)
        else:
            print("Pls enter a given option\n")

    except ValueError as e:
        print("You entered a wrong option\n")

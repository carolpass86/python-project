from PythonProject.cvs_exercise.common.course_name import COURSE_NAME_LIST
from PythonProject.cvs_exercise.store.cvs_store import save_data



def process_list(student_data):
    records = list(student_data.values())
    records.sort(key=lambda a:a.get("name"))
    for record in records:
        print(record.get("name"))
        for course in COURSE_NAME_LIST:
            course_key = course+"_score"
            print(f"{course} record:{record.get(course_key)}")

        print(" ")

def get_score(subject):
    while True:
        try:
            score =input(f"please input your {subject} score:")
            return float(score)
        except ValueError:
            print("your input is wrong .please input a number")



def process_add(student_data):
    name = input("please input your name:")
    chinese_score =get_score("chinese")
    english_score = get_score("english")
    math_score = get_score("math")
    student_data[name] = {
        "name":name,
        "chinese_score":chinese_score,
        "english_score":english_score,
        "math_score":math_score
    }
    print("you added successfully")



def process_del(student_data):
    name = input("please input the name you want to delete:")
    result = student_data.pop(name,None)
    if result :
        save_data(student_data)
        print(f"you deleted {name} successfully")
    else:
        print(f"{name} not exist")
    # if name in student_data.keys():
    #      student_data.pop(name)
    #      print(f"delete {name} successfully")
    # else:
    #   print(f"{name} not exist")



def process_edit(student_data):
    name = input("please input the student's name :")
    if name in student_data:
        course =input("please input the course's name:")
        if course in COURSE_NAME_LIST:

           new_score = get_score(course)
           course_key = course+"_score"
           student_data[name][course_key]=new_score
           # print("Before:", student_data[name])
           # print("course:", repr(course))
           # print("new_score:", new_score)
           #
           # student_data[name].update({course: new_score})
           #
           # print("After:", student_data[name])
           save_data(student_data)
           print("edit score successfully")

        else:
            print("course is not exist,please input the correct course name")
    else:
      print("student not exist")

def process_ave(student_data):
    pass



def process_command(cmd:str,student_data:dict):
    if cmd =="list":
        process_list(student_data)
    elif cmd == "add":
        process_add(student_data)
    elif cmd == "delete":
        process_del(student_data)
    elif cmd == "edit":
        process_edit(student_data)
    elif cmd == "exit":
        exit()
    elif cmd == "average":
        process_ave()
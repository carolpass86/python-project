import csv
import os
from PythonProject.cvs_exercise.common.course_name import COURSE_NAME_LIST


def load_data()->dict:
    file ='student.csv'
    result = {}
    if os.path.exists(file):
        with open(file,mode="r",encoding="utf-8") as file_instance:
            file_reader = csv.DictReader(file_instance)

            for row in file_reader:
                name = row.get("name")
                result[name] = row
    return result

def save_data(data:dict):
    file_instance = "student.csv"
    if not data:
        return

    with open(file_instance,mode="w",encoding="utf-8") as f:
        rows = list(data.values())
        headers = ["name"] +[course+ "_score" for course in COURSE_NAME_LIST]
        writer = csv.DictWriter(f,
                                fieldnames = headers )
        writer.writeheader()
        writer.writerows(rows)



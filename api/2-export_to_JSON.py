#!/usr/bin/python3
""" exports data in json format """
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]
    user = requests.get(url + "/users/{}".format(employee_id)).json()
    todos = requests.get(url + "/users/" + employee_id + "/todos").json()

    task_details = [{"task": todo["title"], "completed": todo["completed"],
                    "username": user["username"]} for todo in todos]
    employee_data = {employee_id: task_details}

    with open(f"{employee_id}.json", "w") as outfile:
        json.dump(employee_data, outfile)

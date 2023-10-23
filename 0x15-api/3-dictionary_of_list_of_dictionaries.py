#!/usr/bin/python3
"""
This module contains python functions used to explore the jsonplaceholder
typicode api
"""

import csv
import json
import requests


def emps_to_json():
    """
    send a request to the api url, get all employee todo info and
    write it to a json file
    """
    employeeUrl = f"https://jsonplaceholder.typicode.com/users"
    employeeResp = requests.get(employeeUrl)
    employees = employeeResp.json()
    todoUrl = f"https://jsonplaceholder.typicode.com/todos"
    todoResp = requests.get(todoUrl)
    todos = todoResp.json()
    output = {}
    for employee in employees:
        emp_id = employee["id"]
        output.update({emp_id: [{"username": employee['username'],
                                 "task": todo['title'],
                                 "completed": todo['completed']}
                                for todo in todos
                                if todo["userId"] == emp_id]})
    with open("todo_all_employees.json", "w", newline="") as fileObj:
        json.dump(output, fileObj)


if __name__ == "__main__":
    emps_to_json()

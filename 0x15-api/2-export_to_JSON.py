#!/usr/bin/python3
"""
This module contains python functions used to explore the jsonplaceholder
typicode api
"""

import json
import requests
import sys


def emp_to_json(emp_id):
    """
    send a request to the api url, get employee todo info and write to
    json file
    """
    employeeUrl = f"https://jsonplaceholder.typicode.com/users?id={emp_id}"
    todoUrl = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    employeeResp = requests.get(employeeUrl)
    todoResp = requests.get(todoUrl)
    employee, todos = employeeResp.json(), todoResp.json()
    with open(f"{emp_id}.json", "w", newline="") as fileObj:
        output = {emp_id: [{"task": todo['title'],
                            "completed": todo['completed'],
                            "username": employee[0]['username']}
                           for todo in todos]}
        json.dump(output, fileObj)


if __name__ == "__main__":
    emp_to_json(sys.argv[1])

#!/usr/bin/python3
"""
This module contains python functions used to explore the jsonplaceholder
typicode api
"""

import csv
import requests
import sys


def emp_to_csv(emp_id):
    """
    send a request to the api url, get employee todo info and display a
    custom message to the stdout
    """
    employeeUrl = f"https://jsonplaceholder.typicode.com/users?id={emp_id}"
    todoUrl = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    employeeResp = requests.get(employeeUrl)
    todoResp = requests.get(todoUrl)
    employee, todos = employeeResp.json(), todoResp.json()
    with open(f"{emp_id}.csv", "w", newline="") as fileObj:
        writerObj = csv.writer(fileObj, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writerObj.writerow([emp_id,
                                employee[0].get("username"),
                                todo.get("completed"),
                                todo.get("title")])


if __name__ == "__main__":
    emp_to_csv(sys.argv[1])

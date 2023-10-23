#!/usr/bin/python3
"""
This module contains python functions used to explore the jsonplaceholder
typicode api
"""
import requests
import sys


def display_info(emp_id):
    """
    send a request to the api url, get employee todo info and display a
    custom message to the stdout
    """
    employeeUrl = f"https://jsonplaceholder.typicode.com/users?id={emp_id}"
    todoUrl = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    employeeResp = requests.get(employeeUrl)
    todoResp = requests.get(todoUrl)
    employee, todos = employeeResp.json(), todoResp.json()
    titles = [todo.get("title") for todo in todos if todo.get("completed")]
    header = f"Employee {employee[0].get('name')} is done with"\
        f"tasks({len(titles)}/{len(todos)}):"
    print(header)
    for title in titles:
        print(f"\t {title}")


if __name__ == "__main__":
    display_info(sys.argv[1])

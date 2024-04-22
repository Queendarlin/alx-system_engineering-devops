#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys


if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID
    employee_id = int(sys.argv[1])
    user_response = requests.get(url + "users/{}".format(employee_id)).json()

    # Get the to-do list for the employee using the provided employee ID
    parameter = {"userId": employee_id}
    todos = requests.get(url + "todos", parameter).json()

    # Filter completed tasks and count them
    completed_tasks = [tasks.get("title") for tasks in todos
                       if tasks.get("completed") is True]

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user_response.get("name"), len(completed_tasks), len(todos)))

    # Print the completed tasks one by one with indentation
    [print("\t {}".format(complete)) for complete in completed_tasks]

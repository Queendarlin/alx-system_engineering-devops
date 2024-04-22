#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from the API and convert the response to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    # Fetch the to-do list items associated with the given user ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Create a dictionary to store the tasks in JSON format
    tasks_json = {user_id: [{"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": username} for task in todos]}

    # Write the JSON data to a file named after the user ID
    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(tasks_json, json_file)

    print("Tasks exported to {}.json successfully.".format(user_id))

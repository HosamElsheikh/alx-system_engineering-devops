#!/usr/bin/python3
"""
Fetches TODO list progress of an employee using JSONPlaceholder API.
"""

import requests
import sys

if __name__ == "__main__":
    # Validate argument count and check if it's a valid integer
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_response = requests.get(f"{base_url}/users/{user_id}")
    if user_response.status_code != 200:
        print("Error: User not found")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("name")

    # Fetch tasks for the user
    todos_response = \
        requests.get(f"{base_url}/todos", params={"userId": user_id})
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task["title"] for task in todos if task["completed"]]

    # Ensure the first line matches the exact format required
    first_line = "Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos)
    )
    print(first_line)

    # Print each completed task title with a tab and space
    for task in completed_tasks:
        print("\t {}".format(task))  # Tab (`\t`) followed by a space

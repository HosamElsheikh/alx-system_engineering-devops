#!/usr/bin/python3
"""
Fetches and displays employee TODO list progress using REST API
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    if not user:
        print(f"Employee with ID {employee_id} not found.")
        return

    # Fetch employee tasks
    todos = requests.get(f"{base_url}/todos", params={"userId": employee_id}).json()

    # Filter completed tasks
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]

    # Display output
    employee_name = user.get("name")
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

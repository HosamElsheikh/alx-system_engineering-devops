#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID """
import json
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    uid = sys.argv[1]

    users_url = 'https://jsonplaceholder.typicode.com/users/' + uid
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'

    try:
        with urllib.request.urlopen(users_url) as res:
            data = res.read().decode('utf-8')
            user = json.loads(data)

        with urllib.request.urlopen(todo_url) as res:
            data = json.loads(res.read().decode('utf-8'))
            todos = []
            done_tasks = 0
            completed_tasks = []
            for todo in data:
                if todo['userId'] == int(uid):
                    todos.append(todo)
                    if todo['completed'] is True:
                        done_tasks += 1
                        completed_tasks.append(todo['title'])

            name = user['name']
            total_tasks = len(todos)
            print(
                "Employee {} is done with tasks({}/{}):".format(
                    name,
                    done_tasks,
                    total_tasks
                )
            )
            for task in completed_tasks:
                print('\t ' + task)

    except urllib.error.URLError as e:
        print(f"Error fetching the URL: {e.reason}")
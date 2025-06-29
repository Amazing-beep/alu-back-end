#!/usr/bin/python3
"""Fetches employee TODO list progress from a REST API and displays it."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch employee data
    user_url = ("https://jsonplaceholder.typicode.com/users/" +
                f"{employee_id}")
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list data
    todos_url = ("https://jsonplaceholder.typicode.com/todos?userId=" +
                 f"{employee_id}")
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [
        task for task in todos_data if task.get("completed")
    ]
    number_of_done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks("
          f"{number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print("\t " + task.get("title"))


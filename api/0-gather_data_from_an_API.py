#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])  # Get ID from command line argument

    # Get user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get user's todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter completed tasks
    done_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    done_count = len(done_tasks)

    # Print output
    print(f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

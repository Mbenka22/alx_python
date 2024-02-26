import requests
import sys

def get_employee_todo_progress(employee_id):
    employee_response = requests.get("https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    todo_response = requests.get("https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    done_tasks = sum(1 for todo in todo_data if todo['completed'])

    print(f" {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
    for todo in todo_data:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: EMPLOYEE_ID")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

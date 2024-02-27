import requests
import sys
import json

def employee_info(employee_id):
    # Getting employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    # Getting employee's todos
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter completed tasks
    completed_tasks = [{'task': task['title'], 'completed': task['completed'], 'username': employee_data['username']} for task in todos_data]

    # Creating the dictionary for JSON output
    output_data = {str(employee_id): completed_tasks}

    # Writing to JSON file
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(output_data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id.")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_info(employee_id)

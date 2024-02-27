import requests
import sys
import json

def employee_info(employee_id):
    """Getting employee details from the given URL by appending the employee_id to the given URL."""
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    """Getting employee's todos by appending the todo path to the URL."""
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    """Filtering completed tasks."""
    completed_tasks = [{'task': task['title'], 'completed': task['completed'], 'username': employee_data['username']} for task in todos_data]

    """Creating the dictionary for JSON output."""
    output_data = {str(employee_id): completed_tasks}

    """Writing to JSON file."""
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(output_data, json_file, indent=4)

    """Displaying the employee's name and the number of done and total tasks."""
    print(f"Employee {employee_data['name']} is done with tasks({len(completed_tasks)}/{len(todos_data)}):")
    
    """Displaying done tasks."""
    for task in completed_tasks:
        print(f"\t{task['task']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id.")
        sys.exit(1)

    """Employee ID from the second argument."""
    employee_id = int(sys.argv[1])

    """Calling the function."""
    employee_info(employee_id)

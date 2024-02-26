import requests
import sys

def get_employee_info(employee_id):
    """employee details from the given url by appending the employee_id """
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    """getting employee's todo by appending the todo path the url"""
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

 
    completed_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    """Display the employee's name and the number of done and total tasks."""
    print(f"Employee {employee_data['name']} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")

    """Display the title of the completed tasks."""
    for task in completed_tasks:
        print(f"\t{task['title']}")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("")
        sys.exit(1)

    """employee id from the second argument"""
    employee_id = int(sys.argv[1])

    """calling the function"""
    get_employee_info(employee_id)
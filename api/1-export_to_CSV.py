import csv
import requests
import sys

def fetch_employee_details(employee_id):
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    if employee_response.status_code !=200:
        print(f'Failed to  fetch  employee details for ID:{employee_id}')
        return None 
    return employee_response.json()

def fetch_employee_todos(employee_id):
        todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
        todos_response = requests.get(todos_url)
        if todos_response.status_code!=200:
            print(f"Failed to fetch  todo for employee  ID:{employee_id}")
            return None
        return todos_response.json()

    
def  generate_csv(employee_id, employee_data, todos_data):
    if not todos_data:
        print(f"No tasks found emolpyee ID:{employee_id}")
        return 
    file_name = f"{employee_data['username']}tasks.csv"
    with open(file_name, mode="w", newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE' ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        """Write the csv headers"""
        writer.writeheader()

        """Write the rows under the epecified columns"""
        for task in todos_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_data['username'],
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })
            print (f" CSV file'{file_name}' created successfully.")
            
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id.")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    employee_data = fetch_employee_details(employee_id)
    if not employee_data:
        sys.exit(1)

    todos_data=fetch_employee_todos(employee_id)
    if not todos_data:
        sys.exit(1)

    generate_csv(employee_id, employee_data,todos_data)    

   
    

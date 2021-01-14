EMPLOYEES = [
    {
      "name": "Jeremy Williams",
      "locationId": 1,
      "animalId": 1,
      "id": 2
    },
    {
      "name": "Jimmy Wilson",
      "locationId": 2,
      "animalId": 3,
      "id": 3
    }
]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    # Get the id value of the last EMPLOYEE in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee


def delete_employee(id): 

    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break

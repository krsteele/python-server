CUSTOMERS = [
    {
      "email": "peter@petersco.com",
      "password": "password",
      "name": "Peter Peters",
      "id": 1
    },
    {
      "email": "scotty@scottco.com",
      "password": "password",
      "name": "Scotty Scott",
      "id": 2
    },
    {
      "email": "millie@millsmill.com",
      "password": "password",
      "name": "Millie Mills",
      "id": 3
    },
    {
      "email": "frankthetank@brewworks.com",
      "password": "boop",
      "name": "Frank Lipsitz",
      "id": 4
    }
]


def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    
    return requested_customer


def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
      if customer["id"] == id:
        customer_index = index

    if customer_index >= 0:
      CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
      if customer["id"] == id:
        # Found the customer. Update the value.
        CUSTOMERS[index] = new_customer
        break
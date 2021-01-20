import sqlite3
import json
from models import Customer

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


# def get_all_customers():
#     return CUSTOMERS

def get_all_customers():
  #Open a connection to the database
  with sqlite3.connect("./kennel.db") as conn:

    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    # Write the SQL query to get the information you want
    db_cursor.execute("""
    SELECT
      c.id,
      c.email,
      c.password,
      c.name
    FROM customer c
    """)

    # Initialize an empty list to hold all customer representations
    customers = []

    # Convert rows of data into a Python list
    dataset = db_cursor.fetchall()

    # Iterate list of data returned from database
    for row in dataset:

      # Create a customer instance from the current row.
      # Note that the database fields are specified in
      # exact order of the parameters defined in the 
      # Customer class above.
      customer = Customer(row['id'], row['email'], row['password'], row['name'])

      customers.append(customer.__dict__)

  # Use `json` package to properly serialize list as JSON
  return json.dumps(customers)


def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      # Use a ? parameter to inject a variable's value into the SQL statement.
      db_cursor.execute("""
      SELECT
        c.id,
        c.email,
        c.password,
        c.name 
      FROM customer c
      WHERE c.id = ?
      """, (id, ))

      # Load the single result into memory
      data = db_cursor.fetchone()

      # Create a customer instance from the current row
      customer = Customer(data['id'], data['email'], data['password'], data['name'])

      return json.dumps(customer.__dict__)


def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)


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
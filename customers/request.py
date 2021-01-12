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
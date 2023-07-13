# Sample Data
__customers = [
    {
        "id":1,
        "name":"Earth Co"
    },
    {
        "id":2,
        "name":"Water Ltd"
    },
    {
        "id":3,
        "name":"Fire Plc"
    }
]

def create_customer(customer_name:str) -> int:
    global __customers

    customer_id = max([x['id'] for x in __customers] + 1)
    __customers.append({
        "id":customer_id,
        "name": customer_name
    })

    return customer_id

def get_customers() -> list:
    return __customers.copy()


def get_customer(customer_id:int) ->dict:
    customer = [x for x in __customers if x['id'] == int(customer_id)]
    return customer.copy()


def update_customer(customer_id:int, custoemr_data:dict):
    pass


def delete_customer(customer_id:int):
    pass
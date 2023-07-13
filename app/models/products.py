# Sample Data
__products = [
    {
        "id":1,
        "name":"Paper A4"
    },
    {
        "id":2,
        "name":"Pens x 10"
    },
    {
        "id":3,
        "name":"Pencils x 20"
    }
]

def create_product(product_name:str) -> int:
    global __products

    product_id = max([x['id'] for x in __products] + 1)
    __products.append({
        "id":product_id,
        "name": product_name
    })

    return product_id

def get_products() -> list:
    return __products.copy()


def get_product(product_id:int) ->dict:
    product = [x for x in __products if x['id'] == int(product_id)]
    return product.copy()


def update_product(product_id:int, custoemr_data:dict):
    pass


def delete_product(product_id:int):
    pass
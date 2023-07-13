from models import customers, products

def get_dashboard_data() -> dict:
    data = {
        "customers":customers.get_customers(),
        "products":products.get_products()
    }

    return data
from step_1 import transform_products_to_list


def group_products_by_customer(products_string):
    products = transform_products_to_list(products_string)
    prod_by_customer = {}
    for product in products:
        customer_id = product[-2]
        prod_by_customer.setdefault(customer_id, [])
        prod_by_customer[customer_id].append(product)
    return prod_by_customer
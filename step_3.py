from step_1 import transform_products_to_list


def group_products_by_customer_and_invoice(products_string):
    products = transform_products_to_list(products_string)
    prod_grouped = {}
    for product in products:
        customer_id = product[-2]
        invoice_id = product[0]
        prod_grouped.setdefault(customer_id, {})
        prod_grouped[customer_id].setdefault(invoice_id, [])
        prod_grouped[customer_id][invoice_id].append(product)
    return prod_grouped

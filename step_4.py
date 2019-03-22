from step_1 import transform_products_to_list


def calculate_total_per_invoices(products_string):
    products = transform_products_to_list(products_string)
    invoice_totals = {}
    for product in products:
        customer_id = product[-2]
        invoice_id = product[0]
        quantity = int(product[3])
        price = float(product[-3])
        total = round(quantity * price, 3)
        invoice_totals.setdefault(customer_id, {})
        invoice_totals[customer_id].setdefault(invoice_id, 0)
        invoice_totals[customer_id][invoice_id] += total
    return invoice_totals

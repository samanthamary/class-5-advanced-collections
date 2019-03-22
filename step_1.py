def transform_products_to_list(products_string):
    products = products_string.split("\n")
    list_of_products = []
    for product in products:
        if product:
            list_of_products.append(product.split(","))
    return list_of_products


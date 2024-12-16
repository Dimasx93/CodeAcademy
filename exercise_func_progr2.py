from functools import reduce

purchases = [{"customer_id": 1, "products": [{"name": "Laptop", "price": 1200.99, "quantity": 1},
                                             {"name": "Mouse", "price": 25.50, "quantity": 2}], "date": "2024-12-01"},

             {"customer_id": 2, "products": [{"name": "Monitor", "price": 300.00, "quantity": 1},
                                             {"name": "Keyboard", "price": 75.99, "quantity": 1}],
              "date": "2024-12-02"},

             {"customer_id": 3, "products": [{"name": "Tablet", "price": 400.99, "quantity": 2},
                                             {"name": "Mouse", "price": 25.50, "quantity": 1}], "date": "2024-12-01"}
             ]

# Tasks:Total Revenue per Purchase: Use map() to calculate the total revenue
# for each purchase(sum of price * quantity for all products in the purchase).
#
# Filter High - Spending Purchases: Use filter() to find all purchases where the total revenue exceeds $500.
#
# Sort Purchases by Revenue: Use sorted() to sort the purchases in descending order of total revenue.
#
# Top Product by Revenue: Use reduce() to determine the single product(across all purchases) that generated
# the highest total revenue(price * quantity).
#
# Bonus Task - Revenue by Customer:
# Combine map() and reduce() to calculate the total revenue per customer(customer_id).

tot_revenue_purchase = list(
    map(lambda purchase: sum([product["price"] * product["quantity"] for product in purchase["products"]]), purchases))
print(tot_revenue_purchase)

filter_high = list(filter(lambda cost: cost > 500, tot_revenue_purchase))
print(filter_high)

sorted_purchase = sorted(tot_revenue_purchase, reverse=True)
print(sorted_purchase)


def compare_products(top, purchase):
    # Calculate the revenue for each product in the current purchase
    product_revenues = [(product["name"], product["price"] * product["quantity"]) for product in purchase["products"]]

    # Find the product with the highest revenue in the current purchase
    max_product = max(product_revenues, key=lambda x: x[1])

    # Compare the current max product with the accumulated top product and return the one with the higher revenue
    if max_product[1] > top[1]:
        return max_product
    else:
        return top

# Using reduce to find the product with the highest total revenue
top_product = reduce(compare_products, purchases, ("", 0))

print(top_product)

# Step 1: Use map() to create a list of (customer_id, revenue) for each purchase
revenue_per_purchase = list(map(lambda purchase: (purchase["customer_id"],
                                                  sum([product["price"] * product["quantity"] for product in
                                                       purchase["products"]])),
                                purchases))


# Step 2: Use reduce() to accumulate the total revenue for each customer
def accumulate_revenue(accumulated, current):
    customer_id = current[0]
    revenue = current[1]

    # Check if the customer already has an accumulated revenue in the result
    if customer_id in accumulated:
        accumulated[customer_id] += revenue
    else:
        accumulated[customer_id] = revenue

    return accumulated


# Reduce the list to total revenue by customer_id
total_revenue_by_customer = reduce(accumulate_revenue, revenue_per_purchase, {})

# Print the result
print(total_revenue_by_customer)
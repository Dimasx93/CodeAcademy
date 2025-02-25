# Lesson SQLAlchemy ORM                                    Date 24/02/2025

# Exercise n2 E-Shop: User Interface

from sqlalchemy.orm import sessionmaker

from sql_alchemy_exercise_2 import (
    Base,
    Customer,
    Order,
    OrderProductAssociation,
    Product,
    Status,
    engine,
)


def show_options(model_class):
    options = session.query(model_class).all()
    for entry in options:
        print(entry)


def show_order_info(order):
    print(
        f"\nOrder #{order.id} customer – {order.customer.f_name} "
        f"{order.customer.l_name}:"
    )
    print("\nProduct\tQty\tPrice\tSum")

    order_product_associations = order.products
    total = 0.0
    for op_assoc in order_product_associations:
        print(
            f"{op_assoc.product.name}\t"
            f"{op_assoc.quantity}\t"
            f"{op_assoc.product.price:.2f}\t"
            f"{op_assoc.quantity * op_assoc.product.price:.2f}"
        )
        total += op_assoc.product.price * op_assoc.quantity
    print(f"\n\t\tTotal:\t{total:.2f}")
    print(f"\t\tStatus:\t{order.status.name}")


def create_customer():
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    email = input("Email: ")
    customer = Customer(f_name=f_name, l_name=l_name, email=email)
    session.add(customer)
    session.commit()
    print("Customer created!\n")


def create_status():
    print("Existing statuses:")
    show_options(Status)
    name = input("\nNew status name: ")
    status = Status(name=name)
    session.add(status)
    session.commit()
    print("Status created!\n")


def create_product():
    print("Existing products:")
    show_options(Product)
    name = input("\nName: ")
    price = float(input("Price: "))
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()
    print("Product created!\n")


def create_order():
    at_least_one_customer = session.query(Customer).first()
    if not at_least_one_customer:
        print("There are no customers yet!")
        return

    at_least_one_status = session.query(Status).first()
    if not at_least_one_status:
        print(
            "There are no statuses yet! You need to create at least one status first.")
        return

    print("List of customers:")
    show_options(Customer)
    customer_id = int(input("\nCustomer ID: "))
    customer = session.get(Customer, customer_id)

    print("List of statuses:")
    show_options(Status)
    status_id = int(input("\nStatus ID: "))
    status = session.get(Status, status_id)

    order = Order(customer=customer, status=status)
    session.add(order)
    session.commit()
    print("Products available:")
    show_options(Product)
    while True:
        product_id = int(input("\nProduct ID: "))
        quantity = int(input("Quantity: "))
        product = session.get(Product, product_id)
        if product is not None:
            order.products.append(
                OrderProductAssociation(product=product, quantity=quantity)
            )
            session.commit()
            choice = input("Would you like to add more products to this order? (y/n): ")
            if choice.lower() == "y":
                continue
            else:
                print("Order created!\n")
                break
        else:
            print("No such product, try again!")


def view_order():
    orders = session.query(Order).all()
    if not orders:
        print("There are no orders yet!")
        return

    first_order_id = orders[0].id
    last_order_id = orders[-1].id
    id_ = int(input(f"Order ID ({first_order_id}–{last_order_id}): "))
    order = session.get(Order, id_)
    show_order_info(order)


def change_status():
    orders = session.query(Order).all()
    if not orders:
        print("There are no orders yet!")
        return

    first_order_id = orders[0].id
    last_order_id = orders[-1].id
    id_ = int(input(f"Order ID ({first_order_id}–{last_order_id}): "))
    order = session.get(Order, id_)
    print(f"Current status of this order: {order.status}")
    print("Existing statuses:")
    show_options(Status)
    status_id = int(input("\nSet status ID: "))
    status = session.get(Status, status_id)
    order.status = status
    session.commit()
    print("Status changed!\n")


def view_customer_orders():
    orders = session.query(Order).all()
    if not orders:
        print("There are no orders yet!")
        return

    print("List of customers:")
    show_options(Customer)
    customer_id = int(input("\nCustomer ID: "))
    customer = session.get(Customer, customer_id)
    customer_orders = customer.orders

    if not customer_orders:
        print("This customer has no orders yet!")
        return

    for order in customer_orders:
        show_order_info(order)
        print("-" * 50)


def main():
    while True:
        print(
            "\n"
            "Options:\n"
            "c – Add Customer\n"
            "p – Add Product\n"
            "s – Add Status\n"
            "o – Add Order\n"
            "v – View Order\n"
            "cs – Change Status\n"
            "vc – View Customer Orders\n"
            "q – Quit"
        )

        choice = input("Enter your choice: ")

        match choice.lower():
            case "c":
                create_customer()
            case "p":
                create_product()
            case "s":
                create_status()
            case "o":
                create_order()
            case "v":
                view_order()
            case "cs":
                change_status()
            case "vc":
                view_customer_orders()
            case "q":
                print("See you!")
                break
            case _:
                print("Incorrect input, try again!")


if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    # ^--- uncomment if you want to drop all tables at the start of the program
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    main()

    session.close()
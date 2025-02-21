#Lesson SQL Introduction, SQLite             date: 18/02/2025

#Exercise Create a DATABASE

# import sqlite3
#
# conn = sqlite3.connect("order_database.sqlite")
# c = conn.cursor()
#
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# table_names = c.fetchall()
# for table_name in table_names:
#     table_name = table_name[0]
#     print(f"\nColumns in {table_name} table:")
#     data = c.execute(f"SELECT * FROM {table_name}")
#     for column in data.description:
#         print(column[0])

# query = """CREATE TABLE order_(
#     id INTEGER PRIMARY KEY,
#     customer_id INTEGER,
#     date_ DATE,
#     status_id INTEGER,
#     FOREIGN KEY(status_id) REFERENCES status(id),
#     FOREIGN KEY(customer_id) REFERENCES customer(id)
# )"""

# query = """CREATE TABLE product(
#     id INTEGER PRIMARY KEY,
#     name STRING,
#     price REAL
# )"""

# query = """CREATE TABLE customer(
#     id INTEGER PRIMARY KEY,
#     f_name STRING,
#     l_name STRING,
#     email STRING UNIQUE
# )"""

# query = """CREATE TABLE status(
#     id INTEGER PRIMARY KEY,
#     name STRING
# )"""

# query = """CREATE TABLE product_order(
#     order_id INTEGER PRIMARY KEY,
#     product_id INTEGER,
#     quantity INTEGER,
#     FOREIGN KEY(product_id) REFERENCES product(id),
#     FOREIGN KEY(order_id) REFERENCES order_(id)
# )"""

# query="""DROP TABLE product_order;"""

# query="""INSERT INTO customer (id,f_name,l_name,email)
# VALUES('1','John','Doe','john.doe@gmail.lt'),('2','Vivy','Cai','vivy.cai@gmail.lt'),('3','Pino','Lino','pino.lino@gmail.lt');"""

# query="""INSERT INTO product (id,name,price)
# VALUES('1','Pizza','10'),('2','Salad','7'),('3','Cola','3'),
# ('4','Beer','5'),('5','Wine','6'),('6','Water','2');"""

# query="""INSERT INTO order_(id,customer_id,date_,status_id)
# VALUES('10','1','2020-10-10','0'),('11','2','2022-04-06','1'),('12','3','2021-03-10','2'),
# ('13','1','2023-08-20','3'),('14','2','2018-11-11','0');"""

# query="""INSERT INTO status(id,name)
# VALUES('0','Approved'),('1','Incoming'),('2','Finish'),
# ('3','Paid');"""

# query="""INSERT INTO product_order(order_id, product_id, quantity)
# VALUES('10','1','2'),('11','5','4'),('12','2','5'),('13','3','2'),('14','1','7')"""

# query="""SELECT order_.id,order_.date_,customer.l_name, product_order.quantity
# FROM  order_ JOIN customer ON order_.customer_id = customer.id JOIN product_order ON order_.id = product_order.order_id
# """

# query="""SELECT order_.id, product.name, product_order.quantity, product.price,
# product_order.quantity * product.price AS total_product_price
# FROM order_ JOIN product_order ON order_.id = product_order.order_id JOIN product ON product_order.product_id = product.id"""

# query="""SELECT product.name, product_order.quantity, product.price,product_order.quantity * product.price AS total_product_price
# FROM order_ JOIN product_order ON order_.id = product_order.order_id JOIN product ON product_order.product_id = product.id """
#
# with conn:
#     c.execute(query)
#     print(c.fetchall())

##########################################################################################################################

#Exercise Car Database

# import sqlite3
#
#
# conn = sqlite3.connect("car_database.sqlite")
# c = conn.cursor()
#
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# table_names = c.fetchall()
# for table_name in table_names:
#     table_name = table_name[0]
#     print(f"\nColumns in {table_name} table:")
#     data = c.execute(f"SELECT * FROM {table_name}")
#     for column in data.description:
#         print(column[0])

# query= """CREATE TABLE cars(
#     make STRING,
#     model STRING,
#     color STRING,
#     year INTEGER,
#     price REAL
# )"""

# query="""DROP TABLE cars;"""

# query="""INSERT INTO cars VALUES
# ('GMC', 'Yukon', 'Crimson', 2001, 76128),('Porsche', 'Cayman', 'Turquoise', 2008, 44927),('Pontiac', 'Sunbird', 'Yellow', 1993, 48916),
# ('Daewoo', 'Leganza', 'Yellow', 1999, 91700),('Acura', 'TL', 'Puce', 2007, 43816),('Ford', 'Ranger', 'Purple', 1990, 62492),
# ('Nissan', 'Altima', 'Goldenrod', 2007, 42633),('Volkswagen', 'Golf', 'Turquoise', 2004, 44043),('Chevrolet', 'Express 3500', 'Blue', 1997, 9787),
# ('Plymouth', 'Grand Voyager', 'Blue', 1997, 54185),('Cadillac', 'DeVille', 'Purple', 2002, 96452),('Ford', 'Bronco', 'Crimson', 1991, 7794),
# ('Lexus', 'LS Hybrid', 'Aquamarine', 2012, 38252),('Volkswagen', 'Passat', 'Turquoise', 2009, 70328),('Mercedes-Benz', 'SL-Class', 'Green', 1987, 34447),
# ('Honda', 'Odyssey', 'Maroon', 2005, 91950),('Saturn', 'Sky', 'Maroon', 2008, 65801),('Toyota', 'Camry', 'Turquoise', 1998, 86343),
# ('Infiniti', 'G', 'Blue', 1993, 74130),('Ford', 'Focus', 'Puce', 2001, 95580),('Ford', 'LTD', 'Goldenrod', 1986, 31708),
# ('Mercedes-Benz', '300D', 'Purple', 1993, 46190),('Cadillac', 'CTS', 'Blue', 2012, 53484),('Honda', 'Odyssey', 'Red', 2009, 7188),
# ('Mercury', 'Mountaineer', 'Blue', 2000, 95484),('Ford', 'Thunderbird', 'Blue', 1992, 85039),('Audi', 'Coupe Quattro', 'Mauv', 1990, 17963),
# ('Ford', 'Econoline E150', 'Mauv', 1999, 77616),('Volvo', '960', 'Purple', 1993, 10070),('Chevrolet', 'Aveo', 'Purple', 2008, 11091),
# ('Acura', 'MDX', 'Maroon', 2012, 37686),('Volkswagen', 'Eos', 'Teal', 2007, 50258),('Hyundai', 'Santa Fe', 'Teal', 2011, 14134),
# ('Jeep', 'Cherokee', 'Mauv', 2000, 26833),('Pontiac', 'LeMans', 'Maroon', 1988, 91500),('Lexus', 'GX', 'Goldenrod', 2003, 4875),
# ('Toyota', 'Xtra', 'Khaki', 1995, 39651),('Mercedes-Benz', 'S-Class', 'Indigo', 1989, 42265),('Mercedes-Benz', 'SL-Class', 'Purple', 1995, 61515),
# ('Ford', 'E-Series', 'Goldenrod', 2008, 74241),('Land Rover', 'Discovery', 'Turquoise', 2003, 51970),('Chevrolet', '2500', 'Green', 1996, 62612),
# ('Mercedes-Benz', 'G-Class', 'Aquamarine', 2003, 30440),('Subaru', 'Tribeca', 'Violet', 2011, 47934),('Hyundai', 'Elantra', 'Teal', 2010, 48035),
# ('Kia', 'Sportage', 'Purple', 1998, 90643),('Chevrolet', 'Prizm', 'Orange', 2001, 23214),('Ford', 'F150', 'Maroon', 2004, 74789),
# ('Mitsubishi', 'Eclipse', 'Red', 1999, 41128),('Oldsmobile', 'Intrigue', 'Pink', 2001, 72735),('Toyota', 'T100', 'Puce', 1994, 48047),
# ('Saturn', 'Sky', 'Yellow', 2008, 2604),('GMC', 'Savana 3500', 'Blue', 2009, 47189),('Ford', 'Edge', 'Crimson', 2010, 39075),
# ('Ford', 'F-Series Super Duty', 'Green', 2008, 3442),('Nissan', 'Pathfinder', 'Khaki', 2009, 10900),('Mazda', 'Millenia', 'Blue', 2001, 57221),
# ('Acura', 'CL', 'Turquoise', 2003, 33236),('Mitsubishi', 'Galant', 'Red', 1995, 2585),('Saturn', 'Ion', 'Turquoise', 2003, 36483),
# ('Chevrolet', 'HHR', 'Goldenrod', 2011, 36060),('BMW', 'X3', 'Pink', 2010, 51103),('BMW', '8 Series', 'Pink', 1995, 72125),
# ('Audi', 'A4', 'Crimson', 2012, 61155),('Scion', 'xB', 'Yellow', 2006, 28119),('Mercedes-Benz', 'S-Class', 'Indigo', 2003, 58174),
# ('Acura', 'RL', 'Fuscia', 2010, 77869),('Mercury', 'Villager', 'Violet', 1993, 50637),('Ford', 'Escape', 'Indigo', 2006, 76794),
# ('Porsche', '944', 'Maroon', 1989, 42270),('Toyota', 'Highlander', 'Teal', 2001, 61487),('Subaru', 'Baja', 'Khaki', 2005, 95233),
# ('Buick', 'Roadmaster', 'Orange', 1995, 39853),('Austin', 'Mini', 'Fuscia', 1959, 46870),('Aston Martin', 'V8 Vantage', 'Blue', 2008, 54431);"""

# with conn:
#     c.execute(query)
#     print(c.fetchall())

##########################################################################################################################

#Exercise Car Database with Python

import sqlite3

# Connect to the SQLite database (create the DB if it doesn't exist)
conn = sqlite3.connect("car_database.sqlite")
cursor = conn.cursor()


# Function to insert a new car into the database
def insert_car(make, model, color, year, price):
    cursor.execute("INSERT INTO cars (make, model, color, year, price) VALUES (?, ?, ?, ?, ?)",
                   (make, model, color, year, price))
    conn.commit()
    print("Car added successfully!")


# Function to search cars in the database
def search_cars(make=None, model=None, color=None, year_range=None, price_range=None):
    query = "SELECT * FROM cars WHERE 1=1"
    params = []

    # Add filtering based on user input
    if make:
        query += " AND make = ?"
        params.append(make)
    if model:
        query += " AND model = ?"
        params.append(model)
    if color:
        query += " AND color = ?"
        params.append(color)
    if year_range:
        query += " AND year BETWEEN ? AND ?"
        params.extend(year_range)
    if price_range:
        query += " AND price BETWEEN ? AND ?"
        params.extend(price_range)

    cursor.execute(query, params)
    results = cursor.fetchall()

    # Display the search results
    if results:
        for row in results:
            print(f"Make: {row[0]}, Model: {row[1]}, Color: {row[2]}, Year: {row[3]}, Price: {row[4]}")
    else:
        print("No matching cars found.")


# Function to take user input for a new car
def add_new_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    color = input("Enter car color: ")
    year = int(input("Enter car year: "))
    price = int(input("Enter car price: "))
    insert_car(make, model, color, year, price)


# Function to handle search filters
def search_for_car():
    print("Enter search criteria. Press Enter to skip a parameter.")

    make = input("Enter car make (or leave blank): ")
    model = input("Enter car model (or leave blank): ")
    color = input("Enter car color (or leave blank): ")

    # Year range input
    year_from = input("Enter start year (or leave blank): ")
    year_to = input("Enter end year (or leave blank): ")
    year_range = None
    if year_from and year_to:
        year_range = (int(year_from), int(year_to))

    # Price range input
    price_from = input("Enter minimum price (or leave blank): ")
    price_to = input("Enter maximum price (or leave blank): ")
    price_range = None
    if price_from and price_to:
        price_range = (int(price_from), int(price_to))

    # Call the search function with the filters
    search_cars(make=make if make else None,
                model=model if model else None,
                color=color if color else None,
                year_range=year_range,
                price_range=price_range)


# Main function to run the program
def main():
    while True:
        print("\n--- Car Database ---")
        print("1. Add new car")
        print("2. Search cars")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_new_car()
        elif choice == "2":
            search_for_car()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")


# Run the main program
if __name__ == "__main__":
    main()

    # Close the database connection when the program ends
    conn.close()
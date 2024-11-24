# Lesson n13 Logging
#
#Exercise n1 User input
#Create a simple program that continuously asks the user for input and logs all their inputs to a file.
#Along with the input, the date and time of the input as well as the logging level should be recorded.
#
# import logging
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="data.log",
#     filemode="a",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )
#
# while True:
#     user_input = input("Log something, write done to exit: ")
#     if user_input.lower() == "done":
#         print("Goodbye!")
#         break
#     logging.info(user_input)
#
#Exercise n2 Mathematical Functions
# import logging
# import math
# logging.basicConfig(
#     filename="functions_log.txt",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )
#
# def math_sum(*args):
#     total_sum = sum(args)
#     logging.info(f"The sum of numbers {args} is: {total_sum}")
#     return total_sum
# print(math_sum(1,2))
#
# def square_r(a):
#     try:
#         result = math.sqrt(a)
#         logging.info(f"The square root of {a} is {result}.")
#         return result
#     except TypeError:
#         logging.exception(f"The input {a} is not a number.")
#         return f"The input {a} is not a number."
# print(square_r("HI"))
#
# def length_str(a:str):
#     try:
#         result = len(a)
#         logging.info(f"The length of {a} is {result}.")
#         return result
#     except TypeError:
#         logging.exception(f"The input {a} is not a string.")
#         return f"The input {a} is not a string."
# print(length_str("5 hello"))
#
# def div_num(a,b):
#     try:
#         result = a / b
#         logging.info(f"The division between {a} and {b} is {result}.")
#         return result
#     except TypeError:
#         logging.exception(f"Both, {a} and {b} must be numbers.")
#         return f"Both, {a} and {b} must be numbers."
#     except ZeroDivisionError:
#         logging.exception(f"Cannot divide a number with {b}")
#         return f"Cannot divide {a} with {b}"
# print(div_num(5, 0))
#
#Exercise n3 Start a Car
import logging

logging.basicConfig(
    filename="car_start_log.txt",
    # Set to DEBUG to capture all logging levels:
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def check_engine() -> bool:
    """Simulates engine check."""
    logging.debug("Engine check started.")

    # Simulate engine check
    engine_ok = True  # You can change this to False

    if engine_ok:
        logging.info("The engine is in good condition.")
        print("The engine is in good condition.")
    else:
        logging.warning("The engine may need maintenance.")
        print("The engine may need maintenance.")

    logging.debug(
        "Engine check finished. Engine status: %s",
        "Good" if engine_ok else "Problems",
    )
    return engine_ok


def check_fuel() -> bool:
    """Simulates fuel level check, using liters."""
    logging.debug("Fuel check started.")

    # Example fuel parameters
    fuel_level = 5  # Current fuel level in liters (simulated)
    max_fuel_capacity = 50  # Example maximum fuel capacity in liters

    # Calculate fuel percentage
    fuel_percentage = (fuel_level / max_fuel_capacity) * 100

    logging.debug(
        "Current fuel level: %.1f%% (%.1f out of %d liters)",
        fuel_percentage,
        fuel_level,
        max_fuel_capacity,
    )

    if fuel_percentage > 15:
        logging.info("Fuel level is sufficient.")
        print("Fuel level is sufficient.")
        return True
    elif fuel_percentage > 5:
        logging.warning("Fuel level is low. Consider refueling soon.")
        print("Fuel level is low. Consider refueling soon.")
        return True
    else:
        logging.error("Critical fuel level! The car may not start.")
        print("Critical fuel level! Refill the fuel.")
        return False


def check_oil() -> bool:
    """Simulates oil level check."""
    logging.debug("Oil check started.")

    # Example oil level parameters
    min_oil_level = 2.0  # Minimum allowed oil level
    max_oil_level = 4.5  # Maximum allowed oil level
    current_oil_level = 3.2  # Current oil level in liters (simulated)

    logging.debug(
        "Current oil level: %.1f liters, MIN: %.1f liters, MAX: %.1f liters",
        current_oil_level,
        min_oil_level,
        max_oil_level,
    )

    if min_oil_level <= current_oil_level <= max_oil_level:
        logging.info("Oil level is sufficient.")
        print("Oil level is sufficient.")
        return True
    elif current_oil_level < min_oil_level:
        logging.warning("Oil level is too low! Refill oil.")
        print("Oil level is low. Consider refilling.")
        return False
    else:
        logging.error("Oil level is too high! This may cause problems.")
        print("Oil level is too high. Consider draining some oil.")
        return False


def start_car() -> None:
    """Simulates starting the car after performing all checks."""
    logging.info("Car start initiated.")
    try:
        engine_status = check_engine()
        fuel_status = check_fuel()
        oil_status = check_oil()

        if engine_status and fuel_status and oil_status:
            # If all checks are successful, the car starts
            logging.info("The car has been successfully started.")
            print("The car has been successfully started. Have a good trip!")
        else:
            logging.critical("Failed to start the car. Check all components.")
            print("Failed to start the car. Contact a mechanic.")
    except Exception as e:
        logging.critical(f"Critical error while starting the car: {e}")
        print(f"Critical error: {e}")

    logging.info("Car start process completed.")


if __name__ == "__main__":
    start_car()
# Lesson SQLAlchemy ORM                                    Date 24/02/2025

# Exercise n4 E-Banking

from sqlalchemy.orm import sessionmaker

from sql_alchemy_exercises_4.sql_alchemy_exercise_4 import (Person, Bank, Account, engine)


def pretty_print(header, contents=None):
    print("-" * 50)
    print(header)

    if contents is not None:
        print("-" * 25)
        for entry in contents:
            print(entry)

    print("-" * 50)


def main():
    while True:
        print(
            "\n"
            "Options:\n"
            "1 - Add User\n"
            "2 - Add Bank\n"
            "3 - Create Account\n"
            "4 - Add income/expense\n"
            "5 - View Person's Accounts\n"
            "6 - View Users\n"
            "7 - View Banks\n"
            "8 - View all Accounts\n"
            "9 - Quit"
        )

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                name = input("Enter name: ")
                surname = input("Enter surname: ")
                social_security_no = int(input("Enter social security number: "))
                phone_no = input("Enter phone number: ")

                person = Person(
                    name=name,
                    surname=surname,
                    social_security_no=social_security_no,
                    phone_no=phone_no,
                )

                session.add(person)
                session.commit()
                pretty_print("User successfully added!")
            case 2:
                name = input("Enter bank name: ")
                address = input("Enter address: ")
                swift_code = input("Enter SWIFT (BIC) code: ")

                bank = Bank(
                    name=name,
                    address=address,
                    swift_code=swift_code,
                )

                session.add(bank)
                session.commit()
                pretty_print("Bank successfully added!")
            case 3:
                persons = session.query(Person).all()
                pretty_print("Available users:", persons)
                person_id = int(input("Select user ID: "))
                selected_person = session.get(Person, person_id)

                banks = session.query(Bank).all()
                pretty_print("Available banks:", banks)
                bank_id = int(input("Select bank ID: "))
                selected_bank = session.get(Bank, bank_id)

                iban_no = int(input("Enter account number (IBAN): "))
                balance = 0

                account = Account(
                    iban_no=iban_no,
                    balance=balance,
                    person=selected_person,
                    bank=selected_bank,
                )

                session.add(account)
                session.commit()
                pretty_print("Account successfully created!")
            case 4:
                accounts = session.query(Account).all()
                pretty_print("Available accounts:", accounts)
                account_id = int(input("Select account ID: "))
                selected_account = session.get(Account, account_id)

                record = float(
                    input("Enter income/expense (use '-' sign for expense): ")
                )
                selected_account.balance += record
                session.commit()

                if record > 0:
                    pretty_print("Income successfully added!")
                else:
                    pretty_print("Expense successfully added!")
            case 5:
                persons = session.query(Person).all()
                pretty_print("Available users:", persons)
                person_id = int(input("Select user ID: "))
                selected_person = session.get(Person, person_id)
                pretty_print(
                    "ID: Balance (€), IBAN Name Surname, Bank name",
                    selected_person.accounts,
                )
            case 6:
                persons = session.query(Person).all()
                pretty_print(
                    "ID: Name Surname, SSN, Phone number",
                    persons,
                )
            case 7:
                banks = session.query(Bank).all()
                pretty_print(
                    "ID: Name, Address, SWIFT (BIC) code",
                    banks,
                )
            case 8:
                accounts = session.query(Account).all()
                pretty_print(
                    "ID: Balance (€), IBAN Name Surname, Bank name",
                    accounts,
                )
            case 9:
                print("Goodbye!")
                break
            case _:
                print("No such option!")


if __name__ == "__main__":

    Session = sessionmaker(bind=engine)
    session = Session()

    main()

    session.close()
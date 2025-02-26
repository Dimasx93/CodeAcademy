# Lesson SQLAlchemy ORM                                    Date 24/02/2025

# Exercise n4 E-Banking

from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, create_engine)
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///e-banking_db.sqlite")
Base = declarative_base()

class Person(Base):
    __tablename__="person"
    id = Column(Integer,primary_key=True)
    f_name = Column("f_name", String)
    l_name = Column("l_name", String)
    social_security_number= Column("social_security_number", String, unique=True)
    phone_number = Column("phone_number", Integer)
    accounts = relationship("Account", back_populates="person")

    def __repr__(self):
        return  f"{self.id}. {self.f_name} {self.l_name}, Social number: {self.social_security_number}, phone number {self.phone_number}."

class Bank(Base):
    __tablename__="bank"
    id = Column(Integer,primary_key=True)
    name = Column("name", String)
    address = Column("address", String)
    swift_code = Column("swift_code", String, unique=True)
    accounts = relationship("Account", back_populates="bank")

    def __repr__(self):
        return f"{self.id}. {self.name}, {self.address}, Swift code: {self.swift_code}."

class Account(Base):
    __tablename__="account"
    id = Column(Integer,primary_key=True)
    iban_code = Column("iban_code", String, unique=True)
    balance = Column("balance", Float)
    person_id = Column(Integer, ForeignKey("person.id"))
    bank_id = Column( Integer, ForeignKey("bank.id"))

    person = relationship("Person", back_populates="accounts")
    bank = relationship("Bank", back_populates="accounts")

    def __repr__(self):
        return f"{self.id}. {self.iban_code}, {self.balance}, {self.person_id}, {self.bank_id}"


if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    # ^--- uncomment if you want to drop all tables at the start of the program
    Base.metadata.create_all(engine)
    
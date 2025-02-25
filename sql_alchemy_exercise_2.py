# Lesson SQLAlchemy ORM                                    Date 24/02/2025

# Exercise n2 E-Shop: Data Model

from datetime import datetime

from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, create_engine)
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///e-shop_with_assoc_object.sqlite")
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    f_name = Column("f_name", String)
    l_name = Column("l_name", String)
    email = Column("email", String)

    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"{self.id} {self.f_name} {self.l_name}"

class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)

    def __repr__(self):
        return f"<{self.id} {self.name}>"

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    price = Column("price", Float)

    def __repr__(self):
        return f"{self.id} {self.name}"

class Order(Base):
    __tablename__ = "order_"
    id = Column(Integer, primary_key=True)
    date = Column("date_", DateTime, default=datetime.today())
    customer_id = Column(Integer, ForeignKey("customer.id"))
    status_id = Column(Integer, ForeignKey("status.id"))

    customer = relationship("Customer", back_populates="orders")
    status = relationship("Status")
    products = relationship("OrderProductAssociation")

class OrderProductAssociation(Base):
    __tablename__ = "order_product_association"
    __table_args__ = (
        UniqueConstraint("order_id", "product_id", name="order_product_uc"),
    )
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("order_.id"))
    product_id = Column(Integer, ForeignKey("product.id"))

    product = relationship("Product")
    order = relationship("Order", back_populates="products")

    quantity = Column("quantity", Integer)

if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    # ^--- uncomment if you want to drop all tables at the start of the program
    Base.metadata.create_all(engine)
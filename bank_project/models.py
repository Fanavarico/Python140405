from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    email= Column(String, unique=True)
    age = Column(Integer, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)

    #-------timestamps-----
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    #-------relationships-----
    accounts= relationship("Account", back_populates="customer")




#-------Accounts------
class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    balance= Column(Float, default=0.0) #mojodi , 00
    type = Column(String, default="standard") # 'standard', 'foreign', 'crypto'
    pin = Column(String, nullable=False) #pin kodom account ro khod kon
    customer_id= Column(Integer, ForeignKey("customers.id"))
    
    #-------relationships-----
    customer= relationship("Customer", back_populates="accounts")
    transactions= relationship("Transaction", back_populates="account")



#-------Transactions------
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    amount= Column(Float, nullable=False)
    type = Column(String, nullable=False) # 'deposit', 'withdraw', 'transfer'
    timestamp = Column(DateTime, default=datetime.now)
    account_id= Column(Integer, ForeignKey("accounts.id"))
    account= relationship("Account", back_populates="transactions")


'''
 def gui_create_customer(self):
        pass
    def gui_create_account(self):
        pass
    def gui_view_accounts(self):
        pass
    def gui_view_transactions(self):
        pass
    def gui_delete_account(self):
        pass



'''

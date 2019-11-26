# todo this isn't working. Re design.
# import os
# import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Numeric, Date
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from . import configreader

user, host, password, db = configreader.configreader(ymalfilepath)
Base = automap_base()
engine = create_engine('postgresql+psycopg2://' + user + ':' + password + '@' + host + '/' + db, echo=True)

class Seller(Base):
    __tablename__ = 'seller'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    eneterydate = Column(DateTime)
    totalsales = Column(Integer)
    rated = Column(Boolean)


class Search(Base):
    __tablename__ = 'search'
    id = Column(Integer, primary_key=True)
    searchterm = Column(String(50), nullable=False)


class Sales(Base):
    __tablename__ = 'sales'
    seller_id = Column(Integer, ForeignKey('seller.id'))
    price =  Column(Numeric)
    date_of_sale = Column(DateTime)
    product_info =  Column(String(100))

#class Product(Base):
#    __tablename__ = 'product'
#    info = Column(String(500))
#    price = Column(Numeric)
#    rating = Column(Boolean)
#    page = Column(Integer)
#    seller_id = Column(Integer, ForeignKey('seller.id'))
#    date_id = Column(Integer, ForeignKey('pdates.id'))



class Pdates(Base):
    __tablename__ = 'pdates'
    id = Column(Integer, primary_key=True)
    dates = Column(Date)
    search_id = Column(Integer,ForeignKey('search.id'))





def loadSession():
    """"""
    metadata = Base.metadata
    #Session = sessionmaker(bind=engine)
    session = Session()
    return session

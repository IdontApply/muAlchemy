from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from . import configreader
from os import os.getenv
def connection_envi_var():
    user = = os.getenv('POSTGRES_USER')
    host = os.getenv('POSTGRES_HOST')
    password = os.getenv('POSTGRES_PASSWORD')
    db = os.getenv('POSTGRES_DATABASE')
    port = os.getenv('POSTGRES_PORT')
    return user, host, password, db, port
def tables():
    '''
    maps a postgres ecommerce database, returns the mapped ORM form of the tables
    needs a dbconfig.yaml to work
    '''
    user, host, password, db, port = connection_envi_var()
    Base = automap_base()
    engine = create_engine('postgresql+psycopg2://'+user+':'+password+'@'+host+':'+port+'/'+db, echo=True)
    Base.prepare(engine, reflect=True)

    session = Session(engine)
    pdates = Base.classes.pdates
    search = Base.classes.search
    product = Base.classes.product
    sales = Base.classes.sales
    seller = Base.classes.seller
    return pdates, search, product, sales, seller ,session

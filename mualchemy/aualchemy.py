from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from . import configreader


def tables(ymalfilepath):
    '''
    maps a postgres ecommerce database, returns the mapped ORM form of the tables
    needs a dbconfig.yaml to work
    '''
    user, host, password, db = configreader.configreader(ymalfilepath)
    Base = automap_base()
    engine = create_engine('postgresql+psycopg2://'+user+':'+password+'@'+host+'/'+db, echo=True)
    Base.prepare(engine, reflect=True)

    session = Session(engine)
    pdates = Base.classes.pdates
    search = Base.classes.search
    product = Base.classes.product
    sales = Base.classes.sales
    seller = Base.classes.seller
    return pdates, search, product, sales, seller ,session

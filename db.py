import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
import uuid
 
engine = sqlalchemy.create_engine('sqlite:///:memory:')
Base = declarative_base()
 
 
class Store_Category(Base):
  __tablename__ = 'store_category'
  id = Column(String(35), primary_key=True, unique=True)
  store_name = Column(String, ForeignKey('stores.store_name'), primary_key=True)
  category_name = Column(String, ForeignKey('categories.category_name'), primary_key=True)

  store = relationship("Store", backref=backref("store_category", cascade="all, delete-orphan" ))
  category = relationship("Category", backref=backref("store_category", cascade="all, delete-orphan" ))

  def __init__(self, store=None, category=None):
    self.id = uuid.uuid4().hex
    self.store = store
    self.category =  category

  def __repr__(self):
    return f"{self.store.store_name}: {self.category.category_name}"

class Store(Base):
  __tablename__ = 'stores'
  store_name = Column(String(35),  primary_key=True, unique=True)
  url = Column(String(200), nullable=False)

  categories = relationship("Category", secondary="store_category", viewonly=True)

  def add_category(self, category):
    self.store_category.append(Store_Category(store=self, category=category))      
 
  def __init__(self, name, url):
    self.store_name = name
    self.url = url
    self.categories =[]
   
  def __repr__(self):
    return '<Store {}>'.format(self.store_name)
 
 
class Category(Base):
    __tablename__ = 'categories'

    category_name = Column(String(35),  primary_key=True, unique=True)
    url = Column(String(200), nullable=False)
    category_id = Column(String(200), nullable=False)
    parent_category_id = Column(String(200), nullable=False)
    image_url = Column(String(500), nullable=False)
  
    stores = relationship("Store", secondary="store_category", viewonly=True)
 
    def __init__(self, name, url, category_id, parent_category_id, image_url):
        self.category_name = name
        self.url = url
        self.category_id = category_id
        self.parent_category_id = parent_category_id
        self.image_url = image_url
        self.stores=[]

    def __repr__(self):
        return '<Category {}>'.format(self.category_name)
 
 
 
Base.metadata.create_all(engine)
 
Session = sessionmaker(bind=engine)
session = Session()
 
produce = Category(name='produce', url='target/produce', category_id='123', parent_category_id='t123', image_url="/produceimage")
dairy = Category(name='dairy', url='/dairy', category_id='456', parent_category_id='wf123', image_url="/dairyimage")


session.add_all([produce, dairy])
session.commit()

target = Store( name = "Target", url="www.target.co")
wf = Store( name = "Whole Foods", url="www.wholefoods.com")


target.add_category(produce)
target.add_category(dairy)
wf.add_category(dairy)


session.commit()


print ("Categories array of target: ")
print (target.categories)
print ("Categories array of wf: ")
print (wf.categories)

print ("Stores array of produce: ")
print (produce.stores)
print ("Stores array of wf: ")
print (dairy.stores)

print ("Store_Category Array of target : ")
print (target.store_category)

print ("Store_Category Array of wf : ")
print (wf.store_category)
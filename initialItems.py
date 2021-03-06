from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="sandeephegde1990@gmail.com")
session.add(User1)
session.commit()

# Menu for Dominos Pizza
restaurant1 = Restaurant(name="Dominos Pizza", user_id="1")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Veg pizza",
                     description="Pizza made with vegetables",
                     price="130rs", restaurant=restaurant1, user_id=1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Pizaa",
                     description="Pizza with chicken",
                     price="200rs",  restaurant=restaurant1, user_id=1)

session.add(menuItem2)
session.commit()


# Menu for South India Restuarant
restaurant2 = Restaurant(name="Shree sagar")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Set Dosa",
                     description="Set Dosa served with chutney",
                     price="50rs", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Idly Vada",
                     description="Served with sambar and chutney",
                     price="30rs",  restaurant=restaurant2)

session.add(menuItem2)
session.commit()


print "Added items to database!"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, State, Park, User

engine = create_engine('sqlite:///parks.db')
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

# Add States

state1 = State(name="Alabama")

session.add(state1)
session.commit()


state2 = State(name="Alaska")

session.add(state2)
session.commit()


state3 = State(name="Arizona")

session.add(state3)
session.commit()


state4 = State(name="Arkansas")

session.add(state4)
session.commit()


state5 = State(name="California")

session.add(state5)
session.commit()


state6 = State(name="Colorado")

session.add(state6)
session.commit()


state7 = State(name="Connecticut")

session.add(state7)
session.commit()


state8 = State(name="Delaware")

session.add(state8)
session.commit()


state9 = State(name="Florida")

session.add(state9)
session.commit()


state10 = State(name="Georgia")

session.add(state10)
session.commit()


state11 = State(name="Hawaii")

session.add(state11)
session.commit()


state12 = State(name="Idaho")

session.add(state12)
session.commit()


state13 = State(name="Illinois")

session.add(state13)
session.commit()


state14 = State(name="Indiana")

session.add(state14)
session.commit()


state15 = State(name="Iowa")

session.add(state15)
session.commit()


state16 = State(name="Kansas")

session.add(state16)
session.commit()


state17 = State(name="Kentucky")

session.add(state17)
session.commit()


state18 = State(name="Louisiana")

session.add(state18)
session.commit()


state19 = State(name="Maine")

session.add(state19)
session.commit()


state20 = State(name="Maryland")

session.add(state20)
session.commit()


state21 = State(name="Massachusetts")

session.add(state21)
session.commit()


state22 = State(name="Michigan")

session.add(state22)
session.commit()


state23 = State(name="Minnesota")

session.add(state23)
session.commit()


state24 = State(name="Mississippi")

session.add(state24)
session.commit()


state25 = State(name="Missouri")

session.add(state25)
session.commit()


state26 = State(name="Montana")

session.add(state26)
session.commit()


state27 = State(name="Nebraska")

session.add(state27)
session.commit()


state28 = State(name="Nevada")

session.add(state28)
session.commit()


state29 = State(name="New Hampshire")

session.add(state29)
session.commit()


state30 = State(name="New Jersey")

session.add(state30)
session.commit()


state31 = State(name="New Mexico")

session.add(state31)
session.commit()


state32 = State(name="New York")

session.add(state32)
session.commit()


state33 = State(name="North Carolina")

session.add(state33)
session.commit()


state34 = State(name="North Dakota")

session.add(state34)
session.commit()


state35 = State(name="Ohio")

session.add(state35)
session.commit()


state36 = State(name="Oklahoma")

session.add(state36)
session.commit()


state37 = State(name="Oregon")

session.add(state37)
session.commit()


state38 = State(name="Pennsylvania")

session.add(state38)
session.commit()


state39 = State(name="Rhode Island")

session.add(state39)
session.commit()


state40 = State(name="South Carolina")

session.add(state40)
session.commit()


state41 = State(name="South Dakota")

session.add(state41)
session.commit()


state42 = State(name="Tennessee")

session.add(state42)
session.commit()


state43 = State(name="Texas")

session.add(state43)
session.commit()


state44 = State(name="Utah")

session.add(state44)
session.commit()


state45 = State(name="Vermont")

session.add(state45)
session.commit()


state46 = State(name="Virginia")

session.add(state46)
session.commit()


state47 = State(name="Washington")

session.add(state47)
session.commit()


state48 = State(name="West Virginia")

session.add(state48)
session.commit()


state49 = State(name="Wisconsin")

session.add(state49)
session.commit()


state50 = State(name="Wyoming")

session.add(state50)
session.commit()


print "Added states..."

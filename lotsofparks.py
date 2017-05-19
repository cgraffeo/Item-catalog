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


# Create dummy users
User1 = User(name="Bob Dole", email="bobdole@bobdole.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

User2 = User(name="Bill Clinton", email="billisgreat@scandle.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User2)
session.commit()

print "Added users..."


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

# Add park types
# parkType1 = ParkType(name="National Park", description="A scenic or historically important area of countryside protected by the federal government for the enjoyment of the general public or the preservation of wildlife.")

# session.add(parkType1)
# session.commit()

# parkType2 = ParkType(name="State Park", description="State parks are parks or other protected areas managed at the sub-national level within those nations which use 'state' as a political subdivision. State parks are typically established by a state to preserve a location on account of its natural beauty, historic interest, or recreational potential.")

# session.add(parkType2)
# session.commit()

# parkType3 = ParkType(name="County Park", description="A County park is an area of land preserved on account of its natural beauty, historic interest, recreational use or other reason, and under the administration of a form of local government.")

# session.add(parkType3)
# session.commit()

# parkType4 = ParkType(name="Town Park", description="A public playground, public recreation center or area, and other public areas, created, established, designated, maintained, provided or set aside by the City, for the purposes of public rest, play, recreation, enjoyment or assembly, and all buildings, facilities and structures located thereon or therein")

# session.add(parkType4)
# session.commit()

# parkType5 = ParkType(name="Dog Park", description="A dog park is a park for dogs to exercise and play off-leash in a controlled environment under the supervision of their owners.")

# session.add(parkType5)
# session.commit()

# print "Park types added..."

# Parks added by user 1

# park1 = Park(user_id=1, name="Sequoia National", description="Sweet place to go for many reasons", photo="https://images.unsplash.com/reserve/fGPqEBbuQrGjOAYy4kBz_IMGP5626-Edit.jpg?dpr=1&auto=format&fit=crop&w=1500&h=996&q=80&cs=tinysrgb&crop=&bg=", state=state1,
#              park_type="National")

# session.add(park1)
# session.commit()

# park2 = Park(user_id=1, name="Oregon State Park", description="Cool place found in Oregon", photo="https://images.unsplash.com/photo-1432912060512-39a70179afa4?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=", state=state2,
#              park_type="State")

# session.add(park2)
# session.commit()

# park3 = Park(user_id=1, name="Marion County Park", description="A park found in Marion County", photo="https://images.unsplash.com/photo-1431794015670-1761ebb156ba?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=", state=state3,
#              park_type="County")

# session.add(park3)
# session.commit()

# park4 = Park(user_id=1, name="Salem Town Park", description=" A park found in Salem, OR", photo="https://images.unsplash.com/photo-1431794062232-2a99a5431c6c?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=", state=state4,
#              park_type="Dog")

# session.add(park4)
# session.commit()

# park5 = Park(user_id=1, name="Run lots Dog park", description="Where doggos can come to run and be crazy!", photo="https://images.unsplash.com/photo-1472934488176-f0323f5da52d?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=", state=state5,
#              park_type="National")

# session.add(park5)
# session.commit()

# park6 = Park(user_id=1, name="Somewhere National", description="Come here to get lost in the awesome scenery", photo="https://images.unsplash.com/photo-1447522200268-a0378dac3fba?dpr=1&auto=format&fit=crop&w=1500&h=1004&q=80&cs=tinysrgb&crop=&bg=", state=state6,
#              park_type="State")

# session.add(park6)
# session.commit()

# park7 = Park(user_id=1, name="Get lost State", description="Lose yourself in this State park", photo="https://images.unsplash.com/photo-1462316104906-06c01d03785b?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=", state=state7,
#              park_type="Dog")

# session.add(park7)
# session.commit()

# park8 = Park(user_id=1, name="Another crazy park", description="Check out this nutso park found somewhere", photo="https://images.unsplash.com/reserve/Y1hediOeRoya666XCjYg_forest.jpg?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=", state=state8,
#              park_type="National")

# session.add(park8)
# session.commit()

# park9 = Park(user_id=1, name="Woof Woof Bowow", description="Woof Arf Arf Rrruf ruff", photo="https://images.unsplash.com/photo-1432842078269-0049eb805253?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=", state=state9,
#              park_type="County")

# session.add(park9)
# session.commit()

# park10 = Park(user_id=1, name="Lose my Sanity park", description="I'm tired of making new parks, this is the last one", photo="https://images.unsplash.com/photo-1430375642086-147fcd5fea57?dpr=1&auto=format&fit=crop&w=1500&h=817&q=80&cs=tinysrgb&crop=&bg=", state=state10,
#               park_type="State")

# session.add(park10)
# session.commit()

# print "Parks added..."
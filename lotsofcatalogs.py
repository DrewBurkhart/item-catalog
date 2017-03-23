from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Store, Base, CatItem, User

engine = create_engine('sqlite:///storecatalog.db')
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
User1 = User(name="Andrew Burkhart", email="Andrew@Andrew-Burhart.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Catalog for Stuffy's
store1 = Store(user_id=1, name="Stuffy\'s")

session.add(store1)
session.commit()

catItem0 = CatItem(user_id=1, name="Men\'s Pocket Tank", description="White and Grey Pocket Tank",
                     price="$19.99", category="Shirts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/297167150.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem0)
session.commit()


catItem1 = CatItem(user_id=1, name="View Tank", description="Men\'s tank with Palm Tree",
                     price="$31.99", category="Shirts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/295492957.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem1)
session.commit()

catItem2 = CatItem(user_id=1, name="Slasher Shorts", description="Men\'s CYA Slasher Shorts",
                     price="$25.50", category="Shorts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/294268523a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem2)
session.commit()

catItem3 = CatItem(user_id=1, name="Clubmaster Flash Sunglasses", description="Ray-Ban Clubmaster Flash sunglasses",
                     price="$43.99", category="Accessories", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/299936441a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem3)
session.commit()

catItem4 = CatItem(user_id=1, name="Nappy Pineapple Shorts", description="Men\'s Nappy Pineapple Shorts",
                     price="$27.99", category="Shorts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/294308100a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem4)
session.commit()

catItem5 = CatItem(user_id=1, name="Worldwide Domination Hat", description="Rebel 8 Worldwide Domination hat",
                     price="$31.99", category="Accessories", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/294504115a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem5)
session.commit()

catItem6 = CatItem(user_id=1, name="Nexpa LX Sandals", description="Van\'s Nexpa LX Sandals",
                     price="$46.99", category="Sandals", picture="https://www.tillys.com/tillys/images/catalog/300x300/295323947a.jpg", store=store1)

session.add(catItem6)
session.commit()

catItem7 = CatItem(user_id=1, name="Aloha Stripe Shorts", description="Floral Striped Shorts", 
                     price="$33.49", category="Shorts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/294158210a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem7)
session.commit()

catItem8 = CatItem(user_id=1, name="Mobbing Shorts", description="Rusty Men\'s Mobbing Shorts",
                     price="$35.99", category="Shorts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/295203320a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem8)
session.commit()


# Catalog for Jameson's
store2 = Store(user_id=1, name="Jameson\s")

session.add(store2)
session.commit()


catItem1 = CatItem(user_id=1, name="La Familia Tank", description="Men\'s Rose Tank",
                     price="$22.99", category="Shirts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/306445100.jpg?yocs=3_&yoloc=us", store=store2)

session.add(catItem1)
session.commit()

catItem2 = CatItem(user_id=1, name="Tropical Native Bear Tank", description="Men's Tropical Native Bear Tank", 
                     price="$25.99", category="Shirts", picture="https://www.tillys.com/tillys/images/catalog/300x300/292020150.jpg", store=store2)

session.add(catItem2)
session.commit()

catItem3 = CatItem(user_id=1, name="Revolution Shorts", description="Reef Revolution Men\'s Shorts",
                     price="$35.99", category="Shorts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/295493100a.jpg?yocs=3_&yoloc=us", store=store2)

session.add(catItem3)
session.commit()

catItem4 = CatItem(user_id=1, name="Dredges Shorts", description="Vissla Dredges Men\'s Shorts",
                     price="$32.99", category="Shorts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/293591110a.jpg?yocs=3_&yoloc=us", store=store2)

session.add(catItem4)
session.commit()

catItem5 = CatItem(user_id=1, name="Spaced Diver Shorts", description="Vissla Men\'s Spaced Diver Shorts",
                     price="$44.99", category="Shorts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/293593512a.jpg?yocs=3_&yoloc=us", store=store2)

session.add(catItem5)
session.commit()

catItem6 = CatItem(user_id=1, name="Rose Bowl Shorts", description="Ezekiel Rose Bowl Men\'s Shorts",
                     price="$32.99", category="Shorts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/295101100a.jpg?yocs=3_&yoloc=us", store=store2)

session.add(catItem6)
session.commit()


# Catalog for OB Drive
store1 = Store(user_id=1, name="OB Drive")

session.add(store1)
session.commit()


catItem1 = CatItem(user_id=1, name="Line Up Shorts", description="Men\'s Line Up Aloha Shorts",
                     price="$48.99", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/295774523a.jpg", store=store1)

session.add(catItem1)
session.commit()

catItem2 = CatItem(user_id=1, name="Homebreak Tank", description="Men\'s Homebreak Tank",
                     price="$16.99", category="Shirts", picture="https://www.tillys.com/tillys/images/catalog/300x300/302062150a.jpg", store=store1)

session.add(catItem2)
session.commit()

catItem3 = CatItem(user_id=1, name="RB4279 Glasses", description="Ray-Ban RB4279 Glasses",
                     price="$19.95", category="Accessories", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/299934100a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem3)
session.commit()

catItem4 = CatItem(user_id=1, name="Fanning Prints Sandals", description="Reef Men\'s Fanning Prints Sandals",
                     price="$36.99", category="Sandals", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/295110907a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem4)
session.commit()

catItem2 = CatItem(user_id=1, name="Field of Radness Shorts", description="Captain Fin Men\'s Field of Radness Shorts",
                     price="$39.50", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/291254700a.jpg", store=store1)

session.add(catItem2)
session.commit()


# Catalog for The Cantina
store1 = Store(user_id=1, name="The Cantina")

session.add(store1)
session.commit()


catItem1 = CatItem(user_id=1, name="Premier Sandals", description="Rainbow Premier Sandals",
                     price="$52.99", category="Sandals", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/500087429a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem1)
session.commit()

catItem2 = CatItem(user_id=1, name="Santa Cruz Stipe Shorts", description="O'Neill Men\'s Santa Cruz Stripe Shorts",
                     price="$45.99", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/293921284a.jpg", store=store1)

session.add(catItem2)
session.commit()

catItem3 = CatItem(user_id=1, name="Twinpin Sandals", description="Reef Twinpin Men\'s Sandals", 
                     price="$44.50", category="Sandals", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/295122400a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem3)
session.commit()

catItem4 = CatItem(user_id=1, name="Tippet Tank", description="Salty Crew Tippet Tank",
                     price="$19.95", category="Shirts", picture="https://www.tillys.com/tillys/images/catalog/300x300/298051100a.jpg", store=store1)

session.add(catItem4)
session.commit()

catItem5 = CatItem(user_id=1, name="Ducky Shorts", description="Neff Men\'s Ducky Hot Tub Volley Shorts",
                     price="$47.95", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/251438350a.jpg", store=store1)

session.add(catItem5)
session.commit()

catItem2 = CatItem(user_id=1, name="Statepark Shorts", description="Rip Curl Men\'s Statepark Shorts",
                     price="$36.80", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/288217300a.jpg", store=store1)

session.add(catItem2)
session.commit()


# Catalog for HB Surf Shop
store1 = Store(user_id=1, name="HB Surf Shop")

session.add(store1)
session.commit()


catItem1 = CatItem(user_id=1, name="Guideline Lo Tides Shorts", description="Bilabong Men\'s Guidelines Lo Tides Shorts",
                     price="$43.95", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/293799320a.jpg", store=store1)

session.add(catItem1)
session.commit()

catItem2 = CatItem(user_id=1, name="One and Only Shorts", description="Hurley Men\'s One and Only Shorts",
                     price="$34.95", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/292447351a.jpg", store=store1)

session.add(catItem2)
session.commit()

catItem3 = CatItem(user_id=1, name="Surf Trunks", description="Men\'s Surf Trunks",
                     price="$36.95", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/291696210a.jpg", store=store1)

session.add(catItem3)
session.commit()

catItem4 = CatItem(user_id=1, name="Brumeister Sandals", description="Salik Brumeister Sandals", 
                     price="$33.95", category="Sandals", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/298773400a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem4)
session.commit()

catItem5 = CatItem(user_id=1, name="Phantom Zion Shorts", description="Hurley Phantom Zion Shorts",
                     price="$47.95", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/304329100a.jpg", store=store1)

session.add(catItem5)
session.commit()


# Catalog for PCH Styles
store1 = Store(user_id=1, name="PCH Styles")

session.add(store1)
session.commit()


catItem1 = CatItem(user_id=1, name="Eastern Shorts", description="Men\'s Eastern Boardshorts",
                     price="$39.95", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/265364180a.jpg", store=store1)

session.add(catItem1)
session.commit()

catItem2 = CatItem(user_id=1, name="Hyperfreak Heist Shorts", description="O'Neill Hyperfreak Heist Men\'s Shorts",
                     price="$47.95", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/284082700a.jpg", store=store1)

session.add(catItem2)
session.commit()

catItem3 = CatItem(user_id=1, name="MF Men's T-Shirt", description="Rip Curl Men\'s Shirt",
                     price="$26.50", category="Shirts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/292059140.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem3)
session.commit()

catItem4 = CatItem(user_id=1, name="Eternal T-Shirt", description="Eternal Men\'s T-Shirt",
                     price="$26.75", category="Shirts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/294730100a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem4)
session.commit()

catItem2 = CatItem(user_id=1, name="Kelsey Psych Shorts", description="RVCA Kelsey Psych Shorts",
                     price="$57.00", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/292568957a.jpg", store=store1)

session.add(catItem2)
session.commit()


# Catalog for Jay's Surf and Snow
store1 = Store(user_id=1, name="Jay\'s Surf and Snow")

session.add(store1)
session.commit()

catItem9 = CatItem(user_id=1, name="Borderluck Shirt", description="Men\'s O\'Hurley Shirt", 
                     price="$18.99", category="Shirts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/299428100.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem9)
session.commit()


catItem1 = CatItem(user_id=1, name="Nexpa Synthetic Sandals", description="Vans Nexpa Synthetic Sandals",
                     price="$32.99", category="Sandals", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/295324125a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem1)
session.commit()

catItem2 = CatItem(user_id=1, name="Daily Sunglasses", description="Neff Daily Sunglasses",
                     price="$10.95", category="Accessories", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/292643957a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem2)
session.commit()

catItem3 = CatItem(user_id=1, name="Outcast T-shirt", description="Take me Surfing t-shirt", 
                     price="$27.50", category="Shirts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/293051150.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem3)
session.commit()

catItem4 = CatItem(user_id=1, name="Mirage Game Shorts", description="Mirage Game Men\'s Shorts",
                     price="$48.95", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/291601241a.jpg", store=store1)

session.add(catItem4)
session.commit()

catItem2 = CatItem(user_id=1, name="Retro Stripe Shorts", description="Rythym Retro Stripe Shorts",
                     price="$39.50", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/292973115a.jpg", store=store1)

session.add(catItem2)
session.commit()

catItem10 = CatItem(user_id=1, name="La Costa Lite Sandals", description="Vans La Costa Lite Sandals",
                      price="$21.99", category="Sandals", picture="https://www.tillys.com/tillys/images/catalog/300x300/295326125a.jpg", store=store1)

session.add(catItem10)
session.commit()


# Catalog for Active Ride Shop
store1 = Store(user_id=1, name="Active Ride Shop")

session.add(store1)
session.commit()


catItem1 = CatItem(user_id=1, name="Drydock Men\'s Shorts", description="Salty Crew Drydock Men\'s Shorts", 
                     price="$55.95", category="Shorts", picture="https://www.tillys.com/tillys/images/catalog/300x300/294152415a.jpg", store=store1)

session.add(catItem1)
session.commit()

catItem2 = CatItem(user_id=1, name="Aviators", description="Ray-Ban Aviator Sunglasses",
                     price="$167.99", category="Shorts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/299932441a.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem2)
session.commit()


store1 = Store(user_id=1, name="Cow Town")
session.add(store1)
session.commit()

catItem1 = CatItem(user_id=1, name="Drip Portrait Shirt", description="Men\'s Pink Dolphin Drip Portrait Shirt",
                     price="$125.95", category="Shirts", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/303165957.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem1)
session.commit

catItem1 = CatItem(user_id=1, name="Beer Cozy Sandals", description="Beer Cozy Men\'s Lite Sandals", 
                     price="$36.95", category="Sandals", picture="", store=store1)

session.add(catItem1)
session.commit()


catItem1 = CatItem(user_id=1, name="Reissue Trucker Hat", description="Billabong Resissue Trucker Hat", 
                     price="$24.25", category="Accessories", picture="https://cdn-us-cf2.yottaa.net/57f4626c312e584b1a000020/www.tillys.com/v~13.3e.0.0/tillys/images/catalog/300x300/292613100.jpg?yocs=3_&yoloc=us", store=store1)

session.add(catItem1)
session.commit()


print "added catalog items!"

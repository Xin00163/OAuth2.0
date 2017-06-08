from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Ingredient, Base, RecipeItem, User

engine = create_engine('sqlite:///ingredientrecipewithusers.db')
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
# User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
#              picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
# session.add(User1)
# session.commit()

# Recipe for UrbanBurger
ingredient1 = Ingredient(user_id=1, name="Beef")

session.add(ingredient1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Quick Beef Stir Fry", method="Juicy grilled veggie patty with tomato mayo and lettuce",
                     time_needed="$7.50", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="French Fries", method="with garlic and parmesan",
                     time_needed="$2.99", meal="Lunch", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Chicken Burger", method="Juicy grilled chicken patty with tomato mayo and lettuce",
                     time_needed="$5.50", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(user_id=1, name="Chocolate Cake", method="fresh baked and served with ice cream",
                     time_needed="$3.99", meal="Breakfast", ingredient=ingredient1)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(user_id=1, name="Sirloin Burger", method="Made with grade A beef",
                     time_needed="$7.99", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem4)
session.commit()

recipeItem5 = RecipeItem(user_id=1, name="Root Beer", method="16oz of refreshing goodness",
                     time_needed="$1.99", meal="Beverage", ingredient=ingredient1)

session.add(recipeItem5)
session.commit()

recipeItem6 = RecipeItem(user_id=1, name="Iced Tea", method="with Lemon",
                     time_needed="$.99", meal="Beverage", ingredient=ingredient1)

session.add(recipeItem6)
session.commit()

recipeItem7 = RecipeItem(user_id=1, name="Grilled Cheese Sandwich",
                     method="On texas toast with American Cheese", time_needed="$3.49", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem7)
session.commit()

recipeItem8 = RecipeItem(user_id=1, name="Veggie Burger", method="Made with freshest of ingredients and home grown spices",
                     time_needed="$5.99", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem8)
session.commit()


# Recipe for Super Stir Fry
ingredient2 = Ingredient(user_id=1, name="Super Stir Fry")

session.add(ingredient2)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Chicken Stir Fry", method="With your choice of noodles vegetables and sauces",
                     time_needed="$7.99", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Peking Duck",
                     method=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", time_needed="$25", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(user_id=1, name="Spicy Tuna Roll", method="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     time_needed="15", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(user_id=1, name="Nepali Momo ", method="Steamed dumplings made with vegetables, spices and meat. ",
                     time_needed="12", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem4)
session.commit()

recipeItem5 = RecipeItem(user_id=1, name="Beef Noodle Soup", method="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     time_needed="14", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem5)
session.commit()

recipeItem6 = RecipeItem(user_id=1, name="Ramen", method="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     time_needed="12", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem6)
session.commit()


# Recipe for Panda Garden
ingredient1 = Ingredient(user_id=1, name="Panda Garden")

session.add(ingredient1)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Pho", method="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     time_needed="$8.99", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Chinese Dumplings", method="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     time_needed="$6.99", meal="Lunch", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(user_id=1, name="Gyoza", method="light seasoning of Japanese gyoza with salt and soy sauce, and in a thin gyoza wrapper",
                     time_needed="$9.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(user_id=1, name="Stinky Tofu", method="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     time_needed="$6.99", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem4)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Veggie Burger", method="Juicy grilled veggie patty with tomato mayo and lettuce",
                     time_needed="$9.50", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()


# Recipe for Thyme for that
ingredient1 = Ingredient(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(ingredient1)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Tres Leches Cake", method="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     time_needed="$2.99", meal="Breakfast", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Mushroom risotto", method="Portabello mushrooms in a creamy risotto",
                     time_needed="$5.99", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(user_id=1, name="Honey Boba Shaved Snow",
                     method="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", time_needed="$4.50", meal="Breakfast", ingredient=ingredient1)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(user_id=1, name="Cauliflower Manchurian", method="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     time_needed="$6.95", meal="Lunch", ingredient=ingredient1)

session.add(recipeItem4)
session.commit()

recipeItem5 = RecipeItem(user_id=1, name="Aloo Gobi Burrito", method="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     time_needed="$7.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem5)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Veggie Burger", method="Juicy grilled veggie patty with tomato mayo and lettuce",
                     time_needed="$6.80", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()


# Recipe for Tony's Bistro
ingredient1 = Ingredient(user_id=1, name="Tony\'s Bistro ")

session.add(ingredient1)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Shellfish Tower", method="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     time_needed="$13.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Chicken and Rice", method="Chicken... and rice",
                     time_needed="$4.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(user_id=1, name="Mom's Spaghetti", method="Spaghetti with some incredible tomato sauce made by mom",
                     time_needed="$6.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     method="Milk, cream, salt, ..., Liquid nitrogen magic", time_needed="$3.95", meal="Breakfast", ingredient=ingredient1)

session.add(recipeItem4)
session.commit()

recipeItem5 = RecipeItem(user_id=1, name="Tonkatsu Ramen", method="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     time_needed="$7.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem5)
session.commit()


# Recipe for Andala's
ingredient1 = Ingredient(user_id=1, name="Andala\'s")

session.add(ingredient1)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Lamb Curry", method="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     time_needed="$9.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Chicken Marsala", method="Chicken cooked in Marsala wine sauce with mushrooms",
                     time_needed="$7.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(user_id=1, name="Potstickers", method="Delicious chicken and veggies encapsulated in fried dough.",
                     time_needed="$6.50", meal="Lunch", ingredient=ingredient1)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(user_id=1, name="Nigiri Sampler", method="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     time_needed="$6.75", meal="Lunch", ingredient=ingredient1)

session.add(recipeItem4)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Veggie Burger", method="Juicy grilled veggie patty with tomato mayo and lettuce",
                     time_needed="$7.00", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()


# Recipe for Auntie Ann's
ingredient1 = Ingredient(user_id=1, name="Auntie Ann\'s Diner' ")

session.add(ingredient1)
session.commit()

recipeItem9 = RecipeItem(user_id=1, name="Chicken Fried Steak",
                     method="Fresh battered sirloin steak fried and smothered with cream gravy", time_needed="$8.99", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem9)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Boysenberry Sorbet", method="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     time_needed="$2.99", meal="Breakfast", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Broiled salmon", method="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     time_needed="$10.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(user_id=1, name="Morels on toast (seasonal)",
                     method="Wild morel mushrooms fried in butter, served on herbed toast slices", time_needed="$7.50", meal="Lunch", ingredient=ingredient1)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(user_id=1, name="Tandoori Chicken", method="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     time_needed="$8.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem4)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Veggie Burger", method="Juicy grilled veggie patty with tomato mayo and lettuce",
                     time_needed="$9.50", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()

recipeItem10 = RecipeItem(user_id=1, name="Spinach Ice Cream", method="vanilla ice cream made with organic spinach leaves",
                      time_needed="$1.99", meal="Breakfast", ingredient=ingredient1)

session.add(recipeItem10)
session.commit()


# Recipe for Cocina Y Amor
ingredient1 = Ingredient(user_id=1, name="Cocina Y Amor ")

session.add(ingredient1)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Super Burrito Al Pastor",
                     method="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", time_needed="$5.95", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Cachapa", method="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     time_needed="$7.99", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()


ingredient1 = Ingredient(user_id=1, name="State Bird Provisions")
session.add(ingredient1)
session.commit()

recipeItem1 = RecipeItem(user_id=1, name="Chantrelle Toast", method="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     time_needed="$5.95", meal="Lunch", ingredient=ingredient1)

session.add(recipeItem1)
session.commit

recipeItem1 = RecipeItem(user_id=1, name="Guanciale Chawanmushi",
                     method="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)", time_needed="$6.95", meal="Breakfast", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Lemon Curd Ice Cream Sandwich",
                     method="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews", time_needed="$4.25", meal="Breakfast", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()


print "added recipe items!"

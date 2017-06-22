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


ingredient1 = Ingredient(user_id=1, name="Beef")

session.add(ingredient1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Quick Beef Stir Fry", method="Heat vegetable oil in a large wok or skillet over medium-high heat; cook and stir beef until browned, 3 to 4 minutes. Move beef to the side of the wok and add broccoli, bell pepper, carrots, green onion, and garlic to the center of the wok. Cook and stir vegetables for 2 minutes. Stir beef into vegetables and season with soy sauce and sesame seeds. Continue to cook and stir until vegetables are tender, about 2 more minutes.",
                    time_needed="25", meal="Lunch", ingredient=ingredient1)

session.add(recipeItem2)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Mushroom Slow Cooker Roast Beef", method="Place the mushrooms in the bottom of a slow cooker; set the roast atop the mushrooms; sprinkle the onion soup mix over the beef and pour the beer over everything; season with black pepper. Set slow cooker to LOW; cook 9 to 10 hours until the meat is easily pulled apart with a fork.",
                     time_needed="540", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem1)
session.commit()


recipeItem3 = RecipeItem(user_id=1, name="Boeuf Bourguignon", method="Heat oil in a skillet over medium heat. Cook onions until tender and transfer to a bowl. Cook and stir beef in the same skillet until browned. Sprinkle flour, marjoram, thyme, and pepper over beef. Pour red wine and beef broth into the skillet; stir well. Reduce heat to low and simmer until beef is tender. Stir onions into the skillet. Add mushrooms.",
                     time_needed="154", meal="Dinner", ingredient=ingredient1)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(user_id=1, name="Horsey Beef Pretzel Bites", method="Arrange Pretzel Crisps(R) onto a large tray. Top with roast beef and a piece of mozzarella cheese. Add a slice or 2 of red onion. Put a dollop (about 1/4 teaspoon) of horseradish on the onion. Garnish with chives.",
                     time_needed="50", meal="Lunch", ingredient=ingredient1)

session.add(recipeItem4)
session.commit()

recipeItem5 = RecipeItem(user_id=1, name="Salisbury Steak", method="In a large bowl, mix together 1/3 cup condensed onion soup with ground beef, bread crumbs, egg, salt and black pepper. Shape into 6 oval patties. In a skillet over medium-high heat, brown both sides of patties. In a small bowl, blend flour and remaining soup until smooth. Mix in ketchup, water, Worcestershire sauce and mustard powder. Pour over meat in skillet. Cover and cook for 20 minutes.",
                     time_needed="40", meal="Lunch", ingredient=ingredient1)

session.add(recipeItem5)
session.commit()


ingredient2 = Ingredient(user_id=1, name="Pork")

session.add(ingredient2)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Apple Butter Pork Loin", method="Season the pork loins with seasoning salt, and place them in a baking dish. Pour apple juice over the pork, and cover the dish with a lid. Bake for 1 hour. While the pork is roasting, mix together the apple butter, brown sugar, water, cinnamon, and cloves. Remove pork roasts from the oven, and spread with apple butter mixture. Cover, and return to the oven for 2 hours.",
                     time_needed="195", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Sweet and Sour Pork",
                     method="Place cubed pork in a medium bowl, and season with salt, sugar and soy sauce. Mix in the egg white and green onions. Cover, and place in the refrigerator at least 1 hour. Heat oil to 365 degrees F in a large saucepan. Coat the pork with cornstarch, and fry in the heated oil about 10 minutes. Drain on paper towels. Stir in the celery, green bell pepper, and onion, and cook until tender. Mix 1 cup water, 1/4 teaspoon salt, 3/4 cup sugar, apple cider vinegar, ketchup, and 1/2 teaspoon soy sauce. Bring to a boil, and stir in the cooked pork, celery mixture, and the pineapple chunks with juice. Return to boil, and mix in cornstarch and water to thicken.", time_needed="120", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(user_id=1, name="Delicious Ham and Potato Soup", method="Combine the potatoes, celery, onion, ham and water in a stockpot. Bring to a boil, then cook over medium heat until potatoes are tender, about 10 to 15 minutes. Stir in the chicken bouillon, salt and pepper.In a separate saucepan, melt butter over medium-low heat. Whisk in flour with a fork, and cook, stirring constantly until thick, about 1 minute. Slowly stir in milk as not to allow lumps to form until all of the milk has been added. Continue stirring over medium-low heat until thick, 4 to 5 minutes. Stir the milk mixture into the stockpot, and cook soup until heated through.",
                     time_needed="45", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem3)
session.commit()

recipeItem4 = RecipeItem(user_id=1, name="NPork Tenderloin in the Slow Cooker ", method="Place pork tenderloin in a slow cooker with the contents of the soup packet. Pour water, wine, and soy sauce over the top, turning the pork to coat. Carefully spread garlic over the pork, leaving as much on top of the roast during cooking as possible. Sprinkle with pepper, cover, and cook on low setting for 4 hours. ",
                     time_needed="275", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem4)
session.commit()

recipeItem5 = RecipeItem(user_id=1, name="Best Grilled Pork Chops", method="Mix water, soy sauce, vegetable oil, lemon pepper seasoning, and minced garlic in a deep bowl; add pork chops and marinate in refrigerator at least 2 hours. Preheat an outdoor grill for medium-high heat and lightly oil the grate. Remove pork chops from the marinade and shake off excess. Discard the remaining marinade. Cook the pork chops on the preheated grill until no longer pink in the center, 5 to 6 minutes per side. An instant-read thermometer inserted into the center should read 145 degrees F (63 degrees C).",
                     time_needed="135", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem5)
session.commit()

recipeItem6 = RecipeItem(user_id=1, name="BBQ Pork for Sandwiches", method="Pour can of beef broth into slow cooker, and add boneless pork ribs. Cook on High heat for 4 hours, or until meat shreds easily. Remove meat, and shred with two forks. It will seem that it's not working right away, but it will. Preheat oven to 350 degrees F (175 degrees C). Transfer the shredded pork to a Dutch oven or iron skillet, and stir in barbeque sauce. Bake in the preheated oven for 30 minutes, or until heated through.",
                     time_needed="295", meal="Dinner", ingredient=ingredient2)

session.add(recipeItem6)
session.commit()



ingredient3 = Ingredient(user_id=1, name="Chicken")

session.add(ingredient3)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Chicken and vegetable pie", method="Preheat oven to 220 C Gas mark 7.In a saucepan, combine chicken, carrots, peas and celery. Add water to cover and boil for 15 minutes. Remove from heat, drain and set aside. In the saucepan over medium heat, cook onion in butter until soft and translucent. Stir in flour, salt, pepper and celery seed. Slowly stir in chicken stock and milk. Simmer over medium-low heat until thick. Remove from heat and set aside. Prepare a 23cm (9 in) pie dish by lining with pastry, reserving pastry to cover. Place the chicken mixture in bottom of the prepared pie dish. Pour hot liquid mixture over. Cover with top pastry, seal edges, and cut away excess pastry. Make several small slits in the top to allow steam to escape. Bake in the preheated oven for 30 to 35 minutes, or until pastry is golden brown and filling is bubbly. Cool for 10 minutes before serving.",
                     time_needed="70", meal="Dinner", ingredient=ingredient3)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Chicken jalfrezi", method="Heat the oil in a large deep frying pan over medium-high heat. Add onions and garlic, and cook for about 2 minutes. Add the chicken, and season with turmeric, chilli powder and salt. Fry gently, scraping the bottom of the pan frequently and turning the chicken. Pour in the tomatoes with their juice, cover the pan, and simmer over medium heat for 20 minutes. Uncover, and simmer for another 10 minutes to let the excess liquid evaporate. Add the ghee, cumin, ground coriander, ginger and fresh coriander, and simmer for another 5 to 7 minutes. Serve the chicken pieces with sauce spooned over the top.",
                     time_needed="75", meal="Lunch", ingredient=ingredient3)

session.add(recipeItem2)
session.commit()

recipeItem3 = RecipeItem(user_id=1, name="Slow cooker butter chicken", method="Heat the butter and vegetable oil in a large frying pan over medium heat. Stir in the chicken, onion and garlic. Cook and stir until the onion has softened and turned translucent, about 10 minutes. Stir in the curry powder, curry paste, tandoori masala, garam masala and tomato puree until no lumps of tomato puree remain. Pour into a slow cooker, and stir in the cardamom pods, coconut milk and yoghurt. Season to taste with salt. Cook on High 4 to 6 hours, or on Low 6 to 8 hours until the chicken is tender and the sauce has reduced to your desired consistency. ",
                     time_needed="270", meal="Dinner", ingredient=ingredient3)

session.add(recipeItem3)
session.commit()



ingredient4 = Ingredient(user_id=1, name="Eggs")

session.add(ingredient1)
session.commit()


recipeItem1 = RecipeItem(user_id=1, name="Pesto Scrambled Eggs", method="Heat oil in a frying pan over medium heat. In a small bowl, combine egg, Cheddar, salt and pepper. Pour into pan, and cook stirring for 3 to 5 minutes, or until desired doneness. Remove from heat, and stir in pesto.",
                     time_needed="10", meal="Breakfast", ingredient=ingredient4)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Curry devilled eggs", method="Cut the eggs in half lengthways. Remove the yolks and put them in a bowl with the paprika, mayonnaise, curry powder, creme fraiche, lemon, salt, Worcestershire and mustard powder. Mix well. Fill each egg white with the yolk mixture. Serve chilled.",
                     time_needed="15", meal="Breakfast", ingredient=ingredient4)

session.add(recipeItem2)
session.commit()

ingredient5 = Ingredient(user_id=1, name="Fruit")

session.add(ingredient1)
session.commit()

recipeItem1 = RecipeItem(user_id=1, name="Groovy green smoothie", method="Place the banana, grapes, yoghurt, apple and spinach into a blender or food processor. Cover, and blend until smooth, stopping frequently to push down anything stuck to the sides. Pour into glasses and serve.",
                     time_needed="10", meal="Beverage", ingredient=ingredient5)

session.add(recipeItem1)
session.commit()

recipeItem2 = RecipeItem(user_id=1, name="Bitter and Twisted", method="Put a few ice-cubes in a glass. Pour in bacardi, pineapple and grapefruit juice. Pour into a cocktail mixer and shake. Pour the mixed cocktail into the glass again the add sparkling water. Serve with cherries, pineapple and umbrellas, if you like!",
                     time_needed="5", meal="Beverage", ingredient=ingredient5)

session.add(recipeItem2)
session.commit()



print "added recipe items!"

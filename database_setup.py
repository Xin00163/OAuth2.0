from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
           'user_id'      : self.user_id
       }

class RecipeItem(Base):
    __tablename__ = 'recipe_item'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    method = Column(String(250))
    time_needed = Column(String(8))
    meal = Column(String(250))
    ingredient_id = Column(Integer,ForeignKey('ingredient.id'))
    ingredient = relationship(Ingredient)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'method'         : self.method,
           'id'         : self.id,
           'time_needed'         : self.time_needed,
           'meal'         : self.meal,
       }



engine = create_engine('sqlite:///ingredientrecipewithusers.db')


Base.metadata.create_all(engine)

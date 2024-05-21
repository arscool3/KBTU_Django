# Project - ResWipe-  a website to share recipes and advices in cooking as "articles" among users. 
# Users can write comments under the articles. 
# Users can check the availability of the ingredients based on their location

# FastAPI, dramatiq, Postgre, sqlalchemy, alembic...

# ----------------------

# from sqlalchemy import Table, Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# # Define association table for many-to-many relationship
# recipe_category_association = Table('recipe_category_association', Base.metadata,
#     Column('recipe_id', Integer, ForeignKey('recipe.id')),
#     Column('category_id', Integer, ForeignKey('category.id'))
# )

# class Recipe(Base):
#     __tablename__ = 'recipe'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     categories = relationship("Category", secondary=recipe_category_association, back_populates="recipes")

# class Category(Base):
#     __tablename__ = 'category'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     recipes = relationship("Recipe", secondary=recipe_category_association, back_populates="categories")

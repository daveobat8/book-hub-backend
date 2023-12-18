from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR,  Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, backref
#create a basemodel
Base = declarative_base()

#define Books model

class Books(Base):
    __tablename__= "books"

    #define columns
    id= Column(Integer(), primary_key=True)
    title= Column(Text(), nullable=False)
    description= Column(VARCHAR, nullable=False)
    author= Column(Text(), nullable=False)
    image= Column(VARCHAR, nullable=False)
    genre= Column(Text(), nullable=False)
    price= Column(Integer(), nullable=False)
    added_at= Column(TIMESTAMP, nullable=False)


class User(Base):
    __tablename__= 'users'

    #define columns
    id= Column(Integer(), primary_key=True)
    name= Column(Text(), nullable=False)
    phone= Column(VARCHAR, nullable=False)
    email= Column(VARCHAR, nullable=False)

    catalogue= relationship('Catalogue', backref='user')

class Catalogue(Base):
    __tablename__= 'catalogues'

    #define columns
    id= Column(Integer(), primary_key=True)
    title= Column(Text(), nullable=False)
    description= Column(VARCHAR, nullable=False)
    author= Column(Text(), nullable=False)
    image= Column(VARCHAR, nullable=False)
    genre= Column(Text(), nullable=False)
    price= Column(Integer(), nullable=False)
    added_at= Column(TIMESTAMP, nullable=False)

    #foreign keys
    book_id= Column(Integer(), ForeignKey('books.id'))
    user_id= Column(Integer(), ForeignKey('users.id'))


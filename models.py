from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR,  Integer, TIMESTAMP
#create a basemodel
Base = declarative_base()

#define Books model

class Books(Base):
    __tablename__= "books"

    #define columns
    id= Column(Integer(), primary_key=True)
    title= Column(Text())
    description= Column(VARCHAR)
    author= Column(Text())
    image= Column(VARCHAR)
    price= Column(Integer())
    added_at= Column(TIMESTAMP)

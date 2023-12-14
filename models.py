from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR,  Integer, TIMESTAMP
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
    price= Column(Integer(), nullable=False)
    added_at= Column(TIMESTAMP, nullable=False)

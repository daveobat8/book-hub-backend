from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connect to out postgre database
engine = create_engine("postgresql://admin:zPnxxBE0m5LNcZpFefEnjSKY2OUMyEW4@dpg-cltkuoq1hbls738lgt50-a.frankfurt-postgres.render.com/book_vwik", echo=True)

#create a connection with sessionmaker
SessionLocal = sessionmaker(bind=engine)

# method to get database
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
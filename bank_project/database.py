
#create engine --> etesal dataabse anham bedim ba url
from sqlalchemy import create_engine

#declarative_base --> ORM --> databse -->python class estefade koni 
from sqlalchemy.orm import declarative_base,sessionmaker


#mysql , ....
DATABASE_URL = "sqlite:///database.db"

engine= create_engine(DATABASE_URL,echo=False)

Base = declarative_base()


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#helper
def get_session():
    return SessionLocal()

def init_db():
    from models import Customer, Account, Transaction  # Import all models
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")


if __name__ == "__main__":
    init_db()

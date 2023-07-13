from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./studentDATABASE.sqlite"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

sessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)

base=declarative_base()

def get_db():
    db=sessionLocal()
    try:
        yield db
    except Exception as e:
        pass
    finally:
        db.close()

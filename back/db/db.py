from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/helpdesk"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

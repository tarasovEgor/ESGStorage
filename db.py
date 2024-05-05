from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "postgresql://postgres:password@localhost:5431/reports_db"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)


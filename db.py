from sqlmodel import create_engine, SQLModel, Session

# Previous container url
# DATABASE_URL = "postgresql://postgres:password@localhost:5431/reports_db"

DATABASE_URL = 'postgresql://postgres:mypassword@reports_db_test:5432/database'

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
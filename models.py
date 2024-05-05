from sqlmodel import SQLModel, Field


class CompanyBase(SQLModel):
    comapny_name: str
    link: str
    inn: str
    year: int
    

class Company(CompanyBase, table=True):
    id: int = Field(default=None, primary_key=True)
from sqlmodel import SQLModel, Field


class CompanyBase(SQLModel):
    company_name: str
    link: str
    inn: str
    year: int
    

class Company(CompanyBase, table=True):
    id: int = Field(default=None, primary_key=True)


class PostCompanyItem(CompanyBase):
    pass


class PostCompanyRequest(SQLModel):
    data: list[PostCompanyItem] = Field(
        default=None
    )


class PostCompanyRequestResponse(SQLModel):
    data: list[PostCompanyItem] = Field(
        default=None
    )

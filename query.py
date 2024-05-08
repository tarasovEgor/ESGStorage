from sqlmodel import Session
from sqlmodel import select
from models import Company


async def create_companies(
        session: Session,
        company_name: list[str],
        company_link: list[str],
        company_year: list[int],
        company_inn: list[str]
) -> list[Company]:
    existing_companies = [(c.company_name, c.link, c.inn, c.year) 
                          for c in (session.scalars(select(Company))).all()]
    company = [
        Company(
            company_name=company_name, link=company_link,
            inn=company_inn, year=company_year
        )
        for company_name, company_link, company_inn, company_year in zip(
            company_name, company_link, company_inn, company_year
            )
        if (company_name, company_link, company_inn, company_year) not in existing_companies
    ]
    session.add_all(company)
    session.commit()
    return company

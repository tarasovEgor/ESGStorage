from fastapi import FastAPI, HTTPException, Depends, Query, Path
from models import Company, PostCompanyItem, PostCompanyRequest, PostCompanyRequestResponse
from contextlib import asynccontextmanager
from sqlmodel import Session
from query import create_companies
from typing import Annotated
from db import init_db, get_session


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/company/{company_id}")
async def get_company_by_id(
    company_id: Annotated[int, Path(title="The company ID")],
    session: Session = Depends(get_session)
) -> Company:
    company = session.get(Company, company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found.")
    return company


@app.post("/company")
async def post_company(
    company_data: PostCompanyItem,
    session: Session = Depends(get_session)
) -> Company:
    company = Company(
        company_name=company_data.company_name, link=company_data.link,
        inn=company_data.inn, year=company_data.year
    )
    session.add(company)
    session.commit()
    session.refresh(company)
    return company
    

@app.post("/companies")
async def post_companies(
    company_data: PostCompanyRequest,
    session: Session = Depends(get_session)
) -> PostCompanyRequestResponse:
    company_names = [c.company_name for c in company_data.data]
    company_links = [c.link for c in company_data.data]
    company_years = [c.year for c in company_data.data]
    company_inns = [c.inn for c in company_data.data]
    companies = await create_companies(
        session, company_names, company_links, company_years, company_inns
    )
    return PostCompanyRequestResponse(
        data=[
            PostCompanyItem(
                company_name=c.company_name, link=c.link,
                inn=c.inn, year=c.year
            )
            for c in companies
        ]
    )

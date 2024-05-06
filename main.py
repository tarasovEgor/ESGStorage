from fastapi import FastAPI, HTTPException, Depends, Query, Path
from contextlib import asynccontextmanager
from sqlmodel import Session
from typing import Annotated
from models import Company, CompanyCreate
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
async def create_company(
    company_data: CompanyCreate,
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
    

from fastapi import APIRouter
from schemas.company import CompanyCreate,CompanyUpdate

router=APIRouter(prefix="/company",tags=["company"])
companies=[]

@router.post("/")
def create_company(company:CompanyCreate):
    companies.append(company)
    return companies


@router.post("/")
def read_company_id(company:Company_id):
    return companies[company]


@router get("/{company_id}")
def update_company_id(company:Company_id):
    return companies[company]

@router put("/{company_id}")
def delete_company_id(company:Company_id):
    return companies[company]

@router.get("/")
def get_all_company():
    return companies

@router.get("/")
def get_all_company(company_id:int):
    return companies[company_id]

# @router.get("/")
# def read_company():
#     return("company""company root")

# @router.get("/{company_id}")
# def read_company(company_id:int):
#     return{"company_id": company_id}
from fastapi import APIRouter

router=APIRouter(prefix="/job",tags=["job"])
jobs=[]

@router.post("/")
def create_job(job:jobCreate):
    jobs.append(job)
    return jobs

@router.get("/")
def get_all_job():
    return jobs


@router.get("/")
def read_job():
    return("job" "job root")

@router.get("/{job_id}")
def read_job(job_id:int):
    return {"job_id":job_id}
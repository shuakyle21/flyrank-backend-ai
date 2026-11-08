from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.llm.config import get_settings
from src.llm.schemas import Classification
from src.llm.schemas import JobEmail

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_handler(request: Request, exc: RequestValidationError):
    errors = [
        {
            "field": ".".join(str(p) for p in e["loc"][1:]) or "body",
            "message": e["msg"],
        }
        for e in exc.errors()
    ]
    return JSONResponse(
        status_code=400,
        content={"detail": "invalid request body", "errors": errors},
    )


@app.post("/classify", response_model=Classification)
def classify_email(email: JobEmail) -> Classification:
    if get_settings().llm_stub:
        return Classification(status=None, company=None, job_title=None, max_stage=1)
    raise HTTPException(status_code=503, detail="model not wired yet")



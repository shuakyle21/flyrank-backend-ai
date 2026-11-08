import os
from enum import StrEnum
from pydantic import BaseModel, ConfigDict, Field

class Status(StrEnum):
    APPLIED = "applied"
    VIEWED_BY_EMPLOYER = "viewed by employer"
    IN_REVIEW = "in review"
    ASSESSMENT = "assessment"
    INTERVIEW_SCHEDULED = "interview scheduled"
    OFFER = "offer"
    REJECTED = "rejected"
    TALENT_POOL = "talent pool"

class RuleHints(BaseModel):
    model_config = ConfigDict(extra="forbid")

    company: str = ""
    job_title: str = ""

class JobEmail(BaseModel):
    model_config = ConfigDict(extra="forbid")

    subject: str
    raw_text: str = Field(max_length=4000)
    from_address: str
    known_from_rules: RuleHints = Field(default_factory=RuleHints)

class Classification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Status | None
    company: str | None
    job_title: str | None
    max_stage: int = Field(ge=1, le=4)
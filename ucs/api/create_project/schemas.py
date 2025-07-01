from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl, constr

class MemberIn(BaseModel):
    email: constr(max_length=255) # type: ignore
    function: Optional[str] = None

class LinkIn(BaseModel):
    title: Optional[str] = None
    url: HttpUrl

class DocumentIn(BaseModel):
    filename: str

class ProjectCreate(BaseModel):
    title: constr(max_length=255) # type: ignore
    subtitle: Optional[str]
    description: Optional[str]
    category_id: int
    stage_id: int
    invest_amount: Optional[int]
    members: List[MemberIn] = Field(default_factory=list)
    links: List[LinkIn] = Field(default_factory=list)
    documents: List[DocumentIn] = Field(default_factory=list)
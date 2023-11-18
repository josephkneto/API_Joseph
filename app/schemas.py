from pydantic import BaseModel

class MemberBase(BaseModel):
    quote: str

class MemberCreate(MemberBase):
    pass

class MemberUpdate(MemberBase):
    pass


class DeletedResponse(BaseModel):
    message: str

class Member(MemberBase):
    id: int

    class Config:
        orm_mode = True

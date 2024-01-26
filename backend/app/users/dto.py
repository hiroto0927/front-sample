from typing import Optional
from pydantic import BaseModel, ConfigDict


class Create(BaseModel):
    name: str
    is_admin: bool
    is_active: bool
    is_notice: bool

    model_config = ConfigDict(from_attributes=True)


class Update(BaseModel):
    id: int
    name: Optional[str] = None
    is_admin: Optional[bool] = None
    is_active: Optional[bool] = None
    is_notice: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)

from typing import Optional
from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    id: int
    name: str
    is_admin: bool
    is_active: bool
    is_notice: bool


class UserCreate(BaseModel):
    name: str
    is_admin: bool
    is_active: bool
    is_notice: bool


class UserUpdate(BaseModel):
    name: Optional[str] = None
    is_admin: Optional[bool] = None
    is_active: Optional[bool] = None
    is_notice: Optional[bool] = None

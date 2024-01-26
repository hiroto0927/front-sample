from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.users import controller as UserCtrl
from sqlalchemy.orm import Session
from config.db import get_db_pgwea
from app.users import schema as UserSchm, dto as UserDTO

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=List[UserSchm.User])
def get_users(db: Session = Depends(get_db_pgwea)):
    return UserCtrl.get_users(db)


@router.get("/{id}", response_model=UserSchm.User)
def get_user(id: int, db: Session = Depends(get_db_pgwea)):
    return UserCtrl.get_user(id, db)


@router.post("", response_model=UserSchm.User)
def add_user(user: UserSchm.UserCreate, db: Session = Depends(get_db_pgwea)):
    user_dto = UserDTO.Create.model_validate(user.model_dump())
    return UserCtrl.add_user(db, user_dto)


@router.patch("/{id}", response_model=UserSchm.User)
def update_user(
    id: int, user: UserSchm.UserUpdate, db: Session = Depends(get_db_pgwea)
):
    user_dto = UserDTO.Update.model_validate({"id": id, **user.model_dump()})
    return UserCtrl.update_user(user_dto, db)


@router.delete("/{id}", response_model=None, status_code=204)
def delete_user(id: int, db: Session = Depends(get_db_pgwea)):
    return UserCtrl.delete_user(id, db)

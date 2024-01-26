from sqlalchemy.orm import Session
from app.users import dto as UserDTO, model as UserModel, exception as Exc
from fastapi import HTTPException


def add_user(db: Session, user: UserDTO.Create):
    return UserModel.create_user(user, db)


def get_users(db: Session):
    return UserModel.get_users(db)


def get_user(user_id: int, db: Session):
    try:
        return UserModel.get_user(user_id, db)
    except Exc.NotFoundUserException:
        raise HTTPException(status_code=404, detail="User not found")


def update_user(user: UserDTO.Update, db: Session):
    try:
        return UserModel.update_user(user, db)
    except Exc.NotFoundUserException:
        raise HTTPException(status_code=404, detail="User not found")


def delete_user(user_id: int, db: Session):
    try:
        return UserModel.delete_user(user_id, db)
    except Exc.NotFoundUserException:
        raise HTTPException(status_code=404, detail="User not found")

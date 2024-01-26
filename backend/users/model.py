from backend.users.entity import User
from sqlalchemy.orm import Session
from sqlalchemy import insert
from backend.users import dto as UserDTO,entity as UserEntity

def create_user(db:Session,user:UserDTO.Create) ->   User:
    




    
    stmt = insert(UserEntity).values(user)

    return user
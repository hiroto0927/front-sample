from app.users.entity import User
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from app.users import dto as UserDTO
from app.users.entity import User as UserEntity
from sqlalchemy.exc import NoResultFound
from app.users import exception as Exc


def create_user(user: UserDTO.Create, db: Session) -> User:
    stmt = insert(UserEntity).values(user.model_dump()).returning(UserEntity)
    user = db.execute(stmt).scalar_one()
    db.commit()
    return user


def get_users(db: Session) -> User:
    stmt = select(UserEntity).order_by(UserEntity.id)

    return db.execute(stmt).scalars().all()


def get_user(user_id: int, db: Session) -> User:
    stmt = select(UserEntity).where(UserEntity.id == user_id)

    try:
        return db.execute(stmt).scalar_one()
    except NoResultFound:
        raise Exc.NotFoundUserException()


def update_user(user: UserDTO.Update, db: Session) -> User:
    stmt = (
        update(UserEntity)
        .where(UserEntity.id == user.id)
        .values(user.model_dump(exclude_none=True))
        .returning(UserEntity)
    )
    try:
        user = db.execute(stmt).scalar_one()
        db.commit()
        return user
    except NoResultFound:
        db.rollback()
        raise Exc.NotFoundUserException()


def delete_user(user_id: int, db: Session) -> None:
    stmt = delete(UserEntity).where(UserEntity.id == user_id)

    result = db.execute(stmt)
    db.commit()

    if result.rowcount == 0:
        raise Exc.NotFoundUserException()

    return

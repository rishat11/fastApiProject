from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound

from database.models import Employee
from database.models import Status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(user) -> Employee:
    user.password = pwd_context.encrypt(user.password)

    try:
        user_obj = await Employee.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(status_code=401,
                            detail=f"Sorry, that username already exists.")

    return await user_obj


async def delete_user(user_id, current_user) -> Status:
    try:
        db_user = await Employee.get(id=user_id)
    except NoResultFound:
        raise HTTPException(status_code=404,
                            detail=f"User {user_id} not found")

    if db_user.id == current_user.id:
        deleted_count = await Employee.filter(id=user_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404,
                                detail=f"User {user_id} not found")
        return Status(message=f"Deleted user {user_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")

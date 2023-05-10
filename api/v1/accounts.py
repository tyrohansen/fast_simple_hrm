from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from core.database import get_db
from core.models import User
from api.v1.account_schemas import UserBaseSchema

router = APIRouter()


@router.get('/')
def get_users(db: Session=Depends(get_db), limit: int = 10, page:int=1, search:str =''):
    skip = (page - 1) * limit
    users = db.query(User).filter(
        User.username.contains(search)
    ).limit(limit=limit).offset(skip).all()
    return {'count':len(users), "results":users}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(payload: UserBaseSchema, db: Session=Depends(get_db)):
    return {}
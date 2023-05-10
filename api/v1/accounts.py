from fastapi import APIRouter, Depends, HTTPException, status, Response
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
    user = User(**payload.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get('/{id}')
def get_user(id: str, db: Session=Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} not found!")
    return user



@router.patch('/{id}')
def update_user(id: str, payload: UserBaseSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id:{id} not found!")
    
    data = payload.dict(exclude_unset=True)
    db.query(User).filter(User.id == id).update(data, synchronize_session=False)
    db.commit()
    db.refresh(user)
    return user



@router.delete('/{id}')
def delete_user(id: str, db: Session = Depends(get_db)):
    user_query = db.query(User).filter(User.id == id)
    if not user_query.first():
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found!")
    
    user_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

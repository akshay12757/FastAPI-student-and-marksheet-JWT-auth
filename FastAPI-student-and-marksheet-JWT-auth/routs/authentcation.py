from fastapi import APIRouter,Depends,HTTPException,status
from schema import loginSchema
from fastapi.security import OAuth2PasswordRequestForm 
from hash_convert import Hash
from database_connection import get_db
from routs.tokenAuth import create_access_token
from sqlalchemy.orm import Session
from models import studentModel


router=APIRouter()

@router.post('/Logins')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(studentModel).filter(studentModel.email==request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Student as username {request.username} and password {request.password} not found')
    
    if not Hash.varify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="password is wrong")
    
    tokanJWT=create_access_token(data={"sub":user.name})
    return {"access_token": tokanJWT, "token_type": "bearer"}
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Response,Depends,APIRouter
from schema import studentSchema,ShowstudentSchema,showMarksSheet,marksheetSchema
import schema,database_connection,models,hash_convert
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext

router=APIRouter(tags=["student"])
models.base.metadata.create_all(database_connection.engine)

def get_db():
    db=database_connection.sessionLocal()
    try:
        yield db
    except Exception as e:
        pass
    finally:
        db.close()



################################ User #################################


@router.post("/register",response_model=ShowstudentSchema)
def register(student:studentSchema,db:Session=Depends(get_db)):
    newStudent=models.studentModel(name=student.name,email=student.email,password=hash_convert.Hash.bcrypt(student.password))
    db.add(newStudent)
    db.commit()
    db.refresh(newStudent)
    return newStudent



@router.get("/students",response_model=List[ShowstudentSchema])
def studentsList(db:Session=Depends(get_db)):
    studentsList=db.query(models.studentModel).all()
    return studentsList

@router.get("/student/{id}")
def gstStudent(id:int,db:Session=Depends(get_db)):
    try:
        student=db.query(models.studentModel).get(id)
        print(student)
        if student:
            return student
        else:
            return {"msg": "student not found "}
    except Exception as error:
        return {'error': error}
    
    
@router.delete("/student/{id}")
def deleteStudent(id:int,db:Session=Depends(get_db)):
    deletedStudent=db.query(models.studentModel).filter(models.studentModel.id==id).delete(synchronize_session=False)
    db.commit()
    return deletedStudent

@router.put("/student/{id}",response_model=ShowstudentSchema)
def updateStudent(id:int,student:studentSchema,db:Session=Depends(get_db)):
    studentQuery = db.query(models.studentModel).filter(models.studentModel.id == id)
    studentQuery.update({"name": student.name, "email": student.email, "password": hash_convert.Hash.bcrypt(student.password)})
    db.commit()
    updatedStudent = studentQuery.first()
    return updatedStudent

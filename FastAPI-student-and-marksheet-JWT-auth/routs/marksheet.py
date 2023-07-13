from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Response,Depends,APIRouter
from schema import studentSchema,ShowstudentSchema,showMarksSheet,marksheetSchema
import schema,database_connection,models,hash_convert
from routs.oauth2Token import get_current_user
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from repository.marks import getAllMarksheets
router=APIRouter(tags=["marksheets"])
models.base.metadata.create_all(database_connection.engine)
def get_db():
    db=database_connection.sessionLocal()
    try:
        yield db
    except Exception as e:
        pass
    finally:
        db.close()

## return all marksheet with Students
@router.get("/marksheets")#,response_model=List[showMarksSheet])
def marksheetList(db:Session=Depends(get_db),get_current_user:schema.studentSchema=Depends(get_current_user)):
    marksheetsList=getAllMarksheets(db)
    return marksheetsList

## add marks
@router.post("/addMarks",response_model=showMarksSheet)
def addMarks(marksheet:marksheetSchema,db:Session=Depends(get_db)):
    print(marksheet)
    newMarksheet=models.markssheetModel(stud_id=marksheet.stud_id,marks=marksheet.marks)
    db.add(newMarksheet)
    db.commit()
    db.refresh(newMarksheet)
    return newMarksheet

## return single mark sheet 
@router.get("/marksheet/{id}",response_model=showMarksSheet)
def gstMarksheet(id:int,db:Session=Depends(get_db)):
    try:
        marksheet=db.query(models.markssheetModel).get(id)
        print(marksheet)
        if marksheet:
            return marksheet
        else:
            return {"msg": "marksheet not found "}
    except Exception as error:
        return {'error': error}
 
@router.delete("/marksheet/{id}")
def deleteMarksheet(id:int,db:Session=Depends(get_db)):
    deletedMarksheet=db.query(models.markssheetModel).filter(models.markssheetModel.id==id).delete(synchronize_session=False)
    db.commit()
    return deletedMarksheet

## update marksheet
@router.put("/marksheeet/{id}",response_model=ShowstudentSchema)
def updateStudent(id:int,marksheet:marksheetSchema,db:Session=Depends(get_db)):
    marksheetQuery = db.query(models.markssheetModel).filter(models.markssheetModel.id == id)
    marksheetQuery.update({"marks":marksheet.marks})
    db.commit()
    updatedStudent = marksheetQuery.first()
    return updatedStudent

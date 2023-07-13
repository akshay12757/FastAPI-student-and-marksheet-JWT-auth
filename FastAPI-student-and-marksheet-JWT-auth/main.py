from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Response,Depends
from schema import studentSchema,ShowstudentSchema,showMarksSheet,marksheetSchema
import schema, database_connection, models, hash_convert
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from routs import marksheet, student,authentcation
app=FastAPI()
templates = Jinja2Templates(directory="")
# models.base.metadata.create_all(database.engine)

app.include_router(student.router)

app.include_router(marksheet.router)

app.include_router(authentcation.router)

@app.get("/")
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# def get_db():
#     db=database.sessionLocal()
#     try:
#         yield db
#     except Exception as e:
#         pass
#     finally:
#         db.close()


# ################################ User #################################


# @app.post("/register",response_model=ShowstudentSchema)
# def register(student:studentSchema,db:Session=Depends(get_db)):
#     newStudent=models.studentModel(name=student.name,email=student.email,password=hash.Hash.bcrypt(student.password))
#     db.add(newStudent)
#     db.commit()
#     db.refresh(newStudent)
#     return newStudent



# @app.get("/students",response_model=List[ShowstudentSchema])
# def studentsList(db:Session=Depends(get_db)):
#     studentsList=db.query(models.studentModel).all()
#     return studentsList

# @app.get("/student/{id}")
# def gstStudent(id:int,db:Session=Depends(get_db)):
#     try:
#         student=db.query(models.studentModel).get(id)
#         print(student)
#         if student:
#             return student
#         else:
#             return {"msg": "student not found "}
#     except Exception as error:
#         return {'error': error}
    
    
# @app.delete("/student/{id}")
# def deleteStudent(id:int,db:Session=Depends(get_db)):
#     deletedStudent=db.query(models.studentModel).filter(models.studentModel.id==id).delete(synchronize_session=False)
#     db.commit()
#     return deletedStudent

# @app.put("/student/{id}",response_model=ShowstudentSchema)
# def updateStudent(id:int,student:studentSchema,db:Session=Depends(get_db)):
#     studentQuery = db.query(models.studentModel).filter(models.studentModel.id == id)
#     studentQuery.update({"name": student.name, "email": student.email, "password": hash.Hash.bcrypt(student.password)})
#     db.commit()
#     updatedStudent = studentQuery.first()
#     return updatedStudent

############################# markssheets #########################

# ## add marks
# @app.post("/addMarks",response_model=showMarksSheet)
# def addMarks(marksheet:marksheetSchema,db:Session=Depends(get_db)):
#     print(marksheet)
#     newMarksheet=models.markssheetModel(stud_id=marksheet.stud_id,marks=marksheet.marks)
#     db.add(newMarksheet)
#     db.commit()
#     db.refresh(newMarksheet)
#     return newMarksheet


# ## return all marksheet with Students
# @app.get("/marksheets",response_model=List[showMarksSheet])
# def marksheetList(db:Session=Depends(get_db)):
#     marksheetsList=db.query(models.markssheetModel).all()
#     return marksheetsList


## return single mark sheet 
# @app.get("/marksheet/{id}",response_model=showMarksSheet)
# def gstMarksheet(id:int,db:Session=Depends(get_db)):
#     try:
#         marksheet=db.query(models.markssheetModel).get(id)
#         print(marksheet)
#         if marksheet:
#             return marksheet
#         else:
#             return {"msg": "marksheet not found "}
#     except Exception as error:
#         return {'error': error}
    
## delete the marksheet  
# @app.delete("/marksheet/{id}")
# def deleteMarksheet(id:int,db:Session=Depends(get_db)):
#     deletedMarksheet=db.query(models.markssheetModel).filter(models.markssheetModel.id==id).delete(synchronize_session=False)
#     db.commit()
#     return deletedMarksheet

# ## update marksheet
# @app.put("/marksheeet/{id}",response_model=ShowstudentSchema)
# def updateStudent(id:int,marksheet:marksheetSchema,db:Session=Depends(get_db)):
#     marksheetQuery = db.query(models.markssheetModel).filter(models.markssheetModel.id == id)
#     marksheetQuery.update({"marks":marksheet.marks})
#     db.commit()
#     updatedStudent = marksheetQuery.first()
#     return updatedStudent

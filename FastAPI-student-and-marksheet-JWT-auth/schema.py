from typing import List
from pydantic import BaseModel
from typing import Optional
class marksheetSchema(BaseModel):
    stud_id:int
    marks:int
    
    
# class ShowmarksheetSchema(BaseModel):
#     stud_id:int
#     marks:int

class studentSchema(BaseModel):
    name:str
    email:str
    password:str
    # class Config():
    #     orm_mode=True
        
    # class Config():
    #     orm_mode=True

class showMarksSheet(BaseModel):
    student:studentSchema
    marks:int
    
class ShowstudentSchema(BaseModel):
    name:str
    email:str
    marksheets:List[showMarksSheet]
    # class Config():
    #     orm_mode=True

class loginSchema(BaseModel):
    email:str
    password:str
    
class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:Optional[str]=None
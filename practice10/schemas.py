from pydantic import BaseModel

class BaseUniversity(BaseModel):
    
    name: str 
    description:str
    class Config:
        from_attributes=True
        
class University(BaseUniversity):
    id:int

class CreateUniversity(BaseUniversity):
    pass


class BaseSchool(BaseModel):
    
    name: str 
    description:str
    class Config:
        from_attributes=True
        
class School(BaseSchool):
    id:int
    university_id:int

class CreateSchool(BaseSchool):
    university:University




class BaseFaculty(BaseModel):
    
    name: str 
    description:str
    class Config:
        from_attributes=True
        
class Faculty(BaseFaculty):
    id:int
    faculty_id:int

class CreateFaculty(BaseFaculty):
    faculty:Faculty


class BaseHuman(BaseModel):
    name:str
    class Config:
        from_attributes=True


class Student(BaseHuman):
    id:int
    gpa:float
    faculty_id:int

class CreateStudent(BaseHuman):
    faculty:Faculty


class Teacher(BaseHuman):
    id:int
    degree:str
    school_id:int

class CreateTeacher(BaseHuman):
    school:School





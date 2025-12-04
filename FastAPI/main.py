from fastapi import FastAPI, Path, HTTPException,Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, computed_field, Field
from typing import Annotated, Literal, Optional

app = FastAPI()

# POST - C
# GET - R
# PUT - U
# DELETE - D

# GET

def load_data():
    with open('./patients.json', 'r') as f:
        data = json.load(f)
    return data
def save_data(data):
    with open('./patients.json', 'w') as f:
        json.dump(data, f)

@app.get('/')
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message':'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()
    return data

# path params # Path in Fastapi for description regarding the path params
# {patient_id} is dynamic segment

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the Patients in the DB', example='P001')):
    # load all the patient
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

#Title, Description, Example, (ge, gt, le, lt), max-length, min_length, regex

# HTTP status codes
# 2xx - The request was sucessfully received and processed
# 3xx - Further action needs to be taken (eg redirect)
# 4xx - Something is wrong with the request from the client
# 5xx - something went wrong on the server side

# 200 OK - standard success (a get or post succeeded)
# 201 Created - resource created (after a post that creates something)
# 204 No content - success, but no data returned (after a delete request)

# 400 Bad request - malformed or invalid request (missing field wrong data type)
# 401 unauthorized - no/invalid authentication (login requird)
# 403 forbidden - authenticated but no permission (logged in but not allowed)
# 404 not found

# 500 internal server error - generic failure (something broke on the server)
# 502 bad gateway - gateway like nginx failed to reach backend
# 503 service unavailable - server is down or overloaded

# using httpexception

# Query parameter - sorted data
# sortby=(what to be sorted (bmi, height etc)), order (decen, ascend)
# if not given default ascend or descend

# http://domain/endpoint?City=delhi&sortby=age
# The ? marks the start of query parameter
#  each parameter is a key-value pair key=value
# multiple parameters are seperated by &

# in this case
# city=delhi is a query for filtering
# sort_by=age is a query for sorting

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='sort on the basis of height, weight or bmi'),
                  order:str = Query('asc', description='sort in asc or desc')): # use Query() for similar Path() like thing
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'invalid field select from valid field {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='invalid order select between asc and desc')
    
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

# POST
# post data and validating the data using pydantic model, and then adding the data to json file

class Patient(BaseModel):
    
    id: Annotated[str, Field(..., description='ID of the Patient', example='P001')]
    name: Annotated[str, Field(..., description='Name of the Patient', example='John Doe')]
    city: Annotated[str, Field(..., description='City of the Patient', example='New York')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the Patient', example=30)]
    gender: Annotated[str,Literal['Male', 'Female', 'Other'], Field(..., description='Gender of the Patient', example='Male')]
    height: Annotated[float, Field(..., gt=0, description='Height of the Patient in meters', example=1.75)]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the Patient in kg', example=70.2)]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        bmi = self.bmi
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 24.9:
            return 'Normal weight'
        elif 25 <= bmi < 29.9:
            return 'Overweight'
        else:
            return 'Obesity'
    

@app.post('/create')
def create_patient(patient: Patient):    
    # load existing data
    data = load_data()
    
    # check if the patient id already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient ID already exists')
    
    # new patient added to the database
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    # save the data back to the json file
    save_data(data)
    return JSONResponse(status_code=201, content={'message':'Patient created successfully'})

# PUT
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default = None)]
    city: Annotated[Optional[str], Field(default = None)]
    age: Annotated[Optional[int], Field(default = None, gt=0, lt=120)]
    gender: Annotated[Optional[str], Literal['male', 'female', 'other'], Field(default = 'male')]
    height: Annotated[Optional[float], Field(default = None, gt=0)]
    weight: Annotated[Optional[float], Field(default = None, gt=0)]
    
@app.put('/edit/{patient_id}')
def update_patient(patient_id: str = Path(..., description='ID of the Patient to be updated', example='P001'),
                   patient_update: PatientUpdate = ...):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    existing_patient_data = data[patient_id]
    updated_patient_data = patient_update.model_dump(exclude_unset=True)
    
    for key, value in updated_patient_data.items():
        existing_patient_data[key] = value
        
    # existing_patient_data -> pydantic object -> updated bmi and verdict
    existing_patient_data['id'] = patient_id  # add id back for pydantic model
    patient_pydantic_object = Patient(**existing_patient_data)  # Recalculate computed fields
    
    # pydantic_object -> dict excluding id
    existing_patient_data = patient_pydantic_object.model_dump(exclude=['id'])
    
    # add back to the main data
    data[patient_id] = existing_patient_data
    save_data(data)
    return JSONResponse(status_code=200, content={'message':'Patient updated successfully'})

# DELETE
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str = Path(..., description='ID of the Patient to be deleted', example='P001')):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    # delete the patient
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200, content={'message':'Patient deleted successfully'})    
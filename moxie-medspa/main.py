from fastapi import FastAPI
from pydantic import BaseModel
from models import ServiceModel, AppointmentModel
import json


class Service(BaseModel):
    name: str
    description: str
    price: float
    duration: int
    

class Appointment(BaseModel):
    start_time: str
    total_duration: int
    total_price: float
    services: list
    

app = FastAPI()

"""
Service

"""

@app.post("/create-service/")
async def create_service(service: Service):
    service_model = ServiceModel()
    res = service_model.create_service(service)
    if (res):
        return {"code": 1, "message": "service successfully created"}
    else:
        return {"code": 0, "message": "service could not be created"}
    


@app.put("/update-service/")
async def update_service_by_id(service: Service):
    service_model = ServiceModel()
    res = service_model.update_service_by_id(service)
    if (res):
        return {"code": 1, "message": "Service successfully updated"}
    else:
        return {"code": 0, "message": "Service could not be updated"}


@app.get("/services/")
async def list_all_services_by_medspa_id(medspa_id: str):
    return {"message": "Welcome to Moxie"}


@app.get("/service/{service_id}")
async def show_service_by_id(service_id: str):
    service_model = ServiceModel()
    res = service_model.show_service_by_id(service_id)
    return {"message": "Welcome to Moxie"}


"""
Appointement

"""

@app.post("/create-appointment/")
async def create_appointment(appointment: Appointment):
    start_time = appointment.start_time
    services = appointment.services
    services_list = services
    total_price = 0;
    total_duration = 0;
    for each_service in services_list:
        each_service_dict = dict(each_service)
        total_price += each_service_dict["price"]
        total_duration += each_service_dict["duration"]
    appointment.total_price = total_price
    appointment.total_duration = total_duration
    appointment_model = AppointmentModel()
    res = appointment_model.create_appointment(appointment)
    if (res):
        return {"code": 1, "message": "Appointment successfully created"}
    else:
        return {"code": 0, "message": "An error occured. Appointment could not be created"}
    
    


@app.get("/appointments/update/{appointment_id}")
async def update_appointment_status(appointment_id: str):
    return {"message": "Welcome to Moxie"}


@app.get("/appointments/id/{appointment_id}")
async def show_appointment_by_id(appointment_id: str):
    return {"message": "Welcome to Moxie"}



@app.get("/appointments/status/{status_id}")
async def list_all_appointments_by_status(appointment_id: str):
    return {"message": "Welcome to Moxie"}


@app.get("/appointments/start-date/{appointment_id}")
async def list_all_appointments_by_start_date():
    return {"message": "Welcome to Moxie"}


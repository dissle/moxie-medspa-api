#from datetime import timedelta
import json
import psycopg2



class ServiceModel:

    def create_service(self, service):
        #pass#Todo: db insert with postgresql db adapter
        with open("data/create_service.json", 'w') as file:
            data = service.dict();
            json.dump(data, file, indent=4)
            
        

    def update_service_by_id(self, service_id, service):
        #pass#Todo: db update with postgresql db adapter
        #sql UPDATE service SET ... WHERE id = service_id and medspa_id = medspa_id
        with open("data/update_service.json", 'w') as file:
            data = service.dict();
            json.dump(data, file, indent=4)
            
    
    
    def list_all_services_by_medspa_id(medspa_id):
        pass#Todo: db select with postgresql db adapter
        #sql SELECT x, y, z FROM service WHERE medspa_id = medspa_id
        # with open("data/services.json", 'w') as file:
            # data = service.dict();
            # json.dump(data, file, indent=4)
        
    
    def show_service_by_id(service_id):
        pass#Todo: db select with postgresql db adapter
        #sql SELECT x, y, z FROM service WHERE medspa_id = medspa_id AND service_id = service_id
        #with open("data/services.json", 'w') as file:
        #    data = service.dict();
        #    json.dump(data, file, indent=4)



class AppointmentModel:    
    
    
    def create_appointment(self, appointment):
        pass #Todo: db insert with postgresql db adapter
        #SQL: INSERT INTO ....
        with open("data/create_appointment.json", 'w') as file:
            data = appointment.dict()
            json.dump(data, file, indent=4)
            #return true of successfull and false if it fails
    
    
    def update_appointment_status_by_id(self, status_id, medspa_id):
        #pass #Todo: db update with postgresql db adapter
        #sql UPDATE appointment SET status = [status_id] WHERE id = appointment_id and medspa_id = medspa_id
        with open("data/update_appointment.json", 'w') as file:
            pass
   
    
    
    def show_appointment_by_id(self, appointment_id, medspa_id):
        #pass #Todo: db select with postgresql db adapter
        #sql SELECT x, y, z FROM appointment WHERE id = appointment_id AND medspa_id = medspa_id
        appointments_dict = {}
        #appointment_dict = {}
        with open("data/appointments.json", "r") as file:
            appointments_data = json.load(file)
            appointments_dict = dict(appointments_data)
        for each_appointment in appointments_dict:
            if appointment_id == each_appointment['appointment_id']:
                return each_appointment['appointment_id']
                
    
    
    def list_all_appointments_by_status_id(self, status_id, medspa_id):
        pass #Todo: db select with postgresql db adapter
        
        
    
    def list_all_appointments_by_start_date(self, status_id, medspa_id):
        pass #Todo: db select with postgresql db adapter
        
        
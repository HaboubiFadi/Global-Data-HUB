from faker import Faker
from faker_vehicle import VehicleProvider
import random
import uuid

fake = Faker()
fake.add_provider(VehicleProvider)

# List of vehicle types
vehicle_types = ['Truck', 'Van', 'Car', 'Ship', 'Airplane']

# Function to generate fake vehicle fleet usage data
def generate_fake_vehicle_fleet_usage(num_vehicles, num_months):
    fleet_usage = []
    monthly_costs_list = []
    monthly_income_list = []
    monthly_driving_list = []
    maintenance_month_list = []  
    monthly_usage_list=[]
    vehicle_id_liste=[]
    driver_id_liste=[]
    monthly_usage_list=[]
    for _ in range(num_vehicles):
        # Vehicle information
        vehicle_id = str(uuid.uuid4())
        vehicle_id_liste.append(vehicle_id)
        vehicle_type = random.choice(vehicle_types)
        mileage_start = random.uniform(1000, 10000)
        mileage_end = mileage_start + random.uniform(500, 1500)
        vehicle_make = fake.vehicle_make_model()
        vehicle_model = fake.vehicle_model()
        vehicle_year = fake.random_int(min=2000, max=2023)
        vehicle_capacity = random.uniform(1000, 10000)
        vehicle_fuel_type = random.choice(['Gasoline', 'Diesel', 'Electric'])
        vehicle_license_plate = fake.license_plate()
        vehicle_insurance_expiry = fake.future_date(end_date='+1y')
        vehicle_status = random.choice(['Available', 'In Use', 'Under Maintenance'])
        last_maintenance_date = fake.date_time_between(start_date='-100d', end_date='now')
        maintenance_cost = random.uniform(100, 1000)
        maintenance_history = [(fake.date_between(start_date='-180d', end_date='now'), random.uniform(50, 500)) for _ in range(5)]
        driver_name = fake.name()
        delivery_completed = random.randint(0, 100)
        on_time_delivery = random.randint(0, delivery_completed)
        driver_rating = round(random.uniform(3.0, 5.0), 2)


        driver_id=fake.uuid4()
        driver_id_liste.append(driver_id)

        driving_type=random.choice(['A', 'B', 'C'])
        num_infractions=random.randint(1, 20)
        num_accidents=random.randint(1, 20)
        
        monthly_usage = []
        monthly_costs = []
        monthly_income = []
        monthly_driving = []
        maintenance_history = [] 



        for month in range(1, num_months + 1):
            id=str(uuid.uuid4())
            income = random.uniform(2000, 5000)

            monthly_income.append({
                'Vehicle_ID': vehicle_id,
                'month_month': month,
                'id': id,
                'Income': income
            })

        for month in range(1, num_months + 1):
         
            id_usage=str(uuid.uuid4())
            distance_traveled = random.uniform(200, 800)
            mileage_end += distance_traveled
         
            monthly_usage.append({
                'Vehicle_ID': vehicle_id,
                'month_month': month,
                'id': id_usage,
                'Distance_Traveled': distance_traveled,
                'Mileage_End': mileage_end
            })
        for month in range(1, num_months + 1):
            maintenance_date = fake.date_between(start_date='-180d', end_date='now')
            maintenance_year = maintenance_date.year
            maintenance_month=month
            maintenance_cost = random.uniform(50, 500)
            id_history=str(uuid.uuid4())
            
            maintenance_history.append({
                'Vehicle_ID': vehicle_id,
   
                'id_maintenance': id_history,
                'date_date': maintenance_date.strftime('%Y-%m-%d'),
        'Cost_maintenance': maintenance_cost,
       
            })

      
        for month in range(1, num_months + 1):
            id_costs=str(uuid.uuid4())

            income = random.uniform(2000, 5000)
            fuel_cost = random.uniform(50, 500)
            other_costs = random.uniform(10, 100)
            maintenance_cost = random.uniform(100, 1000)
            total_cost = maintenance_cost + fuel_cost + other_costs
  

            monthly_costs.append({
                'Vehicle_ID': vehicle_id,
                'month_month': month,
                'id': id_costs,
                'Maintenance_Cost': maintenance_cost,
            'Fuel_cost': fuel_cost,
                'Other_Costs': other_costs,
                'Total_Cost': total_cost,
            })

        for month in range(1, num_months + 1):
            id_driving=str(uuid.uuid4())
            driving_time = random.uniform(50, 400)
            traffic_violation_nb = random.uniform(0, 10)

            monthly_driving.append({
                'Vehicle_ID': vehicle_id,
                'Month_': month,
                'id_driving': id_driving,
                'Driving_Time': driving_time,
                'Traffic_Violation_Number': traffic_violation_nb,
            })

        utilization_rate = random.uniform(60, 100) #The percentage of time each vehicle is in use compared to its availability.
        idle_time = random.uniform(0, 100) #The amount of time each vehicle spends idle or not in use
        vehicle_data = {
            'Vehicle_ID': vehicle_id,
            'Vehicle_Type': vehicle_type,
            'Mileage_Start': mileage_start,
            'Vehicle_Make': vehicle_make,
            'Vehicle_Model': vehicle_model,
            'Vehicle_Year': vehicle_year,
            'Vehicle_Capacity': vehicle_capacity,
            'Vehicle_Fuel_Type': vehicle_fuel_type,
            'License_Plate': vehicle_license_plate,
            'Insurance_Expiry': vehicle_insurance_expiry.strftime('%Y-%m-%d'),
            'Vehicle_Status': vehicle_status,
            'Utilization_Rate': utilization_rate,
            'idle_time': idle_time,
            'Driver_Name': driver_name,
            'Deliveries_Completed': delivery_completed,
            'On_Time_Deliveries': on_time_delivery,
            'Driver_Rating': driver_rating,
            'driver_id': driver_id,
            'driving_type': driving_type,
            'num_infractions': num_infractions,
            'num_accidents':num_accidents
        }

        fleet_usage.append(vehicle_data)
        monthly_usage_list.extend(monthly_usage)
        monthly_costs_list.extend(monthly_costs)
        monthly_driving_list.extend(monthly_driving)
        monthly_income_list.extend(monthly_income)
        maintenance_month_list.extend(maintenance_history)

    
    
        pre_json_liste=[{'fleet_usage':fleet_usage},
        {'monthly_usage_list':monthly_usage_list},
        {'maintenance_month_list':maintenance_month_list},
        {'monthly_costs_list':monthly_costs_list},
        {'monthly_driving_list':monthly_driving_list},
        {'monthly_income_list':monthly_income_list}]

    return pre_json_liste,vehicle_id_liste,driver_id_liste   

from datetime import timedelta
import pandas as pd
# Function to generate fake freight shipment delivery performance data
def generate_fake_delivery_performance(num_shipments,vehicule_id_liste,driver_id_liste):
    delivery_performance = []
    transport_modes = ['Truck', 'Ship', 'Airplane', 'Train']
    for _ in range(num_shipments):
         # Shipment Information
        shipment_id = fake.uuid4()
        sender_name = fake.name()
        sender_address = fake.address()
        receiver_name = fake.name()
        receiver_address = fake.address()
        shipment_weight = random.uniform(100, 1000)
        shipment_volume = random.uniform(5, 50)
        shipment_type = random.choice(['Perishable', 'Hazardous', 'General Cargo'])
        #Estimated Time of Arrival (ETA): The expected time of arrival at the destination.
        shipment_status = random.choice(['In Transit', 'Delivered', 'Delayed', 'Blocked'])
        # Transporter information
        carrier_id=fake.uuid4()
        carrier_name = fake.company()
        transport_mode = random.choice(transport_modes)
        vehicle_id = vehicule_id_liste[random.randint(0,len(vehicule_id_liste))-1]
        vehicle_capacity = random.uniform(10000, 50000)
        driver_id =driver_id_liste[random.randint(0,len(driver_id_liste))-1]

        driver_name = fake.name()
        #Route information
        departure_location = fake.city()
        arrival_location = fake.city()
        departure_date = fake.date_time_between(start_date='-30d', end_date='+30d')
        arrival_date = departure_date + pd.Timedelta(hours=random.randint(1, 100))
        transit_time = (arrival_date - departure_date).total_seconds() / 3600
        distance_traveled = random.uniform(50, 500)
        eta=arrival_date + timedelta(days=random.uniform(0, 3)) #Estimated Time of Arrival (ETA): The expected time of arrival at the destination.
         #Calculate the time difference
        time_difference = eta - arrival_date
        # Check if the time difference is greater than 2 days
        threshold = timedelta(days=1)
        if time_difference < threshold:
            on_time_delivery= True
        else:
            on_time_delivery= False

        freight_cost = random.uniform(500, 5000)
        billing_status = random.choice(['Paid', 'Pending', 'Overdue'])
        # feedback
        customer_feedback = fake.paragraph(nb_sentences=random.randint(1, 3))
        customer_rating = random.randint(1, 5)
       
        performance_data = {
            'Shipment_ID': shipment_id,
            'Sender_Name': sender_name,
            'Sender_Address': sender_address,
            'Receiver_Name': receiver_name,
            'Receiver_Address': receiver_address,
            'Shipment_Weight': shipment_weight,
            'Shipment_Volume': shipment_volume,
            'Shipment_Type': shipment_type,
            'Shipment_Status': shipment_status,
            'Carrier_ID': carrier_id,
            'Carrier_Name': carrier_name,
            'Transport_Mode': transport_mode,
            'Vehicle_ID': vehicle_id,
            'Vehicle_Capacity': vehicle_capacity,
            'Driver_ID': driver_id,
            'Driver_Name': driver_name,
            'Departure_Location': departure_location,
            'Arrival_Location': arrival_location,
            'Departure_Date': departure_date.strftime("%Y/%m/%d, %H:%M:%S"),
            'Arrival_Date': arrival_date.strftime("%Y/%m/%d, %H:%M:%S"),
            'Transit_Time': transit_time,
            'Estimated_Arrival_Time': eta.strftime("%Y/%m/%d, %H:%M:%S"),
            'Distance_Traveled': distance_traveled,
            'On_Time_Delivery': on_time_delivery,
            'Freight_Cost': freight_cost,
            'Billing_Status': billing_status,
            'Customer_Feedback': customer_feedback,
            'Customer_rating': customer_rating,
                     
        }

        delivery_performance.append(performance_data)

    return delivery_performance



#function to generate claims data
def apply_claim(delivery_performance, claim_percentage):
    shipments_claim = random.sample(delivery_performance, k=int(len(delivery_performance) * claim_percentage))
    for claim in shipments_claim:
        claim['Claim_Applied'] = True
        claim['claim_id'] = fake.uuid4()
        claim['claim_date'] = fake.date_between(start_date='-60d', end_date='-31d').strftime('%Y-%m-%d')
        claim['claim_description'] = fake.text(max_nb_chars=100)
        claim['claim_status'] = random.choice(['Pending', 'Approved', 'Rejected'])
        if claim['claim_status']== 'Approved' :
            claim['claim_amount'] = random.uniform(100, 1000) 
            claim['resolution_time'] = random.randint(1, 30)  # Resolution Time (in days)
    
    return delivery_performance



def generate_vehicule_and_shipment(num_vehicles,num_months,num_shipments,claim_percentage):
  
    pre_json,vehicule_id_liste,driver_id_liste  = generate_fake_vehicle_fleet_usage(num_vehicles, num_months)


    fake_delivery_performance = generate_fake_delivery_performance(num_shipments,vehicule_id_liste,driver_id_liste)
    fake_delivery_performance_claims=apply_claim(fake_delivery_performance, claim_percentage)
    pre_json.append({"shipment_list":fake_delivery_performance_claims})
    return pre_json







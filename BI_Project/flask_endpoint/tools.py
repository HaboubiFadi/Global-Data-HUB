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

    monthly_usage_list=[]
    for _ in range(num_vehicles):
        # Vehicle information
        vehicle_id = str(uuid.uuid4())
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
                'Month': month,
                'id': id,
                'Income': income
            })

        for month in range(1, num_months + 1):
         
            id_usage=str(uuid.uuid4())
            distance_traveled = random.uniform(200, 800)
            mileage_end += distance_traveled
         
            monthly_usage.append({
                'Vehicle_ID': vehicle_id,
                'Month': month,
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
   
                'id': id_history,
                'Date': maintenance_date.strftime('%Y-%m-%d'),
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
                'Month': month,
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
                'Month': month,
                'id': id_driving,
                'Driving_Time': driving_time,
                'Traffic_Violation Number': traffic_violation_nb,
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

    return pre_json_liste   










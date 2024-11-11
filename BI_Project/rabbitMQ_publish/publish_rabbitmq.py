#producer

from faker import Faker
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





def generate_fake_insurance_data(num_records):
    insurance_data = []
    fake = Faker()

    for j in range(num_records):
        # Existing variables
        agency_name = fake.company()
        location = fake.city()
        num_employees = random.randint(5, 100)
        years_in_business = random.randint(1, 30)
        policies_offered = random.choices(['All-Risk Cargo Insurance', 'Named Perils Cargo Insurance', 'Valuable Cargo Insurance','Warehouse-to-Warehouse Cargo Insurance', 'Voyage Policy', 'Open Cargo Policy'], k=random.randint(1, 6))
        coverage_limits = [random.randint(100000, 1000000) for _ in range(len(policies_offered))]
        premium_rates = [round(random.uniform(1000, 5000), 2) for _ in range(len(policies_offered))]
        types_of_risk_accepted = random.choice(['Comprehensive', 'Selective'])
        Consumer_evaluation = random.choice(['Exceptional', 'Excellent', 'Satisfactory', 'Mediocre', 'Not recommended'])
        average_rating = round(random.uniform(2.0, 5.0), 2)
        customer_support_availability = random.choice(['24/7', 'Business Hours'])
        customer_base = random.choice(['Local', 'Regional', 'National', 'International'])
        use_of_technology = random.choice(['High', 'Moderate', 'Low'])
        compliance_with_regulations = random.choice(['Yes', 'No'])
        claims_handling_process = random.choice(['Efficient', 'Moderate', 'Inefficient'])

        # New variables
        pricing_method = random.choice(['priori pricing', 'posteriori pricing'])
        claim_frequency = random.randint(0, 1000)
        average_claim_amount = round(random.uniform(100, 10000), 2)
        fraud_detection_rate = round(random.uniform(0, 100), 2)
        esg_score = round(random.uniform(1, 5), 2)
        competition_analysis = round(random.uniform(0, 100), 2)

        # Variables with conditions

        # Revenue-related Variables:
        annual_revenue = round(random.uniform(1000000, 10000000), 2) if num_employees > 20 else round(random.uniform(100000, 1000000), 2)
        profitability = round(random.uniform(0.1, 0.5), 2) if years_in_business > 5 else round(random.uniform(0.05, 0.3), 2)
        market_share = round(random.uniform(5, 30), 2) if annual_revenue > 2000000 else round(random.uniform(1, 15), 2)
        market_penetration = round(random.uniform(0, 100), 2) if profitability > 0.3 else round(random.uniform(0, 50), 2)

        # Employee-related Variables:
        employee_satisfaction_index = round(random.uniform(3.0, 5.0), 2) if num_employees > 10 else round(random.uniform(2.0, 4.5), 2)
        employee_turnover_rate = round(random.uniform(0, 50), 2) if employee_satisfaction_index > 4 else round(random.uniform(10, 70), 2)

        # Claim-related Variables:
        claim_settlement_time = round(random.uniform(1, 30), 2) if average_rating > 3.5 else round(random.uniform(5, 20), 2)
        claim_approval_rate = round(random.uniform(80, 100), 2) if claim_settlement_time < 10 else round(random.uniform(70, 95), 2)

        # Customer-related Variables:
        customer_retention_rate = round(random.uniform(0, 100), 2) if market_share > 15 else round(random.uniform(20, 80), 2)
        customer_acquisition_cost = round(random.uniform(100, 10000), 2) if customer_retention_rate > 50 else round(random.uniform(500, 5000), 2)

        # Technology and Compliance-related Variables:
        online_presence = round(random.uniform(0, 100), 2) if esg_score > 3 else round(random.uniform(10, 50), 2)
        compliance_analysis = round(random.uniform(0, 100), 2) if online_presence > 50 else round(random.uniform(20, 80), 2)

        insurance_data.append({
            'agency_name': agency_name,
            'location': location,
            'num_employees': num_employees,
            'years_in_business': years_in_business,
            'employee_satisfaction_index': employee_satisfaction_index,
            'policies_offered': ", ".join(policies_offered),
            'coverage_limits': ", ".join(map(str, coverage_limits)),
            'Premium_Rates': ", ".join(map(str, premium_rates)),
            'types_of_risk_accepted': types_of_risk_accepted,
            'Consumer_evaluation': Consumer_evaluation,
            'average_rating': average_rating,
            'customer_support_availability': customer_support_availability,
            'annual_revenue': annual_revenue,
            'profitability': profitability,
            'claim_settlement_time': claim_settlement_time,
            'claim_approval_rate': claim_approval_rate,
            'market_share': market_share,
            'customer_base': customer_base,
            'use_of_technology': use_of_technology,
            'compliance_with_regulations': compliance_with_regulations,
            'claims_handling_process': claims_handling_process,
            'pricing_method': pricing_method,
            'claim_frequency': claim_frequency,
            'average_claim_amount': average_claim_amount,
            'customer_retention_rate': customer_retention_rate,
            'market_penetration': market_penetration,
            'customer_acquisition_cost': customer_acquisition_cost,
            'employee_turnover_rate': employee_turnover_rate,
            'fraud_detection_rate': fraud_detection_rate,
            'online_presence': online_presence,
            'esg_score': esg_score,
            'competition_analysis': competition_analysis,
            'compliance_analysis':compliance_analysis
        })

    return insurance_data

def Connect_rabbitmq(config):
    credentials = pika.PlainCredentials("admin","admin")
    connection= pika.BlockingConnection(pika.ConnectionParameters(host=config['host'], credentials= credentials))
    channel= connection.channel()
    channel.exchange_declare(config['exchange'], durable=True, exchange_type="topic")

    channel.queue_declare(queue= config['queue'])
    channel.queue_bind(exchange=config['exchange'], queue=config['queue'], routing_key=config['queue'])    
    return channel
import json



import pika
def Publish_Insurance_Agency_json(channel,num_records,config):
    #messaging to queue named C
    
    message= generate_fake_insurance_data(num_records)
    channel.basic_publish(exchange=config['exchange'], routing_key=config['queue'], body= json.dumps(message))
    channel.close()




config={'host':'localhost','exchange':'test','queue':"topic_ic"}

channel=Connect_rabbitmq(config)
Publish_Insurance_Agency_json(channel,100,config)
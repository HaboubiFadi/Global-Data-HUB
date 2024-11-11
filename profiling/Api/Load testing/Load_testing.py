from locust import HttpUser ,task,between ,TaskSet
import json
class UserTesting (TaskSet):

    

    @task
    def predict_Classification_Comfort(self):
        # Define the payload for the POST request
        dic_Comfort={'Digital_Engagement_Score':10,'Use_of_Technology':2,'Fraud_Detection_Efficiency':0}

        headers = {'Content-Type': 'application/json','Authorization':"Bearer Fadi"}        

        # Send a POST request to the predict endpoint
        return_value=self.client.post("Comfort/Comfort_Classification/predict", data=json.dumps(dic_Comfort), headers=headers)
        print(return_value)


    @task
    def predict_Classification_Price(self):
        # Define the payload for the POST request
        dic_price={'premium_median':8000,'coverage_limit_median':1000000,'Pricing_Method':1}
        dic_price['price_ratio_median']=float(dic_price['coverage_limit_median']/ (dic_price['premium_median']))
        headers = {'Content-Type': 'application/json','Authorization':"Bearer Fadi"}        

        # Send a POST request to the predict endpoint
        return_value=self.client.post("Price/Price_Classification/predict", data=json.dumps(dic_price), headers=headers)
        print(return_value)

    @task
    def predict_recommendation_Classification(self):
        # Define the payload for the POST request
        
        dic={'Financial_solidity':2,'Financial_dynamics':2,'Price_Score':1,'Comfort_score':2,'Service_score':2}

        headers = {'Content-Type': 'application/json','Authorization':"Bearer Fadi"}        
        # Send a POST request to the predict endpoint
        return_value=self.client.post("Recommendation/Recommendation_Classification/predict", data=json.dumps(dic), headers=headers)
        print(return_value)
    
    #
    @task
    def predict_Service_Classification(self):
        # Define the payload for the POST request
        
        dic={'Claim_Settlement_Time':2,'Claim_Approval_Rate':2,'Claims_Handling_Process':1}

        headers = {'Content-Type': 'application/json','Authorization':"Bearer Fadi"}        
        # Send a POST request to the predict endpoint
        return_value=self.client.post("Service/Service_Classification/predict", data=json.dumps(dic), headers=headers)
        print(return_value)        
    
    
    @task
    def predict_Financial_s_Classification(self):
        # Define the payload for the POST request
        


        dic={'Claim_Frequency':200,'Customer_Acquisition_Cost':150,'Years_in_Business':30,'Customer_Base':2,'Loss_Ratio':1.6,'Employee_Satisfaction_Impact':1,'Average_Customer_Revenue':10000}
        headers = {'Content-Type': 'application/json','Authorization':"Bearer Fadi"}        
        # Send a POST request to the predict endpoint
        return_value=self.client.post("Financial_s/Financial_s_Classification/predict", data=json.dumps(dic), headers=headers)
        print(return_value)   
    
    @task
    def predict_Financial_d_Classification(self):
        # Define the payload for the POST request
        
        dic={'Types_of_Risk_Accepted':2,'Profitability':1.6,'Market_Penetration':2,'ESG_Score':1,'Revenue_Growth_Rate':1.6,'Annual_Revenue':10000}
        

        
        
        headers = {'Content-Type': 'application/json','Authorization':"Bearer Fadi"}        
        # Send a POST request to the predict endpoint
        return_value=self.client.post("Financial_d/Financial_d_Classification/predict", data=json.dumps(dic), headers=headers)
        print(return_value)
    
    @task
    def predict_Rating_Regression(self):
        # Define the payload for the POST request
        
        dic={'Market_Share_Growth_Rate':1.2,'Employee_Satisfaction_Impact':2,'Claim_Settlement_Efficiency':1,
     '  Revenue_Growth_Rate':1.2,'Competition_Analysis':1,'Employee_Turnover_Rate':1.5,'Customer_Acquisition_Cost':10000,
        'Market_Penetration':2,'Loss_Ratio':1.3,'Average_Claim_Amount':12000,
        'Claim_Frequency':1000,'Claims_Handling_Process':2,'Compliance_with_Regulations':1,
        'Use_of_Technology':1,'Customer_Base':2,'Claim_Approval_Rate':0,
        'Claim_Settlement_Time':50,'Profitability':1.3,'Customer_Support_Availability':2,
        'Employee_Satisfaction_Index':1,'Years_in_Business':10,'Number_of_Employees':300}
        
        
        
        
        dic={'Number_of_Employees'        :   300,
        'Years_in_Business'             :     12,
        'Employee_Satisfaction_Index'   :   1,
        'Customer_Support_Availability' :     2,
        'Profitability'                 :   1.3,
        'Claim_Settlement_Time'         :   30,
        'Claim_Approval_Rate'           :   2,
        'Customer_Base'                 :     2,
        'Use_of_Technology'             :     2,
        'Compliance_with_Regulations'   :     1,
        'Claims_Handling_Process'      :      1,
        'Claim_Frequency'              :      300,
        'Average_Claim_Amount'         :    20000,
        'Loss_Ratio'                   :    0.3,
        'Market_Penetration'           :    2,
        'Customer_Acquisition_Cost'   :     10000,
        'Employee_Turnover_Rate'        :   3,
        'Competition_Analysis'         :    2.5,
        'Revenue_Growth_Rate'          :    1.6,
        'Claim_Settlement_Efficiency'  :    2,
        'Employee_Satisfaction_Impact' :    2,
        'Market_Share_Growth_Rate'   : 1.6}

        
        
        
        
        
        
        headers = {'Content-Type': 'application/json','Authorization':"Bearer Fadi"}        
        # Send a POST request to the predict endpoint
        return_value=self.client.post("Rating_regression/rating/predict", data=json.dumps(dic), headers=headers)
        print(return_value)        

    
    
    
    @task
    def predict_Claim_settlement_time_Regression(self):
        # Define the payload for the POST request
        dic={"Number_of_Employees"            :    300,
        "Years_in_Business"                 : 8,
        "Customer_Support_Availability"    :  2,
        "Profitability"                   : 1.6,
        "Claim_Approval_Rate"             : 2,
        "Customer_Base"                   :   1,
        "Use_of_Technology"               :   2,
        "Compliance_with_Regulations"      :  1,
        "Claims_Handling_Process"         :   1,
        "Claim_Frequency"                :    200,
        "Average_Claim_Amount"            : 10000,
        "Loss_Ratio"                      : 0.6,
        "Market_Penetration"              : 1,
        "Customer_Acquisition_Cost"       : 20000,
        "Employee_Turnover_Rate"          : 1.3,
        "Competition_Analysis"            : 2,
        "Revenue_Growth_Rate"            :  0.6,
        "Claim_Settlement_Efficiency"     : 2,
        "Market_Share_Growth_Rate"        : 0.9}

        headers = {'Content-Type': 'application/json','Authorization':"Bearer Fadi"}        
        # Send a POST request to the predict endpoint
        return_value=self.client.post("Claim_settlement_time/Claim_settlement_time/predict", data=json.dumps(dic), headers=headers)
        print(return_value)        

                                                              







class WebsiteUser(HttpUser):
    tasks = [UserTesting]
    wait_time = between(1, 5) 
        

WebsiteUser()
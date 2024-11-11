from pydantic import BaseModel

class Financial_s_Classification_base(BaseModel):
    Claim_Frequency :float
    Customer_Acquisition_Cost :float
    Years_in_Business :float
    Customer_Base : int
    Loss_Ratio :float 
    Employee_Satisfaction_Impact :float
    Average_Customer_Revenue :float


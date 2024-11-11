from pydantic import BaseModel

class Service_Classification_base(BaseModel):
    Claim_Settlement_Time :float
    Claim_Approval_Rate :float
    Claims_Handling_Process :int
    
from pydantic import BaseModel

class recommendation_Classification_base(BaseModel):
    Financial_solidity :int
    Financial_dynamics :int
    Price_Score :int
    Comfort_score:int
    Service_score:int
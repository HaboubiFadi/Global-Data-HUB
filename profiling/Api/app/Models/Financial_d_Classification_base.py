from pydantic import BaseModel



class Financial_d_Classification_base(BaseModel):
    Types_of_Risk_Accepted :int
    Profitability :float
    Market_Penetration :float
    ESG_Score :float
    Revenue_Growth_Rate :float
    Annual_Revenue :float
